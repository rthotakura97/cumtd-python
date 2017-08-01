# cumtd-python
An unofficial Python client for the CUMTD REST API. Skip making HTTP requests to the website endpoints and download this easy-to-use package instead!

## Installation

Package will be available on ```pip``` soon.

* Requirements
  * Python "json" library
  * Python "requests" library

1) Go to your project directory, then clone this repo:

```
git clone https://github.com/rthotakura97/cumtd-python.git
```

2) In your project, add ```import cumtd```

##Usage

To use the CUMTD API, you need to first acquire an instant API key at https://developer.cumtd.com/

With this API Key, declare an ```api``` object:
```
api = cumtd.ApiClient(<api-key>)
```

Now you can make calls using ```api``` to retrieve the necessary data.




