
class Sorting:
  def __init__(self, items):
    self.items = items


  def bubble_sort(self):
    """ Also known as Sinking sort """
    items = self.items
    n = len(items)
    swapped = True
    while swapped:
      swapped = False
      for i in range(n-1):
        if items[i] > items[i+1]:
          items[i+1], items[i] = items[i], items[i+1]
          swapped = True
    return items


  def comb_sort():
    return


  def optimized_bubble_sort(self):
    items = self.items
    n = len(items)
    swapped = True
    while swapped:
      swapped = False
      for i in range(n-1):
        if items[i] > items[i+1]:
          items[i+1], items[i] = items[i], items[i+1]
          swapped = True
      n -= 1
    return items


  def insertion_sort(self):
    items = self.items
    for i in range(1, len(items)):
      j = i
      while j > 0 and items[j-1] > items[j]:
        items[j], items[j-1] = items[j-1], items[j]
        j -= 1
    return items


  def selection_sort(self):
    items = self.items
    for i in range(len(items)-1):
      min_index = i
      for j in range(i+1, len(items)):
        if items[j] < items[min_index]:
            min_index = j
      if min_index != i:
        items[i], items[min_index] = items[min_index], items[i]
    return items



  def quicksort_partition(items, low, high):
    """ Lomuto partition scheme """
    i = low
    pivot = items[high]
    for j in range(low, high):
      if items[j] < pivot:
        items[i], items[j] = items[j], items[i]
        i += 1
    items[i], items[high] = items[high], items[i]
    return i


  def quicksort(items, low, high):
    """ The entire list can be sorted by quick_sort(sort_list, 0, len(sort_list)-1) """
    if low < high:
      partition_index = quicksort_partition(items, low, high)
      quicksort(items, low, partition_index-1)
      quicksort(items, partition_index+1, high)

    return items


  def merge_sort(self):
    return


  def heapsort(self):
    return


  def shellsort(self):
    """ Using Marcin Ciura's gap sequence with an inner insertion sort """
    items = self.items
    n = len(items)
    gaps = [701, 301, 132, 57, 23, 10, 4, 1]

    for gap in gaps:
      for i in range(gap, n):
        temp = items[i]
        j = i
        while j >= gap and items[j-gap] > temp:
          items[j] = items[j - gap]
          j -= gap
        items[j] = temp
    return items



  def gnome_sort(self):
    """ Also known as stupid sort """
    items = self.items
    position = 0
    while position < len(items):
      if position == 0 or items[position] >= items[position-1]:
        position += 1
      else:
        items[position], items[position-1] = items[position-1], items[position]
        position -= 1
    return items


  ## TODO:
  ## * Make better tests!!!! (assert)
  ## * Rewrite to look cleaner!
  ## * Fix Quicksort!


if __name__ == "__main__":
  def test():
    items1 = [47, 12, 6, 82, 84, 74, 16, 62, 27, 73, 16]
    items2 = items1.copy()
    items3 = items1.copy()
    items4 = items1.copy()
    items5 = items1.copy()
    items6 = items1.copy()
    items7 = items1.copy()
    print("Test list:\n{}\n".format(items1))

    test_object = Sorting(items1)
    print("Bubble sort:\n{}".format(test_object.bubble_sort()))

    test_object2 = Sorting(items2)
    print("Optimized Bubble sort:\n{}".format(test_object2.optimized_bubble_sort()))

    test_object3 = Sorting(items3)
    print("Insertion sort:\n{}".format(test_object3.insertion_sort()))

    test_object4 = Sorting(items4)
    print("Selection sort:\n{}".format(test_object4.selection_sort()))

    #test_object5 = Sorting(items5)
    #print("Quicksort:\n{}".format(quicksort(items5, 0, len(items5)-1)))

    test_object7 = Sorting(items7)
    print("Selection sort:\n{}".format(test_object7.shellsort()))

    test_object6 = Sorting(items6)
    print("Gnome sort:\n{}".format(test_object6.gnome_sort()))

  test()