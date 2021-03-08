import csv
import logging
from typing import Tuple
from .finder import RoutesFinder
from .location import Location
from .trip import Trip


def output(count: int, route: Tuple[list, float]) -> str:
    """Format the route display."""
    return f"Option {count}: {', '.join(route[0])}\n"


def write_to_file(filename: str, routes: list[Tuple[list, float]]) -> None:
    """Write routes to the file as "Option <X>": <Route>"""
    with open(filename, "w") as file:
        [file.write(output(x + 1, route)) for x, route in enumerate(routes)]


def coalesce_routes(
    routes: list[Tuple[list, float]], max: int
) -> list[Tuple[list, float]]:
    """Coalesce routes list with "N/A" if number requested exceeds actual."""
    size = len(routes)
    # Check if the size of the list is enough for requested max
    if size < max:
        # Append a dummy value to end of list to meet max
        [routes.append((["N/A"], 0)) for _ in range(max - size)]

    return routes[:max]


def parse(
    locations_file: str,
    trips_file: str,
    input_file: str,
    output_file: str,
    results: int,
) -> None:
    """Read CSV files and instruction file to build the graph and traverse."""
    origin = None
    destination = None
    locations = {}

    # Read the CSV file containing the locations (i.e. nodes/vertices)
    with open(locations_file, "r") as data:
        reader = csv.DictReader(data)
        for row in reader:
            location = Location(row)
            locations[location.code] = location

    # Read the CSV file containing the trips (i.e. edges)
    with open(trips_file, "r") as data:
        reader = csv.DictReader(data)
        for row in reader:
            # Ensure the locations are known before adding to the graph
            if row["Origin"] in locations and row["Destination"] in locations:
                locations.get(row["Origin"]).add_trip(Trip(locations, row))
            else:
                # One of the locations for the trip could not be determined
                logging.info(f"Trip Not Added: {row['Route']}")

    # Read the input file to determine origin & destination
    with open(input_file, "r") as input:
        origin = locations.get(input.readline().split(":")[1].strip())
        destination = locations.get(input.readline().split(":")[1].strip())

    routes = RoutesFinder.uniform_cost_search(origin, destination)

    write_to_file(output_file, coalesce_routes(routes, results))
