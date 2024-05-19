import numpy as np
import argparse

from utils import plot_polygon_circle


def point_on_circle(point):
    return np.linalg.norm(point) - 1 < 1e-6

def flip_corner(point):
    new_points = []
    x, y = point
    # find the closest point on the circle
    r = np.linalg.norm(point)
    x_c = x / r
    y_c = y / r
    if x * y > 0:
        new_points.append((x_c, y))
        new_points.append((x_c, y_c))
        new_points.append((x, y_c))
    else:
        new_points.append((x, y_c))
        new_points.append((x_c, y_c))
        new_points.append((x_c, y))
    return new_points
    
def make_new_points(point_list):
    new_point_list = []
    for point in point_list:
        if point_on_circle(point):
            new_point_list.append(point)
        else:
            new_points = flip_corner(point)
            new_point_list.extend(new_points)
    return new_point_list
          
def plot_up_to_depth(n):
    fname = 'rad_4_circle_depth_{}.png'.format(n)
    title = 'Jagged \"Circle\" Depth {}'.format(n)
    if n==0:
        points = [(-1, -1), (-1, 1), (1, 1), (1, -1)]
    else:
        points = make_new_points(plot_up_to_depth(n-1))
    plot_polygon_circle(points, title, fname)
    return points

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('depth', type=int)
    args = parser.parse_args()
    plot_up_to_depth(args.depth)

if __name__ == '__main__':
    main()