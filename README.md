# cumtd-python
An unofficial Python client for the [CUMTD REST API](https://developer.cumtd.com/). Skip making HTTP requests to the website endpoints and download this easy-to-use package instead!

**Disclaimer: This project and I have no association with CUMTD and its partners.**

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

Now available on PyPi!

Simply install the package with:
```
pip install cumtd-python
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

### Calendar 
 * [get_calendar_dates_by_date](https://developer.cumtd.com/documentation/v2.2/method/getcalendardatesbydate/)
```
api.get_calendar_dates_by_date('2017-05-06')
```

* [get_calendar_dates_by_service](https://developer.cumtd.com/documentation/v2.2/method/getcalendardatesbyservice/)
```
api.get_calendar_dates_by_service("1N SHOW")
```

### Departures
* [get_departures_by_stop](https://developer.cumtd.com/documentation/v2.2/method/getdeparturesbystop/)
```
api.get_departures_by_stop("it")
```

### Reroutes
* [get_reroutes](https://developer.cumtd.com/documentation/v2.2/method/getreroutes/)
```
api.get_reroutes()
```

* [get_reroutes_by_route](https://developer.cumtd.com/documentation/v2.2/method/getreroutesbyroute/)
```
api.get_reroutes_by_route("green")
```

### Routes
* [get_route](https://developer.cumtd.com/documentation/v2.2/method/getroute/)
```
api.get_route("teal")
```

* [get_routes](https://developer.cumtd.com/documentation/v2.2/method/getroutes/)
```
api.get_routes()
```

* [get_routes_by_stop](https://developer.cumtd.com/documentation/v2.2/method/getroutesbystop/)
```
api.get_routes_by_stop("it")
```

### Shapes
* [get_shape](https://developer.cumtd.com/documentation/v2.2/method/getshape/)
```
api.get_shape("7E NO EDGE")
```

* [get_shape_between_stops](https://developer.cumtd.com/documentation/v2.2/method/getshapebetweenstops/)
```
api.get_shape_between_stops("IT:1","WRTHLY:4","7E NO EDGE")
```

### Stops
* [get_stop](https://developer.cumtd.com/documentation/v2.2/method/getstop/)
```
api.get_stop("it")
```

* [get_stops](https://developer.cumtd.com/documentation/v2.2/method/getstops/)
```
api.get_stops()
```

* [get_stops_by_lat_lon](https://developer.cumtd.com/documentation/v2.2/method/getstopsbylatlon/)
```
api.get_stops_by_lat_lon("40.1133", "-88.226")
```

* [get_stops_by_search](https://developer.cumtd.com/documentation/v2.2/method/getstopsbysearch/)
```
api.get_stops_by_search("wright")
```

### Stop Times
* [get_stop_times_by_trip](https://developer.cumtd.com/documentation/v2.2/method/getstoptimesbytrip/)
```
api.get_stop_times_by_trip("[@14.0.51617008@][3][1275939436250]/12__O1")
```

* [get_stop_times_by_stop](https://developer.cumtd.com/documentation/v2.2/method/getstoptimesbystop/)
```
api.get_stop_times_by_stop("it")
```

### Planned Trips
* [get_planned_trips_by_lat_lon](https://developer.cumtd.com/documentation/v2.2/method/getplannedtripsbylatlon/)
```
api.get_planned_trips_by_lat_lon("40.12233", "-88.29619", "40.11626", "88.25783")
```

* [get_planned_trips_by_stops](https://developer.cumtd.com/documentation/v2.2/method/getplannedtripsbystops/)
```
api.get_planned_trips_by_stops("unipspct", "dncncltn")
```

### Trips
* [get_trip](https://developer.cumtd.com/documentation/v2.2/method/gettrip/)
```
api.get_trip("[@14.0.51617008@][3][1275939436250]/12__O1")
```

* [get_trips_by_block](https://developer.cumtd.com/documentation/v2.2/method/gettripsbyblock)
```
api.get_trips_by_block("O3")
```

* [get_trips_by_route](https://developer.cumtd.com/documentation/v2.2/method/gettripsbyroute)
```
api.get_trips_by_route("yellow")
```

### Vehicles
* [get_vehicle](https://developer.cumtd.com/documentation/v2.2/method/getvehicle)
```
api.get_vehicle("1352")
```

* [get_vehicles](https://developer.cumtd.com/documentation/v2.2/method/getvehicles)
```
api.get_vehicles()
```

* [get_vehicles_by_route](https://developer.cumtd.com/documentation/v2.2/method/getvehiclesbyroute)
```
api.get_vehicles_by_route("teal)
```

### Other
* [get_news](https://developer.cumtd.com/documentation/v2.2/method/getnews)
```
api.get_news()
```

* [get_api_usage](https://developer.cumtd.com/documentation/v2.2/method/getapiusage)
```
api.get_api_usage()
```











