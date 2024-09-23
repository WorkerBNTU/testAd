# Logs Viewer

## Установка

1. **Клонируйте репозиторий:**

   ```bash
   git clone https://github.com/WorkerBNTU/testAd.git
   cd logs
   ```

2. **Установите зависимости:**

   ```bash
   pip install -r requirements.txt
   ```
   
3. **Создайте .env файл:**

   ```python
   SECRET_KEY='your-secret-key'
   ```

4. **Примените миграции:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
   
5. **Создайте случайные данные:**

   ```bash
   python manage.py load_data
   ```

6. **Запустите сервер:**

   ```bash
   python manage.py runserver
   ```
   
## Использование

   + Откройте браузер и перейдите по адресу http://127.0.0.1:8000.
   + Кликайте по логам, чтобы открыть или скрыть подробную информацию.
   + Нажмите на ссылку, чтобы скачать (файлов нет, поэтому ничего не скачается)
