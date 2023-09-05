# Word Count Challenge using Python and Django

- An web application that receives a text and shows the number of words in the text box.
- This challege was building using python and django.


### How you start the Word Count Challenge Application?

### 1 - Running on local machine
You can run this application on your local machine by following the steps outlined below.
- *It is necessary install and configure Python 3 in your machine before running the application.*

1. Navigate to the folder correct foldel, called 
```bash
cd django_word_count_challenge
```
2. Create a new virtual environment:
```bash
python3 -m venv venv
```
3. Activate the virtual environment:
```bash
source ./venv/bin/activate
```
4. Install the dependencies for this project if you haven't installed them yet:
```bash
(venv) $ python -m pip install -r requirements.txt
```
5. Make and apply the migrations for the project to build your local database:
```bash
(venv) $ python manage.py makemigrations
(venv) $ python manage.py migrate
```
6. Create a superuser that allows you to log in to your Django admin portal:
```bash
(venv) $ python manage.py createsuperuser
```
7. Run the Django development server:
```bash
(venv) $ python manage.py runserver
```
8. Navigate to `http://localhost:8000/` and test the application.


### Stack
- Python3
- Django
- Bootstrap Framework


### References
- [Django Tutorials](https://realpython.com/tutorials/django/)
- [Get Started With Django: Build a Portfolio App](https://realpython.com/get-started-with-django-1/)
- [Manage Your To-Do Lists Using Python and Django](https://realpython.com/django-todo-lists/)
- [Working with forms](https://docs.djangoproject.com/en/4.2/topics/forms/)
