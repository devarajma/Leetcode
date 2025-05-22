class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def bina(nums, x, flag):
            l,h = 0 , len(nums)-1
            n = -1
            while h >=l:
                mid= (h+l)//2
                if nums[mid] == x:
                    n = mid
                    if flag:
                        h = mid - 1
                    else:
                        l = mid + 1


                elif nums[mid] > x:
                    h = mid-1
                else:
                    l = mid+1
            else:
                return n

        s =  bina(nums, target, True)
        e =  bina(nums, target, False)

        return [s,e]