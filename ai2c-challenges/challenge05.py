from argparse import ArgumentParser

def main(string_to_reverse):
    """
    Reverses the order of the string given.
    """
    reversed_string = []
    length_of_string_to_reverse = len(string_to_reverse) - 1 # subtract 1 to account for zero-based numbering
    for c in string_to_reverse:
        reversed_string.append(string_to_reverse[length_of_string_to_reverse])
        length_of_string_to_reverse = length_of_string_to_reverse -1
    print("".join(reversed_string))

if "__main__" == __name__:
    parser = ArgumentParser()
    parser.add_argument("-s", type = str, dest = "string_to_reverse", required = True)
    args = parser.parse_args()
    main(args.string_to_reverse)