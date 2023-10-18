# YOLOAPI

## Установка зависимостей

### Зависимости для YOLO

1. Клонируете репозиторий с YOLO моделью  
```
git clone https://github.com/ultralytics/ultralytics.git
```

2. Затем установите требуемые библиотеки
```
pip install -r ultralytics/requirements.txt
```

3. Установите модуль `ultralytics` через pip
```
pip install ultralytics
```

# Запуск API

1. Установите модуль `fastapi` через pip
```
pip install fastapi[all]
```

2. Запустите API, задав файл с исходным кодом приложения
```
uvicorn api:app --reload
```

