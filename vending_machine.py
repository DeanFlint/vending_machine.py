"""
Calculate the coins that should be returned by a vending machine to make the 
correct change. 

Specs:
- Given an amount of change that needs to be paid, we want to generate the 
  list of coins that needs to be given to the customer.
- Pay the minimum number of coins possible
- Available coins: 100, 50, 20, 10, 5, 2, 1
""" 

from vend_test import *

usd_coins = [100, 50, 25, 10, 5, 2, 1]
eur_coins = [100, 50, 20, 10, 5, 2, 1]


def get_change(amount, coins=eur_coins): 
    """Optional argument, if second argument not defined - 
       eur_coins will be it's default"""
    change = []
    for coin in coins:
        while coin <= amount:
            amount -= coin
            change.append(coin)
            
    return change

test_are_equal(get_change(0), [])
test_are_equal(get_change(1), [1])
test_are_equal(get_change(2), [2])
test_are_equal(get_change(5), [5])
test_are_equal(get_change(10), [10])
test_are_equal(get_change(20), [20])
test_are_equal(get_change(50), [50])
test_are_equal(get_change(100), [100])

test_are_equal(get_change(3), [2,1])
test_are_equal(get_change(7), [5,2])
test_are_equal(get_change(9), [5,2,2])

test_are_equal(get_change(35, usd_coins), [25, 10])

print ("All tests pass!")