# In this code we are going to find next permutation

# Algorithm:

# First, find the break point: Traverse from the end of the list and find a number whose next traversed number is smaller than it. This will become the break point.
# If no break point is found, sort the given list.
# Now, swap the break point with the smallest number having an index greater than it, and then sort the remaining list after the break point.



class Solution:
    def nextPermutation(self, nums):
        if len(nums) > 1:
            breakindex = -1
            for i in range(len(nums) - 1, 0, -1):
                if nums[i] > nums[i - 1]:
                    breakindex = i - 1
                    break
            if breakindex == -1:
                nums.sort()
            else:
                b = float('inf')
                c = -1
                for i in range(len(nums) - 1, breakindex, -1):
                    if nums[i] > nums[breakindex] and nums[i] < b:
                        b = nums[i]
                        c = i
                if c != -1:
                    nums[breakindex], nums[c] = nums[c], nums[breakindex]
                nums[breakindex + 1:] = nums[breakindex + 1:][::-1]
        print(nums)
nums = list(map(int, input("Enter integer seprated by spaces ").split()))
o1 = Solution()
o1.nextPermutation(nums)
