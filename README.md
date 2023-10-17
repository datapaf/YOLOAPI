# YOLOAPI

## Установка зависимостей

### Зависимости для YOLO

1. Клонируете репозиторий с YOLO моделью  
```
git clone https://github.com/ultralytics/ultralytics.git
```

2. Затем установите требуемые библиотеки
```
cd ultralytics; pip install -r requirements.txt
```

3. Установите модуль `ultralytics` через pip
```
pip install ultralytics
```

# Запуск API

1. Установите модуль `flask` через pip
```
pip install flask
```

2. Запустите API, задав файл с исходным кодом приложения
```
flask --app api.py run
```

