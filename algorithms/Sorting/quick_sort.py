import random
n = 5
data = [8, 5, 4, 7, 2]

''' Quick Sort '''
def quick_sort(start, end):
    if start >= end: 
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and data[left] <= data[pivot]:
            left += 1
        while right > start and data[right] >= data[pivot]:
            right -= 1
        if left > right:
            data[right], data[pivot] = data[pivot], data[right]
        else:
            data[left], data[right] = data[right], data[left]
    # 재귀 호출
    quick_sort(start, right - 1)
    quick_sort(right + 1, end)

quick_sort(0, n - 1)

print(data)


''' Quick implementation: Quick Select & Sort '''
def quick_select(arr,k):
    if arr:
        pivot = random.choice(arr)
        lows = [el for el in arr if el < pivot]
        highs = [el for el in arr if el > pivot]
        pivots = [el for el in arr if el == pivot]   # 중복 고려
        
        if k <= len(lows):
            return quick_select(lows,k)
        elif k <= len(lows) + len(pivots):
            return pivots[0]
        else:
            return quick_select(highs,k-len(lows) -len(pivots))

def quick_sort(arr):
	if len(arr) <=1:
		return arr
	pivot = random.choice(arr)
	lows = [el for el in arr if el < pivot]
	highs = [el for el in arr if el > pivot]
	pivots = [el for el in arr if el == pivot]
	
	return quick_sort(lows) + pivots + quick_sort(highs)

arr = [5, 3, 2, 4, 1]

print(quick_select(arr,3))  #out: 3
print(quick_sort(arr))      #out: [1, 2, 3, 4, 5]
