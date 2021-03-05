# RoutesFinder

A mini Python application to find all the routes in a graph and order them on distance. Each node in the graph is given a GPS coordinate. Utilize vincenty method of calculating the distance between the nodes. The edges in the graph are unidirectional. The output is formatted "\<origin>_\<destination>", e.g. BM_MON represents trip running directly from BM to MON.

The application is Dockerized using Python3.9.2-alpine. A Makefile is provided for easily building the image and running the container.

## Installation

Use our Makefile to assist building the application. Run the command below:

    sudo make build

## Testing

Unit tests compare the file output to expected results and provide assertions for each line. To run the tests, execute the command below:

    make test

## Execution

To run the package, execute the command below:

    make run