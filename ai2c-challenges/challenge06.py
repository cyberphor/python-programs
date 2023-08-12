from argparse import ArgumentParser

def main(range_to_print):
    for n in range(1, (range_to_print + 1)):
        if n/3:
            print(n)

if "__main__" == __name__:
    parser = ArgumentParser()
    parser.add_argument("-r", "--range-to-print", type = int, dest = "range_to_print", required = True)
    args = parser.parse_args()
    main(args.range_to_print)