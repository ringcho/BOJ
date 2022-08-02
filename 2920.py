from audioop import reverse
nums = map(int,input().split())
nums = list(nums)
if sorted(nums) == nums:
    print('ascending')
elif sorted(nums, reverse=True) == nums:
    print('descending')
else:
    print('mixed')
