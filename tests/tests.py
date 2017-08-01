import cumtd

client = cumtd.ApiClient(<api-key>)

a = client.get_calendar_dates_by_date('2017-05-06')
assert type(a) is dict

a = client.get_calendar_dates_by_service("1N SHOW")
assert type(a) is dict

a = client.get_departures_by_stop("it:1")
assert type(a) is dict

a = client.get_news()
assert type(a) is dict

a = client.get_reroutes()
assert type(a) is dict

a = client.get_reroutes_by_route("gold")
assert type(a) is dict

a = client.get_route("green")
assert type(a) is dict

a = client.get_routes()
assert type(a) is dict

a = client.get_routes_by_stop("it:1")
assert type(a) is dict

a = client.get_shape("7E NO EDGE")
assert type(a) is dict

a = client.get_shape_between_stops("it:1", "wrthly:4", "4w")
assert type(a) is dict

a = client.get_stop("it")
assert type(a) is dict

a = client.get_stops()
assert type(a) is dict

a = client.get_stops_by_lat_lon("40.1133", "-88.226", "3")
assert type(a) is dict

a = client.get_stops_by_search("green")
assert type(a) is dict

a = client.get_trip("[@14.0.51617008@][3][1275939436250]/12__O1")
assert type(a) is dict

a = client.get_trips_by_block("O3")
assert type(a) is dict

a = client.get_trips_by_route("green")
assert type(a) is dict

a = client.get_vehicle("1352")
assert type(a) is dict

a = client.get_vehicles()
assert type(a) is dict

a = client.get_vehicles_by_route("teal")
assert type(a) is dict

