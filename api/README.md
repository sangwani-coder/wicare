# WiCare API

The WiCare API is a RESTful API that enables communication between the WiCare web and mobile applications and the backend server. It is built using Django Rest Framework and allows users to access data related to poverty in Zambia, as well as donate to poor communities through nurses and teachers in those communities.

## Endpoints
The following endpoints are available in the WiCare API:

### Base URI

If you get a resourse not found error, make sure that you got the base url correct.

    `/api/`

### Subscribers
Allows users to view and update their WiCare account information

* **GET, POST** `/api/subscribers/`
* **PUT, DELETE** `/api/subscribers/<int:id>/`
  
## Donees
Allows users to view and add Donnes to the WiCare platform.

* **GET, POST** `/api/donees/`
* **PUT, DELETE** `/api/donees/<int:id>/`
* **GET, POST** `/api/communities/` Allows users to view information about poor communities in Zambia

## Donation
Allows users to view and make Donation to poor communities through nurses and teachers in those communities

* **GET, POST** `/api/Donation`

## Authentication
The WiCare API uses token-based authentication with the Knox library. To access protected endpoints, users must include a valid access token in the request headers.

    {"Authorization": "Token 7671fcda7591a3ca307438374cc86f56d8c86ab5d5b7204b6f50123b9c1e98e8"}

## Rate Limiting
To prevent abuse and ensure fair usage of the API, rate limiting is implemented on certain endpoints. For example, the donation endpoint is limited to a maximum of 10 Donation per user per day.

## Error Handling
The WiCare API handles errors using standard HTTP status codes and returns detailed error messages in JSON format. In addition, custom exceptions are raised for certain error cases, such as when a user attempts to donate to a community that has already reached its donation goal.

## Versioning
The WiCare API is currently on version 1.0. Future versions may include additional endpoints and functionality, but changes to the API will be communicated to users to ensure a smooth transition.

## Users
The first user in the users table is a superuser that will be a default Donee if a donor
decides to make a general donation.