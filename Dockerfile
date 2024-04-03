# Используйте базовый образ Python
FROM python:3.8-slim-buster

# Установите рабочую директорию внутри контейнера
WORKDIR /app

# Скопируйте файл requirements.txt в контейнер
COPY requirements.txt requirements.txt

# Установите зависимости из requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Скопируйте все файлы из текущего каталога в контейнер
COPY . .

# Запустите ваше Flet приложение (замените main.py на ваш файл)
CMD ["python", "main.py"]