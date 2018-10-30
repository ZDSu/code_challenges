from string_permutation import *


def test_string_permutation():
    assert sorted(permute('abc')) == sorted(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    assert sorted(permute('dog')) == sorted(['dog', 'dgo', 'odg', 'ogd', 'gdo', 'god'])