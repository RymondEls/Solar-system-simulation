import pygame
import sys
import numpy as np
from entities.star import Star
from entities.planet import Planet
from entities.moon import Moon
from entities.comet import Comet
from entities.asteroid import Asteroid
from entities.spacecraft import Spacecraft
from operations.orbit_simulation import simulate_orbits
from utils.json_load import load_bodies_from_json, save_bodies_to_json
from utils.scene_interaction import *

def main():
    pygame.init()
    font = pygame.font.SysFont("Arial", 16)
    screen = pygame.display.set_mode((1600/1.25, 900/1.25), pygame.RESIZABLE)
    pygame.display.set_caption("Solar System Simulation")
    bodies = load_bodies_from_json("config/solar_system.json")
    
    scale = 250 / 1.496e11
    offset = np.array([screen.get_width() // 2, screen.get_height() // 2], dtype=float)
    time_scale = 1
    dt = 3600
    pause = False
    dragging = False
    last_mouse_pos = pygame.mouse.get_pos()
    tracked_body = None
    running = True
    while running:
        if tracked_body:
            offset[0] = screen.get_width() // 2 - tracked_body.position[0] * scale
            offset[1] = screen.get_height() // 2 - tracked_body.position[1] * scale
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            dragging, scale, offset, tracked_body, last_mouse_pos = handle_mouse_events(
                event, scale, offset, tracked_body, dragging, last_mouse_pos
            )
            pause, time_scale, tracked_body, offset = handle_keyboard_events(
                event, time_scale, tracked_body, offset, pause)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
                bodies, offset, tracked_body = menu(bodies, offset, screen, scale, tracked_body)
        if not pause:
            simulate_orbits(bodies, dt, time_scale)
        
        screen.fill((0, 0, 0))
        for body in bodies:
            body.draw(screen, scale, offset, font)
        pygame.display.flip()

    save_bodies_to_json("config/solar_system_state.json", bodies)
    pygame.quit()
    sys.exit()

main()