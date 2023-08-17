from argparse import ArgumentParser
from math import sqrt
from matplotlib import pyplot

def get_perfect_square_roots(min: int, max: int) -> list:
    perfect_square_roots = []
    for x in range(min, (max + 1)):
        y = sqrt(x)
        if y.is_integer():
            perfect_square_roots.append({x:y})
    return perfect_square_roots

def visualize(points: list) -> None:
  for point in points:
    pyplot.scatter(x = point.keys(), y = point.values())
  pyplot.xlabel(xlabel = "Square Root")
  pyplot.ylabel(ylabel ="Value")
  pyplot.show()

def main(data):
    perfect_square_roots = get_perfect_square_roots(min = data.min, max = data.max)
    visualize(points = perfect_square_roots)

if __name__ == "__main__":
  parser = ArgumentParser()
  parser.add_argument("-m", "--min", dest = "min", type = int, required = True)
  parser.add_argument("-M", "--max", dest = "max", type = int, required = True)
  args = parser.parse_args()
  main(data = args)