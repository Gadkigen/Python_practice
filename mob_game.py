import pygame
import random
import math

# ─── INIT ───────────────────────────────────────────────
pygame.init()
WIDTH, HEIGHT = 480, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mob Control")
clock = pygame.time.Clock()

# ─── COLORS ─────────────────────────────────────────────
WHITE      = (255, 255, 255)
BLACK      = (10,  10,  10)
BLUE       = (30,  144, 255)
RED        = (220, 50,  50)
GREEN      = (50,  200, 100)
YELLOW     = (255, 210, 0)
GRAY       = (180, 180, 180)
DARK_GRAY  = (60,  60,  60)
ORANGE     = (255, 140, 0)

# ─── FONTS ──────────────────────────────────────────────
font_big   = pygame.font.SysFont("Arial", 48, bold=True)
font_med   = pygame.font.SysFont("Arial", 28, bold=True)
font_small = pygame.font.SysFont("Arial", 20)

# ─── GATE CLASS ─────────────────────────────────────────
class Gate:
    def __init__(self, x, y, operation, value, color):
        self.rect  = pygame.Rect(x, y, 90, 44)
        self.op    = operation   # 'x' or '+'
        self.value = value
        self.color = color
        self.speed = 2

    def update(self):
        self.rect.y += self.speed

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, border_radius=10)
        pygame.draw.rect(surface, WHITE, self.rect, 2, border_radius=10)
        label = f"{self.op}{self.value}"
        txt = font_med.render(label, True, WHITE)
        surface.blit(txt, txt.get_rect(center=self.rect.center))

# ─── UNIT (mob dot) CLASS ───────────────────────────────
class Unit:
    def __init__(self, x, y):
        self.x  = float(x)
        self.y  = float(y)
        self.vx = random.uniform(-1, 1)
        self.vy = random.uniform(-1, 1)
        self.r  = 8

    def update(self, target_x, target_y):
        # Drift toward formation center
        dx = target_x - self.x
        dy = target_y - self.y
        self.vx += dx * 0.02
        self.vy += dy * 0.02
        # Dampen
        self.vx *= 0.9
        self.vy *= 0.9
        self.x += self.vx
        self.y += self.vy

    def draw(self, surface):
        pygame.draw.circle(surface, BLUE,   (int(self.x), int(self.y)), self.r)
        pygame.draw.circle(surface, WHITE,  (int(self.x), int(self.y)), self.r, 2)

# ─── ENEMY CLASS ────────────────────────────────────────
class Enemy:
    def __init__(self, count):
        self.x     = random.randint(60, WIDTH - 60)
        self.y     = -40
        self.count = count
        self.r     = 18
        self.speed = 1.5

    def update(self):
        self.y += self.speed

    def draw(self, surface):
        pygame.draw.circle(surface, RED,   (int(self.x), int(self.y)), self.r)
        pygame.draw.circle(surface, WHITE, (int(self.x), int(self.y)), self.r, 2)
        txt = font_small.render(str(self.count), True, WHITE)
        surface.blit(txt, txt.get_rect(center=(int(self.x), int(self.y))))

# ─── GAME STATE ─────────────────────────────────────────
def new_game():
    units   = [Unit(WIDTH//2 + random.randint(-30,30),
                    HEIGHT - 120 + random.randint(-20,20)) for _ in range(5)]
    gates   = []
    enemies = []
    return units, gates, enemies

