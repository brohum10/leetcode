nums = [1, 2, 3, 4, 5]
target = 9

def twoSum(nums, target):
  for i in range(len(nums)):
    for j in range(i, len(nums)):
      if (nums[i]+nums[j]) == target:
        print(nums[i], nums[j])

twoSum(nums, target)
