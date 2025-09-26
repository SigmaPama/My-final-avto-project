# My-final-avto-project

# Автотесты для Kinopoisk.ru

## Структура проекта
- `config/` - Файлы конфигурации и тестовые данные
- `tests/ui/` - UI тесты с использованием Selenium
- `tests/api/` - API тесты с использованием requests
- `utils/` - Вспомогательные классы и утилиты

## Настройка
1. Установите зависимости: `pip install -r requirements.txt`
2. Установите переменные окружения:
   - API_KEY для Kinopoisk API
   - BROWSER (chrome/firefox)
   - HEADLESS (True/False)
   - VALID_EMAIL
   - VALID_PASSWORD
   - VALID_LOGIN

## Запуск тестов
- Только UI тесты: `pytest tests/ui/ -v`
- Только API тесты: `pytest tests/api/ -v`
- Все тесты: `pytest -v`

## Тестовые данные
Обновите тестовые учетные данные в `config/test_data.py` или используйте переменные окружения

## Ссылка на проект ручного тестирования
https://qa-2025.yonote.ru/share/a917a4d2-a9af-4dd9-868e-233af89efe26