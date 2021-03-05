from typing import TypeVar, Generic
from geopy.distance import geodesic

Location = TypeVar("Location")


class Trip:
    """"""

    def __init__(self, locations: dict[str, Generic[Location]], data: dict) -> None:
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