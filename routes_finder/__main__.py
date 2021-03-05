from .parser import parse

LOCATIONS_FILE = "data/locations.csv"
TRIPS_FILE = "data/trips.csv"


def main():
    parse(LOCATIONS_FILE, TRIPS_FILE, "tests/input/input4.txt")


if __name__ == "__main__":
    main()
