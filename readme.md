# Project API

Trell Hackathon - Project implementing better visualizations of user responses. Hence recommending better.

## Getting Started

To get started on your PC. Clone the repository. And then in virtual environment install
the dependencies by
```
pip install -r requirement.txt
```

For Populating the DB with tables

```
python manage.py makemigrations
python manage.py migrate
```

Then simply run in project directory

```
python manage.py runserver
```
OR for Linux
```
python3 manage.py runserver
```