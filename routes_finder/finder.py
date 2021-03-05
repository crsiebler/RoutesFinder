import queue


class RoutesFinder:
    @staticmethod
    def sort_routes(paths: list):
        print(paths)
        pass

    @staticmethod
    def top_routes(paths: list[list], number: int):
        return RoutesFinder.sort_paths(paths)[:number]

    @staticmethod
    def uniform_cost_search(origin, destination):
        routes = []
        frontier = queue.PriorityQueue()
        frontier.put((0, origin, []))
        while not frontier.empty():
            cost, location, route = frontier.get()
            location.visited = True

            if location == destination:
                location.visited = False
                routes.append((route, cost))
            else:
                for edge in location.trips:
                    child = edge.destination
                    if not child.visited:
                        frontier.put(
                            (cost + edge.distance, child, route + [edge.route])
                        )

        return routes
