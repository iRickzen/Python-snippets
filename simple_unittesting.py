#Some basic unit testing
import unittest

class TestClass(unittest.TestCase):
    def test_square(self):
        self.assertEqual(list(square([1,3,5])),[1,9,25])
        self.assertEqual(list(square([2,4,8])),[4,16,64])
        self.assertEqual(list(square([5,7,6])),[25,49,36])

    def test_add(self):
        self.assertEqual(list(add([1,3,5])),[2,6,10])
        self.assertEqual(list(add([2,4,8])),[4,8,16])
        self.assertEqual(list(add([5,7,6])),[10,14,12])


### some function to test
def square(nums):
    for i in nums:
        yield(i*i)

def add(nums):
    for i in nums:
        yield(i+i)




if __name__ == "__main__":
    # test_nums = sum([1,3,5,4,5,6,7,8])

    # for n in test_nums:
    #     print(n)

    unittest.main()


