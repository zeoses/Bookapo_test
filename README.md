#  bokato test
## To get started:
1 - Clone the repository
`git clone git@github.com:zeoses/Bookapo_test.git`  
2 - Create virtual environment
`python3.x -m venv .venv`
and then activate it
`source .venv/bin/activate`
3 -  go to solaris directory `cd bookapo`  
4 - if in developer mode Install requirement-dev packages else
`pip install -r requirements.txt`

5 - Run `python manage.py migrate`.

6 - Create a superuser
`python manage.py createsuperuser`

7 - Run server `python manage.py runserver` and open `localhost:8000` in your browser.  

8 - loging from `http://127.0.0.1:8000/admin/` and add user to profile
9 - go to `http://127.0.0.1:8000/redoc/` and see project document
## for test
### login

```
curl \       
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"username": "your_user_name", "password": "your_password"}' \
  http://localhost:8000/api/token/

```
### get profile detail (note : Do step 7 first and then apply )
```
curl -X GET \
  http://127.0.0.1:8000/profile/ \
  -H 'authorization: Bearer "your_access_token" \
  -H 'cache-control: no-cache' \
  -H 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
```
