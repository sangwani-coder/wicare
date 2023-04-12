# WiCare API

The WiCare API is a RESTful API that enables communication between the WiCare web and mobile applications and the backend server. It is built using Django Rest Framework and allows users to access data related to poverty in Zambia, as well as donate to poor communities through nurses and teachers in those communities.

## Endpoints
The following endpoints are available in the WiCare API:

### Base URI

If you get a resourse not found error, make sure that you got the base url correct.

    `/wicare/api/`

### Subscribers
Allows users to view and update their WiCare account information

* **GET, POST** `wicare/api/subscribers/`
* **PUT, DELETE** `wicare/api/subscribers/<int:id>/`
  
## Donees
Allows users to view and add Donnes to the WiCare platform.

* **GET, POST** `wicare/api/donees/`
* **PUT, DELETE** `wicare/api/donees/<int:id>/`
* **GET, POST** `wicare/api/communities/` Allows users to view information about poor communities in Zambia

## Donations
Allows users to view and make donations to poor communities through nurses and teachers in those communities

* **GET, POST** `wicare/api/donations`

## Authentication
The WiCare API uses token-based authentication with the Knox library. To access protected endpoints, users must include a valid access token in the request headers.

## Rate Limiting
To prevent abuse and ensure fair usage of the API, rate limiting is implemented on certain endpoints. For example, the donation endpoint is limited to a maximum of 10 donations per user per day.

## Error Handling
The WiCare API handles errors using standard HTTP status codes and returns detailed error messages in JSON format. In addition, custom exceptions are raised for certain error cases, such as when a user attempts to donate to a community that has already reached its donation goal.

## Versioning
The WiCare API is currently on version 1.0. Future versions may include additional endpoints and functionality, but changes to the API will be communicated to users to ensure a smooth transition.