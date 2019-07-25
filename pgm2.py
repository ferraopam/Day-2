"""2.	Write a program to accept a two-dimensional array containing integers as the parameter and determine the following from the elements of the array:
a.	element with minimum value in the entire array
b.	element with maximum value in the entire array
c.	the elements with minimum and maximum values in each column
d.	the elements with minimum and maximum values in each row

Example:
Input: 
[[0 1 2 3]
 [3 4 5 5]
 [6 7 8 8]
 [9 0 1 9]]"""
import  itertools
r = int(input("Enter number of rows"))
c = int(input("Enter the number of columns"))
main_list = []
for i in range(r):
    temp_list = []
    for j in range(c):
        temp_list.append(input("Element {0}:{1}: ".format(i , j)))
    main_list.append(temp_list)
i = 0
for l in main_list:
    print(f"Max of {i} th row is:{max(l)}")
    i += 1
    for l in main_list:
        print(f"Min of {i} th row is :{min(l)}")
        i += 1
    i = 0
    for l in main_list:
        print(f"Max of {i} th row is :{max(l)}")
        i =+ 1
    i = 0
    for l in main_list:
        print(f"Min of {i} th row is :{min(l)}")
    l = list(itertools.chain.from_iterable(main_list))
    print(f"Max of all elements in list is {max(l)} and min is {min(l)}")



    