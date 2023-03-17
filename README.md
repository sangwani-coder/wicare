# wicare
Web application where subscribers register destitute people on the platform and raise donations on their behalf.

## Technologies

* *Django Rest* Backend(server side)
* *Vues.js* Frontend
* *postgres* Database


## API Endpoints

**Base URI**

If you get a resourse not found error, make sure that you got the base url correct.

    http://localhost:8000/wicare/api/


**Donations**
The endpoint that adds and lists a donation.

    url: http://localhost:8000/wicare/api/donations

* Create
* List

### example query

    GET /wicare/api/donations/donations/1

### example response

    {
        "created": "2023-03-15T23:25:08.755951Z",
        "sponsor": "Peter Zyambo",
        "amount": 50,
        "donate_to": "Education",
        "mobile": "0977604012",
        "email": "zyambo@icloud.com",
        "url": "http://localhost:8000/wicare/api/donations/donations/1/"
    }

**Health**
The endpoint that adds, lists, updates, and deletes a health related case.

    url: http://localhost:8000/wicare/api/health

* Create
* Delete
* List
* Update

**Education**
The endpoint that adds, lists, updates, and deletes an education related case.

    url: http://localhost:8000/wicare/api/education

* Create
* Delete
* List
* Update


**Subscribers**
The endpoint that adds, lists, updates, and deletes a subscriber.

    url: http://localhost:8000/wicare/api/subscribers

* Create
* List
* Update
* Delete

**Users**

    url: http://localhost:8000/wicare/api/users
    
* List
