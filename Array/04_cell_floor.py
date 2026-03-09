
# You are given a sorted array of integers num and a target value target.

# Write a program that:
# If the target exists in the array, print the target and its index.
# If the target does not exist, find the largest number smaller than the target and print it.
# If the target is greater than all elements, print the largest element in the array.










num = [1,2,3,4,5,7,8,12,23]
target = 9

for i in range(len(num)):
    if num[i] == target:
        print(num[i], num[i])
        break
    else: 
        if target > num[i] and target < num[i + 1]:
            print(num[i] , -1)
            break
else:
    print(num[-1], -1)