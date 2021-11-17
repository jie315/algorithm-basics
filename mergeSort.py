def merge(l1:list, l2:list):
    l = []
    while len(l1) > 0 and len(l2) > 0:
        if l1[-1] > l2[-1]:
            l.append(l1.pop())
        else:
            l.append(l2.pop())
    l = l[::-1]
    if len(l1) > 0:
        l = l1 + l
    elif len(l2) > 0:
        l = l2 + l
    return l

def mergeSort(nums:list):
    n = len(nums)
    if n <= 1:
        return nums
    mid = n // 2
    left = mergeSort(nums[:mid])
    right = mergeSort(nums[mid:])

    return merge(left, right)

