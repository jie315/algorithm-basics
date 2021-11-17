# Method 1
def quickSort(nums:list):
    n = len(nums)
    if n <= 1:
        return nums
    left = [i for i in nums[1:] if i < nums[0]]
    right = [i for i in nums[1:] if i >= nums[0]]

    return quickSort(left) + [nums[0]] + quickSort(right)


# Method 2
def quickSort(nums:list):
    n = len(nums)
    if n <= 1:
        return nums

    return qSort(nums, 0, n-1)

def qSort(nums, left, right):
    if left < right:
        pivot = partition(nums, left, right)
        qSort(nums, left, pivot-1)
        qSort(nums, pivot+1, right)
    return nums

def partition(nums, left, right):
    pivot_value = nums[left]
    while left < right:
        while left < right and nums[right] >= pivot_value:
            right -= 1
        nums[left] = nums[right]
        while left < right and nums[left] <= pivot_value:
            left += 1
        nums[right] = nums[left]
    nums[left] = pivot_value
    return left
