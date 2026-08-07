"""
3D Snake Game — Ursina Engine (optimized: entity pooling, no per-tick create/destroy)

Install first:
    pip install ursina

Run:
    python snake_3d.py

Controls:
    Arrow Keys / WASD  -> move on the X/Z grid
    Space              -> pause / unpause
    Enter              -> restart after Game Over
    Esc                -> quit
"""

from ursina import *
import random

app = Ursina()

# ---------------- Config ----------------
GRID_SIZE = 15
MOVE_INTERVAL = 0.15
MIN_MOVE_INTERVAL = 0.05
SPEEDUP_EVERY = 5
MAX_LENGTH = GRID_SIZE * GRID_SIZE  # pool size cap

window.title = "3D Snake"
window.color = color.rgb(20, 20, 30)
Sky(color=color.rgb(15, 15, 25))

# ---------------- Camera ----------------
camera.position = (GRID_SIZE / 2, GRID_SIZE * 1.3, -GRID_SIZE * 0.9)
camera.rotation_x = 55
camera.fov = 90

# ---------------- Ground / Arena ----------------
Entity(
    model='plane',
    scale=(GRID_SIZE, 1, GRID_SIZE),
    position=(GRID_SIZE / 2 - 0.5, -0.5, GRID_SIZE / 2 - 0.5),
    color=color.rgb(40, 40, 55),
    texture='white_cube',
    texture_scale=(GRID_SIZE, GRID_SIZE),
)

wall_color = color.rgb(80, 80, 100)
Entity(model='cube', color=wall_color, position=(GRID_SIZE / 2 - 0.5, 0, -1),
       scale=(GRID_SIZE + 1, 1, 0.2))
Entity(model='cube', color=wall_color, position=(GRID_SIZE / 2 - 0.5, 0, GRID_SIZE),
       scale=(GRID_SIZE + 1, 1, 0.2))
Entity(model='cube', color=wall_color, position=(-1, 0, GRID_SIZE / 2 - 0.5),
       scale=(0.2, 1, GRID_SIZE + 1))
Entity(model='cube', color=wall_color, position=(GRID_SIZE, 0, GRID_SIZE / 2 - 0.5),
       scale=(0.2, 1, GRID_SIZE + 1))

# ---------------- UI ----------------
score_text = Text(text="Score: 0", position=(-0.85, 0.45), scale=2, color=color.white)
status_text = Text(text="", position=(-0.2, 0.1), scale=2.5, color=color.red, origin=(0, 0))
help_text = Text(text="Arrows/WASD move   Space pause   Enter restart",
                  position=(-0.85, -0.48), scale=1.1, color=color.gray)

HEAD_COLOR = color.azure
BODY_COLOR = color.lime

# ---------------- Entity Pool ----------------
# Pre-create every cube we could ever need once, then just move/show/hide them.
# This avoids the cost (and slowdown) of destroy()/Entity() every single move.
segment_pool = [
    Entity(model='cube', color=BODY_COLOR, scale=0.9, position=(0, -100, 0), enabled=False)
    for _ in range(MAX_LENGTH)
]
food_entity = Entity(model='sphere', color=color.red, scale=0.7, position=(0, -100, 0))


class State:
    pass


s = State()


def reset_game():
    s.body = [(GRID_SIZE // 2, GRID_SIZE // 2)]
    s.direction = (1, 0)
    s.pending_direction = s.direction
    s.grow_pending = 0
    s.score = 0
    s.move_timer = 0
    s.move_interval = MOVE_INTERVAL
    s.paused = False
    s.game_over = False

    # Hide all pooled segments, then show just the head
    for seg in segment_pool:
        seg.enabled = False

    s.food_pos = spawn_food()
    food_entity.position = (s.food_pos[0], 0, s.food_pos[1])

    score_text.text = "Score: 0"
    status_text.text = ""

    sync_segments()


def spawn_food():
    while True:
        pos = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))
        if pos not in s.body:
            return pos


def opposite(a, b):
    return a[0] == -b[0] and a[1] == -b[1]


def sync_segments():
    """Reposition pooled entities to match s.body, without creating/destroying anything."""
    for i, seg in enumerate(segment_pool):
        if i < len(s.body):
            x, z = s.body[i]
            seg.position = (x, 0, z)
            seg.color = HEAD_COLOR if i == 0 else BODY_COLOR
            seg.enabled = True
        else:
            seg.enabled = False


def input(key):
    if s.game_over:
        if key == 'enter':
            reset_game()
        return

    if key == 'space':
        s.paused = not s.paused
        status_text.text = "PAUSED" if s.paused else ""
        return

    new_dir = None
    if key in ('up arrow', 'w'):
        new_dir = (0, 1)
    elif key in ('down arrow', 's'):
        new_dir = (0, -1)
    elif key in ('right arrow', 'd'):
        new_dir = (1, 0)
    elif key in ('left arrow', 'a'):
        new_dir = (-1, 0)

    if new_dir:
        # Compare against the last *requested* direction (not the last applied one)
        # so two fast key taps in the same tick can't sneak in an illegal U-turn.
        current = s.pending_direction
        if not (len(s.body) > 1 and opposite(new_dir, current)):
            s.pending_direction = new_dir


def update():
    if s.game_over or s.paused:
        return

    s.move_timer += time.dt
    if s.move_timer < s.move_interval:
        return
    s.move_timer = 0

    s.direction = s.pending_direction
    head_x, head_z = s.body[0]
    new_head = (head_x + s.direction[0], head_z + s.direction[1])

    if not (0 <= new_head[0] < GRID_SIZE and 0 <= new_head[1] < GRID_SIZE):
        trigger_game_over()
        return

    body_check = s.body if s.grow_pending > 0 else s.body[:-1]
    if new_head in body_check:
        trigger_game_over()
        return

    s.body.insert(0, new_head)

    if new_head == s.food_pos:
        s.score += 1
        score_text.text = f"Score: {s.score}"
        s.grow_pending += 1
        if len(s.body) < MAX_LENGTH:
            s.food_pos = spawn_food()
            food_entity.position = (s.food_pos[0], 0, s.food_pos[1])
        if s.score % SPEEDUP_EVERY == 0:
            s.move_interval = max(MIN_MOVE_INTERVAL, s.move_interval - 0.01)

    if s.grow_pending > 0:
        s.grow_pending -= 1
    else:
        s.body.pop()

    sync_segments()


def trigger_game_over():
    s.game_over = True
    status_text.text = "GAME OVER — Press Enter to Restart"


reset_game()
app.run()