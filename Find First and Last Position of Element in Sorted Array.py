class Solution:
    def searchRange(self, nums, target):
        low, high = 0, len(nums) - 1
        a = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                a = mid
                high = mid - 1  # Continue searching the left half for first occurrence
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        low, high = 0, len(nums) - 1
        b = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                b = mid
                low = mid + 1  # Continue searching the right half for last occurrence
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return [a, b]  # Return both first and last occurrences

# Input handling
nums = list(map(int, input("Enter integers separated by spaces: ").split()))
target = int(input("Insert target element: "))

o1 = Solution()
print(o1.searchRange(nums, target))
