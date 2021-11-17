def insertSort(nums:list):
    n = len(nums)
    if n <= 1:
        return nums
    
    for i in range(1, n):
        insert_value = nums[i] # 下面循环可能改变nums[i]的值
        j = i-1
        while j >= 0 and nums[j] > insert_value:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = insert_value
    return nums
