import pytest
import pygame
from unittest.mock import MagicMock, patch
from utils.scene_interaction import handle_mouse_events, handle_keyboard_events, menu
from entities.planet import Planet
from entities.spacecraft import Spacecraft

# Фикстура для инициализации Pygame
@pytest.fixture(autouse=True)
def init_pygame():
    pygame.init()
    yield
    pygame.quit()

# Фикстура для создания экрана Pygame
@pytest.fixture
def screen():
    return pygame.display.set_mode((800, 600))

# Фикстура для создания списка тел
@pytest.fixture
def bodies():
    return [
        Planet(name="Earth", type="planet", mass=5.972e24, position=[0, 0], velocity=[0, 0], color=(0, 0, 255), radius=6371000, atmosphere="Nitrogen-Oxygen", surface="Rocky"),
        Planet(name="Mars", type="planet", mass=6.4171e23, position=[227.9e9, 0], velocity=[0, 24000], color=(255, 0, 0), radius=3390000, atmosphere="Carbon Dioxide", surface="Rocky")
    ]

# Тесты для handle_mouse_events
def test_handle_mouse_events_left_click():
    event = MagicMock()
    event.type = pygame.MOUSEBUTTONDOWN
    event.button = 1  # Левая кнопка мыши

    dragging, scale, offset, tracked_body, last_mouse_pos = handle_mouse_events(event, 1.0, [0, 0], None, False, None)
    assert dragging is True
    assert last_mouse_pos == pygame.mouse.get_pos()

def test_handle_mouse_events_scroll_up():
    event = MagicMock()
    event.type = pygame.MOUSEBUTTONDOWN
    event.button = 4  # Колесо мыши вверх

    dragging, scale, offset, tracked_body, last_mouse_pos = handle_mouse_events(event, 1.0, [0, 0], None, False, None)
    assert scale == 1.5  # Масштаб увеличился

def test_handle_mouse_events_scroll_down():
    event = MagicMock()
    event.type = pygame.MOUSEBUTTONDOWN
    event.button = 5  # Колесо мыши вниз

    dragging, scale, offset, tracked_body, last_mouse_pos = handle_mouse_events(event, 1.0, [0, 0], None, False, None)
    assert scale == 1.0 / 1.5  # Масштаб уменьшился

# Тесты для handle_keyboard_events
def test_handle_keyboard_events_pause():
    event = MagicMock()
    event.type = pygame.KEYDOWN
    event.key = pygame.K_p  # Клавиша P

    pause, time_scale, tracked_body, offset = handle_keyboard_events(event, 1.0, None, [0, 0], False)
    assert pause is True

def test_handle_keyboard_events_time_scale_up():
    event = MagicMock()
    event.type = pygame.KEYDOWN
    event.key = pygame.K_PLUS  # Клавиша "+"

    pause, time_scale, tracked_body, offset = handle_keyboard_events(event, 1.0, None, [0, 0], False)
    assert time_scale == 2.0  # Масштаб времени увеличился

def test_handle_keyboard_events_time_scale_down():
    event = MagicMock()
    event.type = pygame.KEYDOWN
    event.key = pygame.K_MINUS  # Клавиша "-"

    pause, time_scale, tracked_body, offset = handle_keyboard_events(event, 1.0, None, [0, 0], False)
    assert time_scale == 0.5  # Масштаб времени уменьшился


def test_menu_valid_actions(bodies, capsys):
    with patch("builtins.input") as mock_input:
        # Имитируем ввод действия и последующие ответы
        mock_input.side_effect = [
            "1",  # Действие: Изучение атмосферы
            "1",  # Выбор планеты Earth
            "2",  # Действие: Изучение поверхности
            "1",  # Выбор планеты Earth
            "3",  # Действие: Сбор данных
            "1",  # Выбор тела Earth
            "4",  # Действие: Запуск космического аппарата
            "Apollo",  # Название аппарата
            "5000",  # Масса
            "0",  # Скорость по x
            "0",  # Скорость по y
            "5",  # Радиус
            "Moon Landing",  # Миссия
            "5",  # Действие: Слежение за телом
            "1",  # Выбор тела Earth
        ]

        # Вызываем меню и проверяем вывод
        for _ in range(5):  # Проверяем все 5 действий
            bodies, offset, tracked_body = menu(bodies, [0, 0], MagicMock(), 1.0, None)
            captured = capsys.readouterr()

            # Проверяем, что меню отработало без ошибок
            assert "Ошибка" not in captured.out

        # Проверяем, что космический аппарат был добавлен
        assert len(bodies) == 3
        assert isinstance(bodies[-1], Spacecraft)
        assert bodies[-1].name == "Apollo"

# Тест для неверного ввода (число вне диапазона 1-5)
def test_menu_valid_actions(bodies, capsys):
    with patch("builtins.input") as mock_input:
        # Имитируем ввод для всех действий (1-5)
        mock_input.side_effect = [
            "1",  # Действие: Изучение атмосферы
            "1",  # Выбор планеты Earth
            "2",  # Действие: Изучение поверхности
            "1",  # Выбор планеты Earth
            "3",  # Действие: Сбор данных
            "1",  # Выбор тела Earth
            "4",  # Действие: Запуск космического аппарата
            "Apollo",  # Название аппарата
            "5000",  # Масса
            "0",  # Скорость по x
            "0",  # Скорость по y
            "5",  # Радиус
            "Moon Landing",  # Миссия
            "5",  # Действие: Слежение за телом
            "1",  # Выбор тела Earth
        ]

        # Вызываем меню и проверяем вывод
        for _ in range(5):  # Проверяем все 5 действий
            bodies, offset, tracked_body = menu(bodies, [0, 0], MagicMock(), 1.0, None)
            captured = capsys.readouterr()

            # Проверяем, что меню отработало без ошибок
            assert "Ошибка" not in captured.out

        # Проверяем, что космический аппарат был добавлен
        assert len(bodies) == 3
        assert isinstance(bodies[-1], Spacecraft)
        assert bodies[-1].name == "Apollo"


def test_menu_invalid_selection(bodies, capsys):
    with patch("builtins.input") as mock_input:
        # Имитируем ввод действия и неверный выбор
        mock_input.side_effect = [
            "1",  # Действие: Изучение атмосферы
            "999",  # Неверный выбор планеты
        ]

        bodies, offset, tracked_body = menu(bodies, [0, 0], MagicMock(), 1.0, None)
        captured = capsys.readouterr()

        # Проверяем, что меню сообщает о неверном выборе
        assert "Вы ввели число не из списка" in captured.out

