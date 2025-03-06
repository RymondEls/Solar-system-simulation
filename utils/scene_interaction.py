import pygame
from operations.atmosphere_study import study_atmosphere
from operations.surface_study import study_surface
from operations.data_collection import collect_data
from entities.spacecraft import Spacecraft

def handle_mouse_events(event, scale, offset, tracked_body, dragging, last_mouse_pos):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            dragging = True
            tracked_body = 0
            last_mouse_pos = pygame.mouse.get_pos()
        elif event.button == 4:
            scale *= 1.5
        elif event.button == 5:
            scale /= 1.5

    elif event.type == pygame.MOUSEBUTTONUP:
        if event.button == 1: 
            dragging = False

    elif event.type == pygame.MOUSEMOTION:
        if dragging:
            current_mouse_pos = pygame.mouse.get_pos()
            dx = current_mouse_pos[0] - last_mouse_pos[0]
            dy = current_mouse_pos[1] - last_mouse_pos[1]
            offset[0] += dx
            offset[1] += dy
            last_mouse_pos = current_mouse_pos

    return dragging, scale, offset, tracked_body, last_mouse_pos

def handle_keyboard_events(event, time_scale, tracked_body, offset, pause):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_p:
            return not pause, time_scale, tracked_body, offset
        elif event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS:
            time_scale *= 2
            print(f"Масштаб времени: {time_scale}x")
        elif event.key == pygame.K_MINUS:
            time_scale /= 2
            print(f"Масштаб времени: {time_scale}x")
    return pause, time_scale, tracked_body, offset

def menu(bodies, offset, screen, scale, tracked_body):
    planets = []
    print('''Выберите операцию:
    1. Изучение атмосферы планеты
    2. Изучение поверхности планеты
    3. Сбор данных
    4. Запуск космического аппарата
    5. Слежение за телом''')
    action = input()
    if action == "1":
        print("Выберите планету для изучения атмосферы:")
        i = 1
        for planet in bodies:
            if planet.type == "planet":
                planets.append(planet)
                print(f"{i}. {planet.name}")
                i += 1
        try :
            study_planet = int(input())
            if study_planet > 0 and study_planet <= planets.__len__():
                study_planet = planets[study_planet-1]
                study_atmosphere(study_planet)
            else: print("Вы ввели число не из списка")
        except ValueError:
            print("Ошибка: введите число.")
    elif action == "2":
        print("Выберите планету для изучения поверхности:")
        i = 1
        for planet in bodies:
            if planet.type == "planet":
                planets.append(planet)
                print(f"{i}. {planet.name}")
                i += 1
        try :
            study_planet = int(input())
            if study_planet > 0 and study_planet <= planets.__len__():
                study_planet = planets[study_planet-1]
                study_surface(study_planet)
            else: print("Вы ввели число не из списка")
        except ValueError:
            print("Ошибка: введите число.")    
    elif action == "3":
        print("Выберите тело для сбора данных:")
        i = 1
        for body in bodies:
            print(f"{i}. {body.name}")
            i += 1
        try :
            data_body = int(input())
            if data_body > 0 and data_body <= bodies.__len__():
                data_body = bodies[data_body-1]
                collect_data(data_body)
            else: print("Вы ввели число не из списка")
        except ValueError:
            print("Ошибка: введите число.")
    elif action == "4":
        names = [body.name for body in bodies]
        print("Запуск космического аппарата. Введите начальные параметры: ")
        name = input("Введите название аппарата: ")
        type = "spacecraft"
        mass = float(input("Введите массу объекта (в кг): "))
        try:
            earth_index = names.index("Earth")
        except ValueError:
            print(f"Земля не найдена, в качестве тела отправления используется Солнце.")
            earth_index = 0
        position = [0,0]
        position[0] = bodies[earth_index].position[0]
        position[1] = bodies[earth_index].position[1] + bodies[earth_index].radius + 10000
        velocity = [0,0]
        velocity[0] = float(input("Введите скорость по x (в м/с): "))
        velocity[1] = float(input("Введите скорость по y (в м/с): "))
        color = (255,255,255)
        radius = float(input("Введите радиус (в метрах): "))
        mission = input("Опишите миссию космического аппарата: ")
        spacecraft = Spacecraft(name, type, mass, position, velocity, color, radius, mission)
        bodies.append(spacecraft)
    elif action == "5":
        print("Выберите тело слежения:")
        for i, body in enumerate(bodies):
            print(f"{i + 1}. {body.name}")
        try:
            input_body = int(input()) - 1
            if 0 <= input_body < len(bodies):
                tracked_body = bodies[input_body]
                offset[0] = screen.get_width() // 2 - tracked_body.position[0] * scale
                offset[1] = screen.get_height() // 2 - tracked_body.position[1] * scale
        except ValueError:
            print("Ошибка: введите число.")
    return bodies, offset, tracked_body
            
