import matplotlib.pyplot as plt
import matplotlib.animation as animation

def visualize_sort(generator, arr, title='sorting_visualizer'):
    fig, ax = plt.subplots()
    ax.set_title(title)
    bar_rec = ax.bar(range(len(arr)), arr, align="edge")

    ax.set_xlim(0, len(arr))
    ax.set_ylim(0, max(arr) + 10)

    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
    iteration = [0]
    