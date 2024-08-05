class Solution(object):
    def kthSmallest(self, arr, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(arr)
        maxHeap = []
        for i in range(0, k):
            maxHeap.append(arr[i])

        for i in range(k, n):
            maxHeap.sort(reverse=True)
            if maxHeap[0] < arr[i]:
                continue
            else:
                maxHeap.pop(0)
                maxHeap.append(arr[i])
        print(max(maxHeap))