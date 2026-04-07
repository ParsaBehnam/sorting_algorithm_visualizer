import random
from visualizer import visualize_sort
from bubble_sort import bubble_sort
from merge_sort import merge_sort

def main():
    size = int(input("Enter array size: "))

    data = [random.randint(1, 100) for _ in range(size)]

    generator = merge_sort(data)

    visualize_sort(generator, data, title="Merge Sort")


if __name__ == "__main__":
    main()
