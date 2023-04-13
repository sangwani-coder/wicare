# wicare
WiCare is a web and mobile application that aims to reduce poverty and improve the quality of life of families in poor communities by connecting them with individuals and organizations willing to provide Donation.

WiCare provides a platform for subscribers (nurses and teachers) in poor communities to create profiles of families in need and request Donation on their behalf.

Donors can browse profiles of families in need, read their stories, and make Donation directly through the platform. WiCare's mission is to provide a simple, efficient, and transparent way for subscribers and donors to help families in need and create a positive impact on their lives.

WiCare's ultimate goal is to reduce poverty and improve the well-being of communities in Zambia and beyond.

## Technologies

* *Django Rest* Backend(server side)
* *Vues.js* Frontend
* *postgres* Database
* *knox* Authentication


## API Endpoints

**Base URI**

If you get a resourse not found error, make sure that you got the base url correct.
It returns links to all the endpoints.

    `/wicare/api/`

### Base URL response

    $ curl http:localhost:8000/wicare/api/

    {
        "users": "http://localhost:8000/wicare/api/users/",
        "donees": "http://localhost:8000/wicare/api/donees/",
        "donations": "http://localhost:8000/wicare/api/donation/",
        "subscriber-profiles": "http://localhost:8000/wicare/api/donees/profile/"
    }

## WiCare Apps

|Application name | Description |
|------------------|------------|
| [*] [Accounts](./accounts/)| User Authentication|
| [*] [API](./api/)| Business logic |

## Team

- Peter Zyambo (Founder)
- Petrocelly Kafula (Co-Founder with experience in project management and fundraising)
- Sepiso Mukelabai (Co-Founder, Student Nurse, Community worker)