def spawn_gate_pair():
    ops    = [('+', random.randint(2,10), GREEN),
              ('x', random.randint(2, 4), ORANGE),
              ('+', random.randint(1, 5), GREEN),
              ('+', random.randint(5,15), GREEN)]
    left   = random.choice(ops)
    right  = random.choice(ops)
    gap    = 20
    lx     = random.randint(20, WIDTH//2 - 100)
    rx     = lx + 90 + gap + random.randint(10, 60)
    if rx + 90 > WIDTH - 20:
        rx = WIDTH - 20 - 90
    y = -60
    return [Gate(lx, y, left[0],  left[1],  left[2]),
            Gate(rx, y, right[0], right[1], right[2])]

# ─── MAIN LOOP ──────────────────────────────────────────
def main():
    units, gates, enemies = new_game()
    score        = 0
    mob_x        = WIDTH // 2
    spawn_timer  = 0
    enemy_timer  = 0
    game_over    = False
    win          = False
    level        = 1
    boss_count   = 30

    while True:
        clock.tick(60)
        screen.fill(DARK_GRAY)

        # ── Draw road ──
        pygame.draw.rect(screen, (50, 50, 60), (60, 0, WIDTH-120, HEIGHT))
        for i in range(0, HEIGHT, 60):
            pygame.draw.rect(screen, (80, 80, 90), (WIDTH//2 - 5, i, 10, 35))

        # ── Events ──
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    units, gates, enemies = new_game()
                    score = mob_x = 0
                    mob_x = WIDTH//2
                    spawn_timer = enemy_timer = 0
                    game_over = win = False; level = 1
                    boss_count = 30

        if game_over or win:
            msg   = "YOU WIN! 🎉" if win else "GAME OVER"
            color = GREEN if win else RED
            txt   = font_big.render(msg, True, color)
            screen.blit(txt, txt.get_rect(center=(WIDTH//2, HEIGHT//2 - 30)))
            txt2  = font_med.render("Press R to restart", True, WHITE)
            screen.blit(txt2, txt2.get_rect(center=(WIDTH//2, HEIGHT//2 + 30)))
            pygame.display.flip(); continue

        # ── Mouse / touch controls ──
        mx, _ = pygame.mouse.get_pos()
        mob_x += (mx - mob_x) * 0.15
        mob_x  = max(80, min(WIDTH - 80, mob_x))

        # ── Spawn gates ──
        spawn_timer += 1
        if spawn_timer > max(90 - level*5, 40):
            gates += spawn_gate_pair()
            spawn_timer = 0

        # ── Spawn enemies ──
        enemy_timer += 1
        if enemy_timer > max(180 - level*10, 60):
            enemies.append(Enemy(random.randint(5, 10 + level*3)))
            enemy_timer = 0

        # ── Update gates ──
        for g in gates[:]:
            g.update()
            # Check collision with any unit
            for u in units[:]:
                if g.rect.collidepoint(u.x, u.y):
                    if g.op == '+':
                        for _ in range(g.value):
                            units.append(Unit(mob_x + random.randint(-30,30),
                                              HEIGHT - 120 + random.randint(-20,20)))
                    elif g.op == 'x':
                        current = len(units)
                        for _ in range(current * (g.value - 1)):
                            units.append(Unit(mob_x + random.randint(-40,40),
                                              HEIGHT - 120 + random.randint(-20,20)))
                    gates.remove(g)
                    break
            else:
                if g.rect.y > HEIGHT:
                    gates.remove(g)

        # ── Update enemies ──
        for e in enemies[:]:
            e.update()
            # Battle: check if any unit touches enemy
            for u in units[:]:
                dist = math.hypot(u.x - e.x, u.y - e.y)
                if dist < e.r + u.r:
                    e.count  -= 1
                    units.remove(u)
                    if e.count <= 0:
                        enemies.remove(e)
                        score += 10
                        level  = 1 + score // 50
                    break
            else:
                if e.y > HEIGHT:
                    enemies.remove(e)

        # ── Cap units ──
        if len(units) > 200:
            units = units[:200]

        # ── Check lose ──
        if len(units) == 0:
            game_over = True

        # ── Check win (reach 500 score) ──
        if score >= 500:
            win = True

        # ── Update & draw units ──
        for u in units:
            u.update(mob_x + random.uniform(-40, 40), HEIGHT - 120)
            u.draw(screen)

        # ── Draw gates & enemies ──
        for g in gates:   g.draw(screen)
        for e in enemies: e.draw(screen)

        # ── HUD ──
        # Mob count badge
        pygame.draw.circle(screen, YELLOW, (50, 50), 30)
        cnt = font_med.render(str(len(units)), True, BLACK)
        screen.blit(cnt, cnt.get_rect(center=(50, 50)))

        # Score
        sc_txt = font_med.render(f"Score: {score}", True, WHITE)
        screen.blit(sc_txt, (WIDTH//2 - sc_txt.get_width()//2, 15))

        # Level
        lv_txt = font_small.render(f"Level {level}", True, GRAY)
        screen.blit(lv_txt, (WIDTH - 80, 20))

        pygame.display.flip()

main()