# nums = [1,2,3,4,5,6,7,8,9]
# target = 6
# k = 3
# nums1 = nums[-k:] + nums[:-k]
# for i in range(len(nums1)):
#     if nums1[i] == target:
#         print(i, end=' ')
#         break
# else:
#         print(-1)







nums = [17 , 18, 19,1,2,3,4,5,6,7,8,9]
target = 1
low = 0
high = len(nums) - 1
while low <= high:
    mid = (low + high) // 2
    if nums[mid] == target:
        print(mid)
        break
    if nums[low] <= nums[mid]:
        if nums[low] <= target < nums[mid]:
            high = mid - 1
        else:
            low = mid + 1



    else:       
        if nums[mid] < target <= nums[high]:
            low = mid + 1
        else:
            high = mid - 1
else:    
    print(-1)