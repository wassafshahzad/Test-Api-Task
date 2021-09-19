# How to RUN this project

- first install requirements from base.txt
- cd into testapp 
- Run migrations using command `python manage.py migrate`
- Create super user using command `python manage.py createsuperuser`
- Run server using command `python manage.py runserver`
- Login to admin panel at /admin
- Create UserAPIKey for your user
- save the key generated as it is not saved on server for security reasons
- set Authorization header in the format `Authorization:Api-Key <GENERATED API KEY>`
- send POST request to server at /login/ with the format
 {
     "email" : <USER_EMAIL>,
     "password": <USER_PASSWORD>
 }