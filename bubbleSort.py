def bubbleSort(nums:list):
    # assert(type(nums) == type([])) 
    # 可以在条件不满足程序运行的情况下直接返回错误，
    # 而不必等待程序运行后出现崩溃的情况
    
    n = len(nums)
    if n <= 1:
        return nums

    for _ in range(n-1):
        judge = False
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                nums[i],nums[i+1] = nums[i+1],nums[i]
                judge = True
        if not judge:
            break
    return nums
