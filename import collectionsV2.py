import collections  
  
list1 = [10, 20, 30, 40, 50, 60]  
list2 = [10, 20, 30, 50, 40, 70]  
list3 = [50, 10, 30, 20, 60, 40]  
  
# Sorting the list  
list1.sort()  
list2.sort()  
list3.sort()  
  
  
if list1 == list2:  
    print("Lista broj 1 i lista broj 2 nisu iste")  
else:  
    print("Lista broj 2 nije ista kao broj 1")  
  
if list1 == list3:  
    print("Lista broj 1 i lista broj 2 su iste")  
else:  
    print("Lista 2 i 1 su iste")  