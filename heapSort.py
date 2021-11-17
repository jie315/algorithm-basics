def heapSort(nums:list):
    n = len(nums)
    if n <= 1:
        return nums
    
    result = []
    while len(nums) > 0:
        n = len(nums)
        for i in range(n-1, -1, -1):
            left = 2*i + 1
            right = 2*i + 2
            if left < n and nums[i] < nums[left]:
                # 有左节点
                nums[i], nums[left] = nums[left], nums[i]
            if right < n and nums[i] < nums[right]:
                # 有右节点
                nums[i], nums[right] = nums[right], nums[i]
        result = [nums.pop(0)] + result
    return result
