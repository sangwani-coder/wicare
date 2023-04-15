# wicare
WiCare is a web and mobile application that aims to reduce poverty and improve the quality of life of families in poor communities by connecting them with individuals and organizations willing to provide Donation.

WiCare provides a platform for subscribers (nurses and teachers) in poor communities to create profiles of families in need and request Donation on their behalf.

Donors can browse profiles of families in need, read their stories, and make Donation directly through the platform. WiCare's mission is to provide a simple, efficient, and transparent way for subscribers and donors to help families in need and create a positive impact on their lives.

WiCare's ultimate goal is to reduce poverty and improve the well-being of communities in Zambia and beyond.

## Technologies

* *Django-Rest-Framework* Backend
* *Vues.js* Frontend
* *postgres* Database
* *knox* Token based Authentication


## API Endpoints

**Base URI**

If you get a resourse not found error, make sure that you got the base url correct.
It returns links to all the endpoints.

    `/api/`

### Base URL response

    $ curl http:localhost:8000/api/

    {
        "users": "http://localhost:8000/api/users/",
        "donees": "http://localhost:8000/api/donees/",
        "donations": "http://localhost:8000/api/donations/",
        "register-user": "http://localhost:8000/api/auth/register/",
        "login-user": "http://localhost:8000/api/auth/login/",
        "logout-user": "http://localhost:8000/api/auth/logout/",
        "logoutall-user": "http://localhost:8000/api/auth/logoutall/"
    }

## WiCare Apps

|Applications | Description |
|------------------|------------|
| [*] [accounts](./accounts/)| Handles User authentication(registration, login and logout)|
| [*] [api](./api/)| Handles the business logic of the site |