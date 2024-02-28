def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    iterations = 0
    
    while low <= high:
        mid = (low + high) // 2
        iterations += 1
        
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return iterations, arr[mid]
    
    if high < 0:
        return iterations, None
    
    return iterations, arr[low] if low < len(arr) else None

# Приклад використання:
arr = [0.1, 0.5, 0.7, 1.2, 1.5, 2.0, 2.3, 3.0]
target = 1.3
iterations, upper_bound = binary_search(arr, target)
print("Кількість ітерацій:", iterations)
print("Верхня межа:", upper_bound)