class py_solution:
    def twoSum(self, nums, target):
        lookup = {}
        for i, num in enumerate(nums):
            print(i)
            print("nums", nums)
            if target - num in lookup:
                return lookup[target - num], i
            lookup[num] = i


print("index1=%d, index2=%d" % py_solution().twoSum((10, 20, 40, 10), 50))
