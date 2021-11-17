def selectSort(nums:list):
    n = len(nums)
    if n <= 1:
        return nums
    
    for i in range(n):
        min_value = min(nums[i:])
        min_index = nums.index(min_value)
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums
