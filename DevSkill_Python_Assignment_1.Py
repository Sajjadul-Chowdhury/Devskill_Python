"""
Python Assignment: 1
Author: Sajjadul
----------------------
Task : 1. Take input of two integer lists and Concatenate two lists index-wise

suppose the user gives inputs such as a = [4, 3, 6] and b = [7. 2, 11]
the output should be = [11, 5, 17]. Make sure you consider the corner cases
"""
# Asking for number of element from the user
list_1_user_input= int(input("Number of Element for List_1 "))
list_2_user_input= int(input("Number of Element for List_2 "))
list_1= [ ]
list_2= [ ]
print ( )

# user defined list input
print("Enter ", list_1_user_input, " number for List_1")
for i in range(list_1_user_input):

    j= int(input())
    list_1.append(j)

print ( )
print("Enter ", list_2_user_input, " number for List_2")
for i in range(list_2_user_input):
    j= int(input())
    list_2.append(j)

print ( )
print("List_1 from user input: ",list_1)
print("List_1 from user input: ",list_2)


# checking both list consist same number of element or not.
# If different then it will append zero to ensure that both list consist same number of element. 
if len(list_1)!=len(list_2):
    if len(list_1)>len(list_2):
        for i in range(len(list_1)-len(list_2)):
            list_2.append(0)
    else:
        for j in range(len(list_2)-len(list_1)):
            list_1.append(0)

# concatenate list_1 and list_2
list_3 = [ i+j for i, j in zip(list_1, list_2)]
print ( )
print("Element wise concatanated number list: ", list_3)


"""
-------------------------------------------------------------
Task-2: Reverse a list in Python (without the reverse method)
-------------------------------------------------------------
"""

list_4=[1, 2, 3, 'a', 'b', 'c', 10.523]

"""
reversed_list= list_4[: : -1]
print( )
print(reversed_list)

"""

# this function reverse a list
def reversed_list(user_list):
    new_list= user_list[: : -1]
    return new_list

print( )
print("Reversed List: ", reversed_list(list_4))


"""
---------------------------------------------------------
Task 3. Add a new item to the list after a specified item
---------------------------------------------------------
"""
list_comb=[1, 2, 3, 'ab', 'cd', 'gh']
print( )
print("Given List: ", list_comb)

list_comb.insert(list_comb.index('cd') + 1, 'ef')


print("After adding a new item (ef) to the list after a specified item (cd): ",list_comb)


"""
--------------------------------------------------------------
Task 4: Remove all occurrences of a specific item from a list.
--------------------------------------------------------------

Given a Python list, write a program to remove all occurrences of item 20.
list1 = [5, 20, 15, 20, 25, 50, 20]

the output should be [5,15, 25, 50]
"""
list1 = [5, 20, 15, 20, 25, 50, 20]
k = [ ]

#removing all the occurences from the list
for i in list1:
    j=list1.count(i)
    if j>1:
        continue
    else:
        k.append(i) 

print( )
print("Given List: ",list1)
print("After removing all the occurrences: ", k)

