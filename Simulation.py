import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Realistic Smart Adapter Lights Simulation")

# Colors
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
WHITE = (255, 255, 255)
YELLOW_DIM = (100, 100, 0)  
YELLOW_BRIGHT = (255, 255, 0) 

# Road settings
road_y = HEIGHT // 2
lanes = [road_y - 40, road_y + 20]  # Two lanes
streetlights = [(150, road_y - 70), (350, road_y - 70), (550, road_y - 70), (750, road_y - 70)]

# Vehicle settings
class Vehicle:
    def __init__(self, x, y, speed):
        self.rect = pygame.Rect(x, y, 50, 30)
        self.speed = speed

    def move(self):
        self.rect.x += self.speed
        if self.rect.x > WIDTH:
            self.rect.x = -50  # Reset position

# Generate multiple vehicles
vehicles = [Vehicle(random.randint(-200, WIDTH), random.choice(lanes), random.randint(2, 4)) for _ in range(3)]

# Light transition dictionary
light_intensity = {pos: 100 for pos in streetlights}  # Default dim

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(GRAY)
    pygame.draw.rect(screen, BLACK, (0, road_y - 50, WIDTH, 100))  # Road

    # Move vehicles
    for vehicle in vehicles:
        vehicle.move()
        pygame.draw.rect(screen, WHITE, vehicle.rect)

    # Adaptive streetlight brightness
    for (x, y) in streetlights:
        min_distance = min(abs(vehicle.rect.x - x) for vehicle in vehicles)  # Find closest vehicle
        target_brightness = 255 if min_distance < 100 else 100  # Bright when close

        # Smooth brightness transition
        light_intensity[(x, y)] += (target_brightness - light_intensity[(x, y)]) * 0.1  
        light_color = (light_intensity[(x, y)], light_intensity[(x, y)], 0)
        
        pygame.draw.circle(screen, light_color, (x, y), 20)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(30)  # 30 FPS for smooth movement

pygame.quit()
