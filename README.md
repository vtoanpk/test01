# test02

#RUN ON LOCAL

Code for products


Step1:  Clone my project to your computer

$ git clone https://github.com/vtoanpk/test02.git

Step2: Open the project that you have just downloaded, Create a virtual environment

$ virtualenv env

Step3: Activate virtual environments

$ source env/bin/activate

Step4: Install packages for prorject

$ pip3 install -r requirements.txt

Step5: Migrate database and runserver

$ python3 manage.py migrate

$ python3 manage.py rusnerver

# DEPLOY TO HEROKU

# Firstly, Heroku needs us to install a few new packages. Go to your console with virtualenv activated and type this:

$ pip3 install dj-database-url gunicorn whitenoise

# After the installation is finished, go to the test02 directory and run this command:

$ pip3 freeze > requirements.txt

# Open this file requirements.txt and add the following line at the bottom:

psycopg2==2.8.5

# Create a file called Procfile in test02 directory and add this line:

web: gunicorn test02.wsgi --log-file -

# We also need to tell Heroku which Python version we want to use, Create a file called runtime.txt in test02 directory and add this line:

python-3.8.2

#  Another thing we need to do is modify our website's settings.py file. Open product_project/settings.py in your editor and change/add the following lines:

import dj_database_url

...

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', '.herokuapp.com']

...

DATABASES = {

    'default': {
    
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
       
        'NAME': 'vtoanpkdb',
        
        'USER': 'vtoanpk',
        
        'PASSWORD': '',
        
        'HOST': 'localhost',
        
        'PORT': '',
        
    }
    
}

...

db_from_env = dj_database_url.config(conn_max_age=500)

DATABASES['default'].update(db_from_env)

# Open the product_project/wsgi.py file and add these lines at the end:

from whitenoise.django import DjangoWhiteNoise

application = DjangoWhiteNoise(application)

# Then authenticate your Heroku account on your computer by running this command:

$ heroku login

# And we commit our changes

$ git status

$ git add -A .

$ git commit -m "additional files and changes for Heroku"


# Createa a app o heroku

$ heroku create vtoanpk

# Deploy to Heroku!

$ git push heroku master

$ heroku ps:scale web=1

We need to run the migrate and createsuperuser commands.

This time, they come via a special command-line on our own computer, heroku run:

$ heroku run python manage.py migrate

$ heroku run python manage.py createsuperuser

#DONE
