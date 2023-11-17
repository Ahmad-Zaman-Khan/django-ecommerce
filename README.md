An e-commerce website built with django.
<br>
Here is the link to the live demo: https://ahmad81.pythonanywhere.com

## Features

* Custom User Authentication
* Django Allauth (google authentication)
* Search functionality
* Product Categories
* Related Products

## Local Installation

1. Clone this repo
2. Install `virtualenv` if haven’t installed it
3. Create a new environment - `mkvirtualenv ecommerce`
4. `cd` to cloned repo
installs the required modules:

   pip install -r requirements.txt
Apply the migrations:

   python manage.py migrate
7. `python manage.py createsuperuser` - create an admin user
8. Navigate to http://localhost:8000/admin and enter the credentials from the previous step
9. From left panel click on Pages then choose “Home page” from “Add…” dropdown
10. Fill in the fields, scroll down to “Meta data” tab and type “/” without quotes in URL field
11. Click Save and navigate to http”//localhost:8000

