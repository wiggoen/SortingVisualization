import timeit
import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def bubble_sort(sort_list):
  n = len(sort_list)
  swapped = True
  while swapped:
    swapped = False
    for i in range(n-1):
      if sort_list[i] > sort_list[i+1]:
        sort_list[i+1], sort_list[i] = sort_list[i], sort_list[i+1]
        swapped = True


def animation(x_list, sort_list, i, comparisons, swaps, image_index, first_or_last = False):
  red = "#d62728"
  green = "#2ca02c"
  blue = "#1f77b4"

  plt.bar(x_list, sort_list, color=blue)
  if not first_or_last:
    plt.bar(x_list[i], sort_list[i], color=green)
    plt.bar(x_list[i+1], sort_list[i+1], color=green)
  plt.title("Comparisons = {:04d} | Swaps = {:04d}".format(comparisons, swaps))
  #plt.legend(["Comparisons = {}".format(x[4]), "Swaps = {}".format(y[2])], ncol=2, bbox_to_anchor=(0, 1), loc="lower left")
  #plt.savefig("img2/bubble_sort_{}.png".format(image_index))
  plt.savefig("img3/bubble_sort_{:04d}.png".format(image_index))
  plt.clf()


def bubble_sort_animation(sort_list):
  n = len(sort_list)
  x_list = [i for i in range(1, n+1)]
  image_index = 0
  comparisons = 0
  swaps = 0

  animation(x_list, sort_list, 0, comparisons, swaps, image_index, True)

  swapped = True
  while swapped:
    swapped = False
    for i in range(n-1):
      comparisons += 1
      if sort_list[i] > sort_list[i+1]:
        sort_list[i+1], sort_list[i] = sort_list[i], sort_list[i+1]
        swapped = True
        swaps += 1
      animation(x_list, sort_list, i, comparisons, swaps, image_index+1)
      image_index += 1
  animation(x_list, sort_list, i, comparisons, swaps, image_index+1, True)
  print(sort_list)


if __name__ == "__main__":

  def test():
    sort_list = [47, 12, 6, 82, 84, 74, 16, 62, 27, 73]
    print("Test list:\n", sort_list)
    bubble_sort(sort_list)
    print("Sorted list:\n", sort_list)


  def time_bubble_sort(sort_list, numbers_to_sort, excecutions = 10000):
    print("Random list:\n", sort_list)
    time = timeit.timeit(stmt="bubble_sort(sort_list)",
                         number=excecutions,
                         globals=globals())
    time_in_sec = time/excecutions
    print("Sorted random list:\n", sort_list)
    print("Time: {:.2e} sec".format(time_in_sec))



  # Running
  #test()

  numbers_to_sort = 100
  sort_list = [random.randint(1, 1000) for i in range(numbers_to_sort)]
  sort_list_copy = sort_list.copy()
  time_bubble_sort(sort_list, numbers_to_sort)


  bubble_sort_animation(sort_list_copy)
