# cumtd-python
An unofficial Python client for the [CUMTD REST API](https://developer.cumtd.com/). Skip making HTTP requests to the website endpoints and download this easy-to-use package instead!

## Benefits
 * A simple to use Python wrapper for public CUMTD API endpoints.
 * In less than 10 minutes, you can start pulling CUMTD data such as routes, timings, stop information and more.
 * You don't have to worry about handling the nuances of the official API --> easy to use methods for every endpoint
 
## Development
 * This package is tested with private and public tests, but may still have some bugs.
 * Implementation of methods with "optional" parameters coming soon (look at [CUMTD API](https://developer.cumtd.com/) for details).
 * If you encounter any bugs or problems, submit an "Issue" to this repository and I will fix it as soon as possible.
 * Any open-source contribution is appreciated!

## Getting Started

Package will be available on ```pip``` soon.

* Requirements
  * Python "json" library
  * Python "requests" library

1) Go to your project directory, then clone this repo:

```
git clone https://github.com/rthotakura97/cumtd-python.git
```

2) In your project, add ```import cumtd```

## Usage

**This API attempts to present a clean interface to the CUMTD API, but in order to use it to its full potential, you must familiarize yourself with the official CUMTD API [documentation](https://developer.cumtd.com/).**

To use the CUMTD API, you need to first acquire an instant API key [here](https://developer.cumtd.com/).

With this API Key, declare an ```api``` object:
```
api = cumtd.ApiClient(<api-key>)
```

Now you can make calls using ```api``` to retrieve the necessary data.

## Methods








