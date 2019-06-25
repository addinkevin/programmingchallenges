import unittest


"""
Given an array of integers, find the subset of non-adjacent elements with 
the maximum sum. Calculate the sum of that subset.
"""
def maxSubsetSum(arr):
    # Opt[n] = Optimal solution considering all n elements
    # Base case: Opt[0] = arr[0], Opt[1] = max(arr[0], arr[1])
    opt = [arr[0], max(arr[0], arr[1])]
    for i in range(2, len(arr)):
        # You need to consider three cases for computing opt[i]
        # 1. Opt[i-1] (last optimal solution)
        # 2. Opt[i-2] + arr[i] (restriction of non adjacent elements)
        # 3. Start over with the value arr[i]
        opt.append(max(opt[-1], opt[-2] + arr[i], arr[i]))
    
    return opt[-1]

class MaxArraySumTest(unittest.TestCase):

    def check(self, arrayString, expectedOutput):
        array = list(map(int, arrayString.split()))
        self.assertEqual(maxSubsetSum(array), expectedOutput)

    def testCase0(self):
        arrayString = "3 7 4 6 5"
        expectedOutput = 13
        self.check(arrayString, expectedOutput)

    def testCase1(self):
        arrayString = "2 1 5 8 4"
        expectedOutput = 11
        self.check(arrayString, expectedOutput)
    
    def testCase2(self):
        arrayString = "3 5 -7 8 10"
        expectedOutput = 15
        self.check(arrayString, expectedOutput)

if __name__ == "__main__":
    unittest.main()
