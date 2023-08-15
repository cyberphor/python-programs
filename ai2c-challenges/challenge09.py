from argparse import ArgumentParser
from time import time_ns

def get_floor(filepath: str) -> str:
    with open(filepath, "r") as filename:
        instructions = filename.readline()
        return instructions.count("^") - instructions.count("v")

def main(filepath: str) -> None:
    start_time = time_ns()
    answer = get_floor(filepath)
    end_time = time_ns()
    total_time = end_time - start_time
    print(f"Go to floor {answer}.")
    print(f"This took {total_time} nanoseconds.")

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-f", required = True)
    args = parser.parse_args()
    main(filepath = args.f)