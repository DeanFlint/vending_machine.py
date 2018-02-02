def number_of_evens(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1
    return count
    

def test_are_equal(actual, expected):
    assert expected == actual, "Expected {0}, got {1}".format(expected, actual)
    
def test_not_equal(a, b):
    assert a != b, "Did not expect {0} but got {1}".format(a, b)
    
def test_is_in(collection, item):
    assert item in collection, "{0} does not contain {1}".format(collection, item)
    
def test_not_in(collection, item):
    assert item not in collection, "{0} does contain {1}".format(collection, item)
    
def test_in_between(collection, item):
    assert item >= min(collection) and item <= max(collection), "{1} is not between values {0}".format(collection, item) 
    
test_are_equal(number_of_evens([1,2,3,4,5]), 2)
test_not_equal(number_of_evens([1,2,3,4,5]), 1)
test_is_in([1,2,3,4,5], 5)
test_not_in([1,2,3,4,5], 7)
test_in_between([1,2,3,4,5], 3)