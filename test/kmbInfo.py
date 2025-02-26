import requests

#send get to server and search "data"s info
def get_json(url):
    return requests.get(url).json().get("data", [])

def display_route_info(route):
    stops = get_json(f"https://data.etabus.gov.hk/v1/transport/kmb/route-stop/{route}/inbound/1")
    print(f"Route {route} Information:")
    # loop index,get station id then check the json
    for index, stop in enumerate(stops):
        stop_id = stop.get("stop")
        stop_name = get_json(f"https://data.etabus.gov.hk/v1/transport/kmb/stop/{stop_id}").get("name_tc", "Unknown")
        print(f"ID: {str(index).zfill(2)} Name: {stop_name} Stop ID: {stop_id}")

route = input("Input a route: ").strip()
display_route_info(route)