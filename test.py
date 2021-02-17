import random
import matplotlib.pyplot as plt 


x = [i for i in range(10)]
y = [random.randint(0,10) for i in range(10)]


#plt.plot(x, y)
#plt.plot(y, x)
#plt.title("wtf = {:04d} | www = {:04d}".format(x[4], y[2]))
#plt.legend(["wtf = {}".format(x[4]), "www = {}".format(y[2])], ncol=2, bbox_to_anchor=(0, 1), loc="lower left")
#plt.show()

from SortingClass import Sorting

list1 = y.copy()
list2 = y.copy()

print("Test 1:")
print(list1)
test1 = Sorting(list1)
sorted_list1 = test1.bubble_sort()
print(sorted_list1)

print("\nTest 2:")
print(list2)
test2 = Sorting(list2)
sorted_list2 = test2.optimized_bubble_sort()
print(sorted_list2)