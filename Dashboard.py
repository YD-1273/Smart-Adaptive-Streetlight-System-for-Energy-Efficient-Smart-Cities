import pygame
import streamlit as st
import random
import time
import threading

# Initialize Pygame
def run_simulation(shared_data):
    pygame.init()
    WIDTH, HEIGHT = 800, 400
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Smart Adapter Lights Simulation")

    BLACK = (0, 0, 0)
    GRAY = (100, 100, 100)
    WHITE = (255, 255, 255)
    
    road_y = HEIGHT // 2
    lanes = [road_y - 40, road_y + 20]
    streetlights = [(150, road_y - 70), (350, road_y - 70), (550, road_y - 70), (750, road_y - 70)]

    class Vehicle:
        def __init__(self, x, y, speed):
            self.rect = pygame.Rect(x, y, 50, 30)
            self.speed = speed

        def move(self):
            self.rect.x += self.speed
            if self.rect.x > WIDTH:
                self.rect.x = -50

    vehicles = [Vehicle(random.randint(-200, WIDTH), random.choice(lanes), random.randint(2, 4)) for _ in range(3)]
    light_intensity = {pos: 100 for pos in streetlights}
    running = True
    clock = pygame.time.Clock()

    while running:
        screen.fill(GRAY)
        pygame.draw.rect(screen, BLACK, (0, road_y - 50, WIDTH, 100))

        for vehicle in vehicles:
            vehicle.move()
            pygame.draw.rect(screen, WHITE, vehicle.rect)

        total_energy = 0
        for (x, y) in streetlights:
            min_distance = min(abs(vehicle.rect.x - x) for vehicle in vehicles)
            target_brightness = 255 if min_distance < 100 else 100
            light_intensity[(x, y)] += (target_brightness - light_intensity[(x, y)]) * 0.1
            light_color = (light_intensity[(x, y)], light_intensity[(x, y)], 0)
            pygame.draw.circle(screen, light_color, (x, y), 20)

            # Calculate energy consumption (arbitrary unit)
            energy_usage = light_intensity[(x, y)] / 255 * 10
            total_energy += energy_usage
            shared_data[(x, y)] = ("ON" if light_intensity[(x, y)] > 150 else "OFF", round(energy_usage, 2))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()
        clock.tick(30)

    pygame.quit()

# Streamlit UI
def start_dashboard():
    st.title("Smart Adapter Lights Dashboard")
    st.write("This dashboard controls the smart lighting simulation.")
    shared_data = {pos: ("OFF", 0) for pos in [(150, 330), (350, 330), (550, 330), (750, 330)]}

    if st.button("Start Simulation"):
        threading.Thread(target=run_simulation, args=(shared_data,), daemon=True).start()
        time.sleep(1)
        st.success("Simulation Running!")
    
    status_placeholder = st.empty()

    while True:
        status_text = "\n".join([f"Streetlight at {pos}: Status = {status}, Energy = {energy} units" for pos, (status, energy) in shared_data.items()])
        status_placeholder.text(status_text)
        time.sleep(1)

if __name__ == "__main__":
    start_dashboard()
