import queue
from typing import Tuple, TypeVar

Location = TypeVar("Location")


class RoutesFinder:
    @staticmethod
    def uniform_cost_search(
        origin: Location, destination: Location
    ) -> list[Tuple[list, int]]:
        """"""
        routes = []
        frontier = queue.PriorityQueue()  # Declare a Priority Queue
        frontier.put((0, origin, []))  # Initialize the Queue
        # Loop until all connected nodes are visited and all paths found
        while not frontier.empty():
            cost, location, route = frontier.get()  # Get the highest priority node
            location.visited = True  # Mark node a visisted

            # Check if the goal is reached
            if location == destination:
                # Mark node as not visisted so the search for more paths may continue
                location.visited = False
                routes.append((route, cost))  # Path found so add it to list
            else:
                # Loop through the adjacency list of all edges for the current node
                for trip in location.trips:
                    # Make sure a previous iteration has not visited this node
                    if not trip.destination.visited:
                        # New frontier found in graph so add to queue
                        frontier.put(
                            (
                                cost + trip.distance,
                                trip.destination,
                                route + [trip.route],
                            )
                        )

        return routes
