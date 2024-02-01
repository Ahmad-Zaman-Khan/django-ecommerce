An e-commerce website built with django.
<br>
[Check out the Live Demo](https://ahmad81.pythonanywhere.com/))



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
5. Install the required modules:

   `pip install -r requirements.txt`

6. Apply the migrations:

   `python manage.py migrate`

7. Create an admin user:

   `python manage.py createsuperuser`

8. Run The Server:

   `python manage.py runserver`

9. Navigate to http://localhost:8000/admin and enter the credentials from the previous step.
10. Checkout the homepage http://localhost:8000/

