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

Go to your project directory, then clone this repo:
```
git clone https://github.com/rthotakura97/cumtd-python.git
```

## Usage

**This API attempts to present a clean interface to the CUMTD API, but in order to use it to its full potential, you must familiarize yourself with the official CUMTD API [documentation](https://developer.cumtd.com/).**

To use the CUMTD API, you need to first acquire an instant API key [here](https://developer.cumtd.com/).

With this API Key, declare an ```api``` object:
```
import cumtd
api = cumtd.ApiClient(<api-key>)
```

Now you can make calls using ```api``` to retrieve the necessary data.

## Methods

[get_calendar_dates_by_date](https://developer.cumtd.com/documentation/v2.2/method/getcalendardatesbydate/)

[get_calendar_dates_by_service](https://developer.cumtd.com/documentation/v2.2/method/getcalendardatesbyservice/)

[get_departures_by_stop](https://developer.cumtd.com/documentation/v2.2/method/getdeparturesbystop/)

[get_reroutes](https://developer.cumtd.com/documentation/v2.2/method/getreroutes/)

[get_reroutes_by_route](https://developer.cumtd.com/documentation/v2.2/method/getreroutesbyroute/)

[get_route](https://developer.cumtd.com/documentation/v2.2/method/getroute/)

[get_routes](https://developer.cumtd.com/documentation/v2.2/method/getroutes/)

[get_routes_by_stop](https://developer.cumtd.com/documentation/v2.2/method/getroutesbystop/)

[get_shape](https://developer.cumtd.com/documentation/v2.2/method/getshape/)

[get_shape_between_stops](https://developer.cumtd.com/documentation/v2.2/method/getshapebetweenstops/)

[get_stop](https://developer.cumtd.com/documentation/v2.2/method/getstop/)

[get_stops](https://developer.cumtd.com/documentation/v2.2/method/getstops/)

[get_stops_by_lat_lon](https://developer.cumtd.com/documentation/v2.2/method/getstopsbylatlon/)

[get_stops_by_search](https://developer.cumtd.com/documentation/v2.2/method/getstopsbysearch/)

[get_stop_times_by_trip](https://developer.cumtd.com/documentation/v2.2/method/getstoptimesbytrip/)

[get_stop_times_by_stop](https://developer.cumtd.com/documentation/v2.2/method/getstoptimesbystop/)

[get_planned_trips_by_lat_lon](https://developer.cumtd.com/documentation/v2.2/method/getplannedtripsbylatlon/)

[get_planned_trips_by_stops](https://developer.cumtd.com/documentation/v2.2/method/getplannedtripsbystops/)

[get_trip](https://developer.cumtd.com/documentation/v2.2/method/gettrip/)

[get_trips_by_block](https://developer.cumtd.com/documentation/v2.2/method/gettripsbyblock)

[get_trips_by_route](https://developer.cumtd.com/documentation/v2.2/method/gettripsbyroute)

[get_vehicle](https://developer.cumtd.com/documentation/v2.2/method/getvehicle)

[get_vehicles](https://developer.cumtd.com/documentation/v2.2/method/getvehicles)

[get_vehicles_by_route](https://developer.cumtd.com/documentation/v2.2/method/getvehiclesbyroute)

[get_news](https://developer.cumtd.com/documentation/v2.2/method/getnews)

[get_api_usage](https://developer.cumtd.com/documentation/v2.2/method/getapiusage)











