class Solution(object):
    def sort(l, n, k):
        heap = l[:k + 1]
        heapify(heap)
        j = 0
        for i in range(k + 1, n):
            print(heappop(heap))
            heappush(heap, l[i])
        while len(heap) != 0:
            print(heappop(heap))