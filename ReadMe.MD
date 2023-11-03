What you must do for run the project?

1)Install python environment(use terminal for that):
    python -m venv venv; - Windows.
    pi - Windows.
    python3 -m venv venv; - Linux or MacOS.
    source venv/bin/activate. - Linux
    
2)Install needed packages:

pip install django;
pip install djangorestframework;
pip install djangorestframework-simplejwt;
pip install requests;

3)Create a database:
    use the IDE interface - click RMB and choose you foundament directory -> that choose "New" -> File -> db.sqlite3

4)make a migrations:
    python manage.py migration;
    python manage.py makemigrations;
    python manage.py migrate;
    
5)After you can try to run server:
    python manage.py runserver