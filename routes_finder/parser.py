import csv
from typing import Tuple
from .finder import RoutesFinder
from .location import Location
from .trip import Trip


def output(count: int, route: Tuple[list, float]) -> str:
    """"""
    return f"Option {count}: {', '.join(route[0])}\n"


def write_to_file(filename: str, routes: list[Tuple[list, float]]) -> None:
    """"""
    with open(filename, "w") as file:
        [file.write(output(x, route)) for x, route in enumerate(routes)]


def coalesce_routes(
    routes: list[Tuple[list, float]], max: int
) -> list[Tuple[list, float]]:
    """"""
    size = len(routes)
    if size < max:
        [routes.append((["N/A"], 0)) for _ in range(max - size)]

    return routes[:max]


def parse(locations_file: str, trips_file: str, input_file: str) -> None:
    """"""
    origin = None
    destination = None
    locations = {}

    with open(locations_file, "r") as data:
        reader = csv.DictReader(data)
        for row in reader:
            location = Location(row)
            locations[location.code] = location

    with open(trips_file, "r") as data:
        reader = csv.DictReader(data)
        for row in reader:
            # Ensure the locations are known before adding to the graph
            if row["Origin"] in locations and row["Destination"] in locations:
                locations.get(row["Origin"]).add_trip(Trip(locations, row))
            else:
                print(f"Trip Not Added: {row['Route']}")

    with open(input_file, "r") as input:
        origin = locations.get(input.readline().split(":")[1].strip())
        destination = locations.get(input.readline().split(":")[1].strip())

    routes = RoutesFinder.uniform_cost_search(origin, destination)

    write_to_file("output4.txt", coalesce_routes(routes, 3))
