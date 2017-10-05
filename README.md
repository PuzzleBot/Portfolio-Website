# Portfolio-Website
This is a website built in Django which was meant to showcase various things I have made. It will eventually be hosted permanently and have its own domain.

## Dependencies

Make sure you have these installed on your computer before trying to host the site on
localhost:

Django
OpenSSL (with TLS 1.2)
Python 2.7.9 or above

## Hosting the website on localhost

First, make sure Django is installed. Installation instructions can be found [here.](https://www.djangoproject.com/download/)

Once that is done, navigate to this directory using the terminal and type "python manage.py runserver" or "make".

The site can then be accessed using any browser at 127.0.0.1:8000.

## What's implemented?

Aside from the aesthetics, the only thing which is really implemented right now is the storage and display of projects on the project page, and the database sanitization that goes with it.

## What's next?

* Hosting it on Amazon Web Services with a proper URL
* Changing the SQLite database to a proper MySQL or PostgreSQL database
* Building a javascript applet embedded into one of the pages
* Using Wordpress' API to display my blog entries on the front page