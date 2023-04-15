# Accounts app
The accounts app defines endpoints for user authentication.

## Base URI

If you get a resourse not found error, make sure that you got the base url correct.

    `/api/`

### Example Requests

### Registration

`POST /api/auth/register/`

This endpoint allows users to register for a WiCare account. The request should include the user's `username`, `email`, and `password`. If successful, the response will include the registered user's information and an authentication token.

**Example Request**


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

### Login

`POST /api/auth/login/`

This endpoint allows users to login to their WiCare account. The request should include the user's `email` and `password`. If successful, the response will include the authenticated user's information and an authentication token.

**Example Request**

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

**Response Codes**
    
    * 200 OK

### Logout

`POST /api/auth/logout/`

This endpoint allows users to logout of their WiCare account. The request should include the user's authentication token. 

* **Example request**

**Request Headers**

    'Authorization: Token 7671fcda7591a3ca307438374cc86f56d8c86ab5d5b7204b6f50123b9c1e98e'

**Response Codes**
    
    * 204 No Content(user has been logged out successfully)

### Logout All

`POST wicare//api/auth/logoutall/`

This endpoint allows users to logout of all their active WiCare sessions. The request should include the user's authentication token.