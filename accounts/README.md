# accounts app
The accounts app defines endpoints for user authentication.

### Examples

**REGISTER**
endpoint that registers a user.

* POST: /wicare/api/auth/register/

**Body (json)**

    {
    "username":"pita",
    "password":"password123"
    }

**Example Reponse**

    {
    "user": {
        "id": 2,
        "username": "pita",
        "email": "pita@bot.com"
    },
    "token": "2cc83e0073251de579f35e1050ce25ad57316b60f7862be1c92c77510b7e13da"
    }

**Response Codes**
    
    * 200 OK
    * 

**LOGIN**
endpoint that logins in a user.

* POST: /wicare/api/auth/login/

**Body (json)**

    {
        "username":"pita",
        "password":"password123"
    }

**Example Response**

    {
    "expiry": "2023-04-12T06:09:09.829531Z",
    "token": "7671fcda7591a3ca307438374cc86f56d8c86ab5d5b7204b6f50123b9c1e98e8"
    }

`token`: Used in request headers to access protected views.

**Response Codes**
    
    * 200 OK

**LOGOUT**

endpoint that logs out an authenticated user.

* POST: /wicare/api/auth/logout/

**Request Headers**

    'Authorization: Token 7671fcda7591a3ca307438374cc86f56d8c86ab5d5b7204b6f50123b9c1e98e'

**Response Codes**
    
    * 204 No Conent(user has been logged out successfully)

