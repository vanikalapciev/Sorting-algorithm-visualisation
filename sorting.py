#Bubble sort
def bubble_sort(list, noOfIter):
# Swap the elements to arrange in order    for iter_num in range(len(list)-1,0,-1):
    for iter_num in range(noOfIter-1,0,-1):
        for idx in range(iter_num):
            if list[idx]>list[idx+1]:
                temp = list[idx]
                list[idx] = list[idx+1]
                list[idx+1] = temp
    return list

#SelectionSort
def selection_sort(nums, noOfIter):
    for i in range(noOfIter):
        lowest_value_index = i
        for j in range(i + 1, noOfIter):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
    return nums

#InsertionSort
def insertion_sort(nums, noOfIter):
    for i in range(1, noOfIter):
        item_to_insert = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = item_to_insert
    return nums

#helper to heap sort
def heapify(nums, heap_size, root_index):
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        heapify(nums, heap_size, largest)

#Heap sort
def heap_sort(nums, noOfIter):
    n = noOfIter

    for i in range(n, -1, -1):
        heapify(nums, n, i)

    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)
        
    return nums

#merge sort
def merge_sort(nums, noOfIter):
    middle = noOfIter // 2
    if len(nums) > 1:
 
        # Finding the mid of the array
        mid = len(nums)//2
 
        # Dividing the array elements
        L = nums[:mid]
 
        # into 2 halves
        R = nums[mid:]
 
        # Sorting the first half
        merge_sort(L, noOfIter)
 
        # Sorting the second half
        merge_sort(R, noOfIter)
 
        i = j = k = 0
 
        # Copy data to temp arrays L[] and R[]
        while i < middle and j < middle:
            if L[i] < R[j]:
                nums[k] = L[i]
                i += 1
            else:
                nums[k] = R[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < middle:
            nums[k] = L[i]
            i += 1
            k += 1
 
        while j < middle:
            nums[k] = R[j]
            j += 1
            k += 1
    return nums

#QuickSort
def partition(nums, low, high):
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        nums[i], nums[j] = nums[j], nums[i]

def quick_sort(nums, noOfIter):
    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, noOfIter - 1)
    return nums

def shell_sort(nums, noOfIter): 
  
    n = noOfIter
    
    gap = n//2
   
    while gap > 0: 
  
        for i in range(gap,n): 
  
            temp = nums[i] 
  
            j = i 
            while  j >= gap and nums[j-gap] >temp: 
                nums[j] = nums[j-gap] 
                j -= gap 
  
            nums[j] = temp 
        gap //= 2
    return nums

def pigeonhole_sort(nums, noOfIter): 
    my_min = min(nums) 
    my_max = max(nums) 
    size = my_max - my_min + 1
  
    holes = [0] * size 
  
    for x in nums: 
        assert type(x) is int, "integers only please"
        holes[x - my_min] += 1
  
    i = 0
    for count in range(noOfIter): 
        while holes[count] > 0: 
            holes[count] -= 1
            nums[i] = count + my_min 
            i += 1
    return nums