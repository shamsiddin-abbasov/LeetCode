# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/description/

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxfr = arr[len(arr)-1]
        arr[len(arr)-1] = -1

        for i in range(len(arr)-2, -1, -1):
            tmp = arr[i]
            arr[i] = maxfr

            if maxfr < tmp:
                maxfr = tmp
        return arr
