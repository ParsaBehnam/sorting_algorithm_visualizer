import random
from visualizer import visualize_sort
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort

def main():
    size = int(input("Enter array size: "))
    data = [random.randint(1, 100) for _ in range(size)]
    choice = int(input("1- Bubble Sort\n2- Insertion Sort\n3- Merge Sort\nChoose sorting algorithm: "))

    match choice:
        case 1:
            visualize_sort(bubble_sort(data), data, title = "Bubble Sort")
        case 2:
            visualize_sort(insertion_sort(data), data, title ="Insertion Sort")
        case 3:
            visualize_sort(merge_sort(data), data, title = "Merge Sort")
        case _:
            print("invalid option. Please try again.")


if __name__ == "__main__":
    main()
