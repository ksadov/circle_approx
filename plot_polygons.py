import argparse
import numpy as np

from utils import plot_polygon_circle

def generate_polygon_points(n):
    points = []
    for i in range(n):
        x = np.cos(2 * np.pi * i / n)
        y = np.sin(2 * np.pi * i / n)
        points.append((x, y))
    return points

def plot_polygon_up_to_n(n):
    for i in range(3, n+1):
        points = generate_polygon_points(i)
        fname = 'polygon_{}.png'.format(i)
        title = 'Regular Polygon with {} sides'.format(i)
        plot_polygon_circle(points, title, fname)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('n', type=int)
    args = parser.parse_args()
    plot_polygon_up_to_n(args.n)

if __name__ == '__main__':
    main()