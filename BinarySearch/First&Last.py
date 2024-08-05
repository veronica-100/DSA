class Solution(object):
    def valueEqualToIndex(self, arr, n):
        for i in range(0, n):
            if arr[i] == i+1:
                print( arr[i]