import os
import sys
import getopt
import logging
from .parser import parse


def usage():
    """Help documentation."""
    print(
        f"\nusage: routes_finder [-v] [-h] [--verbose] [--help] "
        f"[--input=<Input-File>] [--output=<Output-File>] "
        f"[--locations=<Locations-File>] [--trips=<Trip-File>] "
        f"[--results=<Results-Max-Count>]\n"
        f"\nOptions:\n"
        f"\t-v, --verbose\t\tVerbose\n"
        f"\t-h, --help\t\tHelp\n"
        f"\t--input\t\t\tFilename\n"
        f"\t--output\t\tFilename\n"
        f"\t--locations\t\tCSV File\n"
        f"\t--trips\t\t\tCSV File\n"
        f"\t--results\t\tInteger\n"
        f"\nArguments:\n"
        f"\tInput-File: Text file containing the origin & destination input (Default: tests/input/input1.txt).\n"
        f"\tOutput-File: Filename and path where to output the results (Default: tests/output/output1.txt).\n"
        f"\tLocations-File: CSV file storing the locations data (Default: data/locations.csv).\n"
        f"\tTrips-File: CSV file storing the trips data (Default: data/trips.csv).\n"
        f"\tResults-Max-Count: Maximum count of results to output (Default: 3).\n"
    )


def main():
    """Find all routes between two nodes in a unidirectional graph."""
    # Check the user CLI input matches correct syntax
    try:
        # Specify the valid CLI options/arguments
        opts, _ = getopt.getopt(
            sys.argv[1:],
            "hv",
            [
                "help",
                "verbose",
                "input=",
                "output=",
                "locations=",
                "trips=",
                "results=",
            ],
        )
    except getopt.GetoptError as err:
        print(str(err))
        usage()
        sys.exit(2)

    # Define input arguments and initialize default values.
    input_file = "tests/input/input1.txt"
    output_file = "tests/output/output1.txt"
    locations_file = "data/locations.csv"
    trips_file = "data/trips.csv"
    results = 3

    # Loop through all the User CLI options/arguments
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt in ("-v", "--verbose"):
            logging.basicConfig()
            logging.getLogger().setLevel(logging.DEBUG)
        elif opt == "--input":
            input_file = arg

            if not os.path.exists(input_file):
                sys.exit("Could not find input file")
        elif opt == "--output":
            output_file = arg
        elif opt == "--locations":
            locations_file = arg

            if not os.path.exists(locations_file):
                sys.exit("Could not find locations file")
        elif opt == "--trips":
            trips_file = arg

            if not os.path.exists(trips_file):
                sys.exit("Could not find trips file")
        elif opt == "--results":
            results = int(arg)

    parse(
        locations_file,
        trips_file,
        input_file,
        output_file,
        results,
    )


if __name__ == "__main__":
    main()
