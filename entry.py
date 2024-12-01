import sys

if __name__ == "__main__":
    if sys.argv[1] == "run":
        year, day = sys.argv[2], sys.argv[3]
        print("Running: %s %s" % (year, day))

    else:
        raise Exception(f"Invalid command: {sys.argv[1]}")
