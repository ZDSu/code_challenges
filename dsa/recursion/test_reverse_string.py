from reverse_string import *


def test_reverse_string():
    assert reverse('hello world') == 'dlrow olleh'
    assert reverse('hello') == 'olleh'
    assert reverse('123456789') == '987654321'