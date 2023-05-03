Как запустить проект:

1. Клонировать репозиторий: 
git clone git@github.com:bauman1922/api_final_yatube.git

2. Перейти в него в командной строке: 
cd api_final_yatube

3. Cоздать и активировать виртуальное окружение: 
python -m venv env 
source env/bin/activate

4. Установить зависимости из файла requirements.txt:
python -m pip install --upgrade pip
pip install -r requirements.txt

5. Выполнить миграции:
python manage.py migrate

6. Запустить проект:
python manage.py runserver
