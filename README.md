## Требования

- Python 3.10 или выше
- PyQt6
- openpyxl (для экспорта в Excel)
- GitHub аккаунт с персональным токеном доступа
- GusHub аккаунт с правами администратора

### Получение персонального токена GitHub

1. Войдите в свой аккаунт GitHub
2. Нажмите на свой аватар в правом верхнем углу
3. Выберите "Settings" (Настройки)
4. В левом меню прокрутите вниз и выберите "Developer settings" (Настройки разработчика)
5. Выберите "Personal access tokens" (Персональные токены доступа) -> "Tokens (classic)"
6. Нажмите "Generate new token" (Создать новый токен) -> "Generate new token (classic)"
7. Заполните форму:
   - Note (Заметка): "Gushub App"
   - Expiration (Срок действия): выберите подходящий срок (например, 90 дней)
   - Выберите следующие разрешения:
     - `repo` (полный доступ к репозиториям)
     - `white:packages` (загрузка пакетов)
     - `delete:packages` (удаление пакетов)
     - `delete_repo` (удаление репозиториев)
8. Нажмите "Generate token" (Создать токен)
9. **ВАЖНО**: Скопируйте токен сразу после создания, так как он больше не будет доступен для просмотра

### База данных

Скрипт базы данных находится в папке "Database". Файл "diplom_gushub.sql".

## Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/AtsumiAsuna/diplom_Yuldasheva.git
cd gushub_app
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

## Запуск

```bash
python main.py
```

## Сборка exe-файла (Windows)

Для сборки приложения в исполняемый файл:

1. Установите зависимости для разработки:
   ```bash
   pip install -r requirements-build.txt
   ```

2. Соберите приложение:
   ```bash
   pyinstaller gushub.spec
   ```

3. Готовый exe-файл появится в папке `dist`.

