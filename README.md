# NeoFIChat

#Local Server Setup 

python -m venv venv
source venv/Scripts/activate
pip install -r requirements

#Docker and Redis Docker image should be available
docker run --rm -p 6379:6379 redis:7

#Steps to run
python manage.py makemigrations
python manage.py migrate

python manage.py runserver
