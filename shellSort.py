def shellSort(nums:list):
    n = len(nums)
    if n <= 1:
        return nums

    # 设置步长
    step = n // 2 
    while step > 0:
        for i in range(step, n):
            # 跨步长比较，如果符合条件，则交换
            while i >= step and nums[i-step] > nums[i]:
                nums[i-step], nums[i] = nums[i], nums[i-step]
                i -= step
        # 缩小步长
        step //= 2
    return nums
