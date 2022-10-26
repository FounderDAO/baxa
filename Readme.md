
Url:http://127.0.0.1:8000/
Method: GET
HTTP 200 OK
Allow: OPTIONS, GET
Content-Type: application/json
Vary: Accept
Responce:
"Welcome Service Backend!"



Url:http://127.0.0.1:8000/auth/
Method:GET
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept
Responce:
{
    "users": "http://127.0.0.1:8000/auth/users/"
}


Url:http://127.0.0.1:8000/auth/login/
Method: POST
Required: {
    "username": "",
    "password": ""
}


Url:http://127.0.0.1:8000/auth/logout/
Method: POST
responce:
'''Logged out
Thanks for spending some quality time with the web site today.
Log in again'''


Url: http://127.0.0.1:8000/auth/users/
Method: GET
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept
Responce:
    {
        "email": "",
        "id": ,
        "username": ""
    }


Url: http://127.0.0.1:8000/auth/users/
Method: POST
Required: {
    "username": "",
    "email": "",
    "password": ""
}

Url: http://127.0.0.1:8000/api/token/
Method: POST
Required: {
    "username": "",
    "password": ""
}


Url:http://127.0.0.1:8000/api/token/refresh/
Method:POST
Required: {
    "refresh": "",
}
