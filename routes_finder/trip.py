from typing import TypeVar, Dict
from geopy.distance import geodesic

Location = TypeVar("Location")


class Trip:
    """The Edge of the graph.

    Holds the distance attribute representing the Kilometers between the origin
    and destination GPS coordinates. The vincenty method was removed from the
    geopy package, so I utilized geodesic method which I believe has the same
    algorithm to determine distance.

    Weekly capacity is not used but the Priority Queue in the uniform cost
    search could use that attribute instead.
    """

    def __init__(self, locations: Dict[str, Location], data: dict) -> None:
        self.route = data["Route"]
        self.origin = locations.get(data["Origin"])
        self.destination = locations.get(data["Destination"])
        self.weekly_capacity = data["WeeklyCapacity"]
        self.distance = geodesic(self.origin.point, self.destination.point).km

    def __repr__(self) -> str:
        return (
            f"Trip(Route:{self.route},Origin:{self.origin},Destination:"
            f"{self.destination},WeeklyCapacity:{self.weekly_capacity}"
        )

    def __str__(self) -> str:
        return (
            f"Trip: {self.route}\n"
            f"\tOrigin: {self.origin}\n"
            f"\tDestination: {self.destination}\n"
            f"\tWeeklyCapacity: {self.weekly_capacity}"
        )

    def __eq__(self, other: object) -> bool:
        if isinstance(other, str):
            return self.route is other
        elif not isinstance(other, Trip):
            return NotImplemented
        return self.route is other.route
