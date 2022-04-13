# Django_Project
Created basic CRUD operations with django rest framework <br />

Packages Used <br />
  *django               - version =4.0.3   (pip install Django)<br />
  *djangorestframework  - version =3.13.1  (pip install djangorestframework) <br />
  *django-cors-headers  - version =3.11.0  (pip install django-cors-headers) <br />

Added ('rest_framework','api.apps.ApiConfig') inside installed_apps in settings.py<br />
Added (api.middleware.CustomMiddleware) inside middleware in settings.py<br />

created apps    -> "api"<br />
Middleware used -> CustomMiddleware , Not added any functionality just added print statements to check the working of that middleware.<br />
Http methods    -> Used some http methods like get,post,put,delete,patch inside api/views<br />
Model           -> Created a Model User , which has two fields id and name.<br />
Database        -> Used the default database db.sqlite3<br />

urls<br />
  Home Page ->  http://127.0.0.1:8000/ <br />
  View users -> http://127.0.0.1:8000/view <br />
  Add users  -> http://127.0.0.1:8000/add/ <br />
  Delete users ->http://127.0.0.1:8000/delete/id <br />
  Update users ->http://127.0.0.1:8000/update/id <br />
<br />
DRF.postman_collection.json - it contains all the postman request in json format.
