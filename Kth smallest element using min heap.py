
#########################Algorithm to Find Kth Smallest Element Using Min-Heap#########################
# 1. Heapify the Array: Convert the input array into a Min-Heap using heapify().
# 2. Remove Smallest Elements: Pop the smallest element k−1 times from the heap.
# 3. Retrieve the kth Smallest: The root of the heap after k−1 pops is the k-th smallest element.
# 4. Return the Result: Return the popped root value as the k-th smallest element.



import heapq
class Solution():
    def kth_smallest_min_heap(self,arr, k):
        heapq.heapify(arr)
        for _ in range(k - 1):
            heapq.heappop(arr)
        return heapq.heappop(arr)

arr = list(map(int, input("Enter integer seprated by spaces ").split()))
k=int(input("insert target element"))
o1 = Solution()
print(o1.kth_smallest_min_heap(arr,k))
