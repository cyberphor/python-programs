from argparse import ArgumentParser
from itertools import groupby

kounter = 0

def main(data):
    global kounter
    answer = ""
    groups = []
    for _, g in groupby(data, lambda x: x[0]): #  use the first item in each tuple as the grouping key
        groups.append(list(g))
    for g in groups:
        current_list = g
        current_value = g[0]
        counter = 0
        for i in current_list:
            counter = counter + 1
        foo = str(counter) + current_value
        answer = answer + foo
    kounter = kounter + 1
    if kounter == 50:
        print(len(answer))
        return
    main(answer)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--data")
    args = parser.parse_args()
    main(args.data)

"""
1 becomes 11
11 becomes 21
21 becomes 1211
1211 becomes 111221
111221 becomes 312211
"""