def quicksort(nums):
    if len(nums) < 2:
        return nums
    else:
        print(nums)
        pivot = nums[0]
        less = []
        greater = []
        for i in nums[1:]:
            if i <= pivot:
                less.append(i)
            else:
                greater.append(i)
                
            print(f"less:{less} + pivot:[{pivot}] + greater:{greater}")
        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([4,12,43,6,2,9,0,5]))