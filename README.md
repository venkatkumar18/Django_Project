# Django_Project
Created basic CRUD operations with django rest framework.

Packages Used 
  *django                      - version =4.0.3   (pip install Django)
  *djangorestframework version - version =3.13.1  (pip install djangorestframework)
  *django-cors-headers version - version =3.11.0  (pip install django-cors-headers)

Added ('rest_framework','api.apps.ApiConfig') inside installed_apps in settings.py
Added (api.middleware.CustomMiddleware) inside middleware in settings.py

created apps    -> "api"
Middleware used -> CustomMiddleware , Not added any functionality just added print statements to check the working of that middleware.
Http methods    -> Used some http methods like get,post,put,delete,patch inside api/views
Model           -> Created a Model User , which has two fields id and name.
Database        -> Used the default database db.sqlite3

urls
  Home Page ->  http://127.0.0.1:8000/
  View users -> http://127.0.0.1:8000/view
  Add users  -> http://127.0.0.1:8000/add/
  Delete users ->http://127.0.0.1:8000/delete/id
  Update users ->http://127.0.0.1:8000/update/id
  
DRF.postman_collection.json - it contains all the postman request in josn format.
