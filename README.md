# family-recipes

Steps necessary for local setup:
- install Python 3.12 or higher
- install latest Django
- Setup database 
python manage.py migrate
- Populate DB with sample data
python manage.py loaddata initial_data.json
- Start server
python manage.py runserver
-> user front-end: http://127.0.0.1:8000/recipes/ 
-> admin front-end: http://127.0.0.1:8000/admin/
