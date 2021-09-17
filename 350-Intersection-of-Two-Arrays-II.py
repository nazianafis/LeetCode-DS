class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums3 = collections.Counter(nums1)
        nums4 = collections.Counter(nums2)
        nums5 = []
        for key1 in nums3:
            for key2 in nums4:
                if key1 == key2:
                    l1 = nums3[key1]
                    l2 = nums4[key2]
                    if l1 == l2:
                        for i in range(l2):
                            nums5.append(key1)
                        break
                    else:
                        if l1 < l2:
                            l3 = l1
                        else:
                            l3 = l2
                        for i in range(l3):
                            nums5.append(key1)
                        break
        return nums5
