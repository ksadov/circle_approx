import matplotlib.pyplot as plt
import numpy as np

def plot_polygon_circle(points, title, out_fname):
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.add_patch(plt.Polygon(points, fill=False, edgecolor='b'))

    circle = plt.Circle((0, 0), 1, fill=False, edgecolor='r')
    ax.add_patch(circle)
    
    plt.title(title)
    plt.xlim(-1.2, 1.2)
    plt.ylim(-1.2, 1.2)
    # save figure
    plt.savefig(out_fname)
    # close figure
    plt.close()
    