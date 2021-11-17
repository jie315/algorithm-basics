def countSort(nums:list):
    n = len(nums)
    if n <= 1:
        return nums

    l = [0] * (max(nums)+1) # 初始化桶
    for i in nums:
        l[i] += 1
    result = []
    for i in range(len(l)):
        if l[i] == 0:
            continue
        for c in range(l[i]):
            result.append(i)
    return result
