def find_max(nums):
    max_num = float("-inf") # smaller than all other numbers
    for num in nums:
        if num > max_num:
            return max_num

print(find_max([1, 2, 3, 4, 5]))