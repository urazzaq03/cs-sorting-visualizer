import matplotlib.pyplot as plt
import random


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                yield arr


def visualize_sort(arr):
    plt.ion()
    fig, ax = plt.subplots()
    bars = ax.bar(range(len(arr)), arr)
    ax.set_title('Bubble Sort Visualization')
    for updated in bubble_sort(arr):
        for bar, val in zip(bars, updated):
            bar.set_height(val)
        plt.pause(0.1)
    plt.ioff()
    plt.show()


if __name__ == "__main__":
    arr = [random.randint(1, 100) for _ in range(20)]
    visualize_sort(arr)
