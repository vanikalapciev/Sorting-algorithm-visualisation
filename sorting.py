#Bubble sort
def bubbleSort(arr, iterations): 
    n = len(arr) 
  
    for i in range(iterations): 

        for j in range(0, n-i-1): 
  
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
    return arr

#SelectionSort
def selectionSort(arr, iterations):
    for i in range(iterations): 
      
    # Find the minimum element in remaining  
    # unsorted array 
        min_idx = i 
        for j in range(i+1, len(arr)): 
            if arr[min_idx] > arr[j]: 
                min_idx = j 
                  
        # Swap the found minimum element with  
        # the first element         
        arr[i], arr[min_idx] = arr[min_idx], arr[i] 
    
    return arr

#InsertionSort
def insertionSort(arr, iterations): 
  
    for i in range(iterations): 
  
        key = arr[i] 
  
        j = i-1
        while j >= 0 and key < arr[j] : 
                arr[j + 1] = arr[j] 
                j -= 1
        arr[j + 1] = key
    return arr

#helper to heap sort
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2

    if l < n and arr[largest] < arr[l]:
        largest = l
 
    if r < n and arr[largest] < arr[r]:
        largest = r
 
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
 
        heapify(arr, n, largest)
 
 
#Heap sort
def heapSort(arr, iterations):
    n = iterations
 
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
 
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)
    return arr

#shell sort
def shellSort(arr, iterations): 
  
    n = iterations
    
    gap = n//2
   
    while gap > 0: 
  
        for i in range(gap,n): 
  
            temp = arr[i] 
  
            j = i 
            while  j >= gap and arr[j-gap] >temp: 
                arr[j] = arr[j-gap] 
                j -= gap 
  
            arr[j] = temp 
        gap //= 2
    return arr

def pigeonholeSort(arr, iterations): 
    my_min = min(arr) 
    my_max = max(arr) 
    size = my_max - my_min + 1
  
    holes = [0] * size 
  
    for x in arr: 
        assert type(x) is int, "integers only please"
        holes[x - my_min] += 1
  
    i = 0
    for count in range(iterations): 
        while holes[count] > 0: 
            holes[count] -= 1
            arr[i] = count + my_min 
            i += 1
    return arr

def countSort(arr, iterations): 
    max_element = int(max(arr)) 
    min_element = int(min(arr)) 
    range_of_elements = max_element - min_element + 1
    count_arr = [0 for _ in range(range_of_elements)] 
    output_arr = [0 for _ in range(len(arr))] 
  
    for i in range(len(arr)): 
        count_arr[arr[i]-min_element] += 1
  
    for i in range(1, len(count_arr)): 
        count_arr[i] += count_arr[i-1] 
  
    for i in range(iterations-1, -1, -1): 
        output_arr[count_arr[arr[i] - min_element] - 1] = arr[i] 
        count_arr[arr[i] - min_element] -= 1
  
    for i in range(iterations): 
        arr[i] = output_arr[i] 
  
    return arr
