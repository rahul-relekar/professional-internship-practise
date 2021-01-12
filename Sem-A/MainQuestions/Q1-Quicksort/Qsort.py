"""

    Write a function by Quick Sort algorithm to sort the following array.
    data = 3, 4, 9, 0, 2, 2, 3, 5, 11, 1

    Type: Divide-and-Conquer Algorithm

"""

# function to sort the integer array in ascending order
def QuickSort(arr):

    # saves the length of the given array arr
    elements = len(arr)
    
    #Base case
    if elements < 2:
        return arr
    
    # We have chosen the start position of the partitioning element
    current_position = 0 

    #Partitioning loop
    for index in range(1, elements):

        #  if the sub array element on the right side is smaller than the left element,
        # then swap it with the pivot and change the index to the next element
         if arr[index] <= arr[0]:


             # Changed the index when condition is met  
             current_position += 1

             # Swap it with the sub-array element
             temp = arr[index]
             arr[index] = arr[current_position]
             arr[current_position] = temp

    #  Once the element has pass through the conditon,
    #  we can swap it with the pivot element
    temp = arr[0]
    arr[0] = arr[current_position] 
    # Brings pivot to it's appropriate position
    arr[current_position] = temp 
    
    # Sorts the elements to the left of pivot
    left = QuickSort(arr[0:current_position])

    # Sorts the elements to the right of pivot
    right = QuickSort(arr[current_position+1:elements]) 

    # finally merge the completely sorted sub-arrays on both the side of the pivot
    arr = left + [arr[current_position]] + right #Merging everything together
    
    return arr


data = [3, 4, 9, 0, 2, 2, 3, 5, 11, 1]
print("Given Array : ",data,"\n")
print("Sorted Array: ",QuickSort(data),"\n")