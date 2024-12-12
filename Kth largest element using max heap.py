
#########################Algorithm to Find Kth Smallest Element Using Min-Heap#########################
# 1. make the Array Values Negative: Convert each value to negative using for loop.
# 2. Heapify the Array: Convert the input array into a max-Heap using heapify().
# 3. Remove Smallest Elements: Pop the largest element k−1 times from the heap.
# 4. Retrieve the kth Smallest: The root of the heap after k−1 pops is the k-th largest element.
# 5. Return the Result: Return the popped root value as the k-th largest element(reverse symbol).



import heapq
class Solution():
    def kth_largest_max_heap(self,arr, k):
        arr=[-x for x in arr]
        heapq.heapify(arr)
        for _ in range(k - 1):
            heapq.heappop(arr)
        return -heapq.heappop(arr)

# arr =[7, 10, 4, 3, 40,30,65,20, 15]
# k = 3
arr = list(map(int, input("Enter integer seprated by spaces ").split()))
k=int(input("insert target element"))
o1 = Solution()
print(o1.kth_largest_max_heap(arr,k))
