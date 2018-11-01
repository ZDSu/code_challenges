from homework import *


def test_fac():
    assert fact(5) == 120
    assert fact(4) == 24


def test_rec_sum():
    assert rec_sum(4) == 10


def test_sum_func():
    assert sum_func(4321) == 10


def test_word_split():
    assert word_split('themanran',['the','ran','man']) == ['the', 'man', 'ran']
    assert word_split('ilovedogsJohn',['i','am','a','dogs','lover','love','John']) == ['i', 'love', 'dogs', 'John']
    assert word_split('themanran',['clown','ran','man']) == []