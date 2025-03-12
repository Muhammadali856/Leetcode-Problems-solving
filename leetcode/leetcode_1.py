nums = [3, 2, 3]
target = 6

for i in range(len(nums)-1):
    for a in range(i + 1, len(nums)):
        if nums[i] + nums[a] == target:
            print(i, a)