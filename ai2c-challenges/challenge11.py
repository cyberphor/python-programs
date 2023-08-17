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

def get_triangle_numbers(min: int, max: int) -> list:
    triangle_numbers = []
    for x in range(min, (max + 1)):
      y = (x + (x**2)) / 2
      triangle_numbers.append({y:x})
    return triangle_numbers 
      
def update_visualization(visualization: pyplot, points: list, color: str) -> pyplot:
    for point in points:
        visualization.scatter(x = point.keys(), y = point.values(), c = color)
    return visualization

def main(data):
    v = pyplot
    perfect_square_roots = get_perfect_square_roots(min = data.min, max = data.max)
    triangle_numbers = get_triangle_numbers(min = 1, max = 10)
    v = update_visualization(visualization = v, points = perfect_square_roots, color = "red")
    v = update_visualization(visualization = v, points = triangle_numbers, color = "blue")
    v.title("Challenge 11")
    v.xlabel("Values")
    v.ylabel("Squares/Triangles")
    v.show()

if __name__ == "__main__":
  parser = ArgumentParser()
  parser.add_argument("-m", "--min", dest = "min", type = int, required = True)
  parser.add_argument("-M", "--max", dest = "max", type = int, required = True)
  args = parser.parse_args()
  main(data = args)