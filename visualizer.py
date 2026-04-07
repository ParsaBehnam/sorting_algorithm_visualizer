import matplotlib
matplotlib.use("QtAgg")
import matplotlib.pyplot as plt
import matplotlib.animation as animation

plt.style.use("dark_background")

def visualize_sort(generator, arr, title='sorting_visualizer'):
    fig, ax = plt.subplots()
    ax.set_title(f"{title}", fontsize=16, color="white")
    bar_rec = ax.bar(range(len(arr)), arr, width=0.8, align="edge", edgecolor="none")

    ax.set_xlim(0, len(arr))
    ax.set_ylim(0, max(arr) + 10)
    ax.set_xticks([])
    ax.set_yticks([])

    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
    iteration = [0]

    def update_plot(arr):
        for rect, val in zip(bar_rec, arr):
            rect.set_height(val)
            rect.set_color("#4CC9F0")
        iteration[0] += 1
        text.set_text(f"Number Of Operations: {iteration[0]}")

    anim = animation.FuncAnimation(
        fig,
        update_plot,
        frames=generator,
        repeat=False,
        interval=20,
        cache_frame_data=False
    )

    plt.show()