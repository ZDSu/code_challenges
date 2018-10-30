from coin_change import *


# NOTE: NON-DYNAMIC FUNCTIONS WILL TAKE A LONG TIME TO TEST. IF YOU BELIEVE YOU HAVE A SOLUTION GO CHECK THE SOLUTION NOTEBOOK INSTEAD OF RUNNING THIS!
def test_coin_change():
    assert rec_coin(10, [1, 5]) == 2
    coins = [1, 5, 10, 25]
    assert rec_coin(45, coins) == 3
    assert rec_coin(23, coins) == 5
    assert rec_coin(74, coins) == 8