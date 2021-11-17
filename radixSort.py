def radixSort(nums:list):
    n = len(nums)
    if n <= 1:
        return nums

    maxi = max(nums)
    p = 1
    while maxi >= 10**p:
        p += 1

    for i in range(p):
        bucket = [[] for _ in range(10)]
        for j in nums:
            radix = (j // 10**i) % 10
            bucket[radix].append(j)
        j = 0
        for radix in range(10):
            for m in bucket[radix]:
                nums[j] = m
                j += 1
    return nums
