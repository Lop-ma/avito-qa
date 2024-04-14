# Инструкция 
Для выполнения кода и получения скриншотов тест-кейсов в папке "output" необходимо выполнить следующие действия:
1. Склонируйте репозиторий ```git clone https://github.com/Lop-ma/avito-qa.git```
2. Проверить версию Python с помощью команды ```python --version```
3. Если на компьютере не установлен Python версии 3.8+, его можно установить с помощью следующей инструкции 
4. Написать в командной строке 
```
pip install -U virtualenv
python -m virtualenv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
playwright install --with-deps chromium
```
5. Запустить тесты с помощью команды ```pytest```