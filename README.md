# Мультиязычный чат-бот
Этот проект представляет собой мультиязычный чат-бот, созданный с использованием платформы с открытым исходным кодом RASA. Чат-бот способен распознавать язык пользователя и отвечать на его запросы на том же языке, обеспечивая более естественное взаимодействие.
## Начало работы
Для локального запуска и разработки чат-бота выполните следующие шаги:
### Предварительные требования
Убедитесь, что у Вас установлены:
- Python 3.8.0
- pip 21.1.1
- <details>
    <summary>Необходимые библиотеки</summary>
	  
  - websockets==10.0
  - googletrans==3.1.0a0
  - transformers==4.38.2
  - rasa==3.1.0
	</details>

## Установка
1. Склонируйте репозиторий
	```bash
	git clone https://github.com/nika953/multilanguage_bot.git
	```
2. Создание и активация виртуального окружения venv.

	>_Перейдите в корневую директорию перед созданием venv._
	
	__Linux__
	```bash
	python3 -m venv venv
	source ./venv/bin/activate
	```
	__Windows(cmd)__
	```bash
	python -m venv venv
	venv\Scripts\activate.bat
	```
	__Windows(PowerShell)__
	```bash
	python -m venv venv
	venv/Scripts/Activate.ps1
	```
3. Установка зависимостей
 	> Уствновите все необходимые зависимости с помощью файла '_requirements.txt_', который находится в корне проекта:
	```bash
    pip install -r requirements.txt --no-cache-dir
	```
## Запуск в режиме консоли:
```bash
rasa run actions # Запуск custom actions
```

```bash
  rasa shell # Запуск модели rasa
```
