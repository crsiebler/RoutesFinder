import geopy
from typing import Hashable, TypeVar, Generic

Trip = TypeVar("Trip")


class Location:
    """The Node/Vertex of the graph.

    Contains an adjacency list stored in the `trips` attribute used to build the
    adjacency graph. Also has a `visited` attribute used in the search to avoid
    cycles.
    """

    def __init__(self, data: dict) -> None:
        self.code = data["LocationCode"]
        self.point = geopy.Point(data["Latitude"], data["Longitude"])
        self.facility_owned = bool(data["FacilityOwnedByCarvana"])
        self.trips = []
        self.visited = False

    def __hash__(self) -> Hashable:
        return hash(self.code)

    def __repr__(self) -> str:
        return (
            f"Location(Code:{self.code},Coordinate:{self.point},"
            f"FacilityOwned:{self.facility_owned})"
        )

    def __str__(self) -> str:
        return (
            f"Location: {self.code}\n"
            f"\tCoordinate: {self.point}\n"
            f"\tFacilityOwned: {self.facility_owned}"
        )

    def __eq__(self, other: object) -> bool:
        if isinstance(other, str):
            return self.code is other
        elif not isinstance(other, Location):
            return NotImplemented
        return self.code is other.code

    def add_trip(self, trip: Trip) -> list[Generic[Trip]]:
        self.trips.append(trip)
        return self.trips