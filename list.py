# creating a list  
lst=[1,2,3,4,5]
 #empty list
lst1=[]
#mixed list
lst2=[1,"hello",3.4,True]

#accessing the list elements
print(lst[0]) #accessing the first element
print(lst[2]) #accessing the third element
print(lst[-1]) #accessing the last element

#slicing the list
print(lst[1:4]) #slicing from index 1 to 3
print(lst[:3]) #slicing from the beginning to index 2

#mutalbe nature of list
lst[0] = 10 #changing the first element to 10
print(lst) #printing the modified list

#3. List Methods
#Adding elements to a list
lst.append(6) #adding an element at the end of the list
print(lst) #printing the modified list
lst.insert(2, 15) #inserting an element at index 2
print(lst) #printing the modified list

#Removing elements from a list
lst.remove(3) #removing the element with value 3    
print(lst) #printing the modified list
lst.pop(1) #removing the element at index 1 
print(lst) #printing the modified list
lst.clear() #removing all elements from the list
print(lst) #printing the modified list

#searching and counting for an element in a list
lst2 = [1, "hello", 3.4, True,True]
print(lst2.index("hello")) #searching for the index of "hello" in the list
print(lst2.count(1)) #counting the number of occurrences of 1 in the list

#sorting and reverse a list
lst2.sort() #sorting the list in ascending order
print(lst2) #printing the sorted list
lst2.reverse() #reversing the list
print(lst2) #printing the reversed list

#cpying a list
lst3 = lst2.copy() #creating a copy of lst2
print(lst3) #printing the copied list


#4. Built-in Functions with Lists

#len() function to get the length of a list
print(len(lst2)) #printing the length of lst2

#sum() function to get the sum of elements in a list
lst4 = [1, 2, 3, 4, 5]  
print(sum(lst4)) #printing the sum of elements in lst4

#max() function to get the maximum element in a list    
print(max(lst4)) #printing the maximum element in lst4

#min() function to get the minimum element in a list
print(min(lst4)) #printing the minimum element in lst4


#LOOPING IN LISTS
#using for loop to iterate through a list
for item in lst4:
    print(item) #printing each item in lst4