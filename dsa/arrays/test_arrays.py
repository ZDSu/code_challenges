from arrays import *


def test_anagrams():
    assert anagram('dog','god') is True
    assert anagram('clint eastwood','old west action') is True
    assert anagram('aa','bb') is False
    assert anagram('go go go','gggooo') is True
    assert anagram('abc','cba') is True
    assert anagram('hi man','hi     man') is True
    assert anagram('aabbcc','aabbc') is False
    assert anagram('123','1 2') is False


def test_pair_sum():
    assert pair_sum([1,3,2,2],4) == 2
    assert pair_sum([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10) == 6
    assert pair_sum([1,2,3,1],3) == 1
    # additional tests from Providence interview
    assert pair_sum([1, 2, 3, 6, 7, 8, 9, 1], 10) == 3
    assert pair_sum([6, 12, 3, 9, 3, 5, 1], 12) == 1


def test_missing_element():
    assert finder([1,2,3,4,5,6,7], [3,7,2,1,4,6]) == 5
    assert finder([5,5,7,7], [5,7,7]) == 5
    assert finder([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1]) == 6


def test_largest_sum():
    assert large_cont_sum([1,2,-1,3,4,10,10,-10,-1]) == 29
    assert large_cont_sum([1,2,-1,3,4,-1]) == 9
    assert large_cont_sum([-1,1]) == 1
    # additional tests
    assert large_cont_sum([-4, -1, -3, -2]) == -1
    assert large_cont_sum([1,2,-1,3,4,10,10,10,-1]) == 39


def test_sentence_reversal():
    assert rev_word('Hi John,   are you ready to go?') == 'go? to ready you are John, Hi'
    assert rev_word('    space before') == 'before space'
    assert rev_word('space after     ') == 'after space'
    assert rev_word('   Hello John    how are you   ') == 'you are how John Hello'
    assert rev_word('1') == '1'
    assert rev_word('This is the best') == 'best the is This'


def test_string_compression():
    assert compress('AAAAABBBBCCCC') == 'A5B4C4'
    assert compress('') == ''
    assert compress('AABBCC') == 'A2B2C2'
    assert compress('AAABCCDDDDD') == 'A3B1C2D5'


def test_unique_char():
    assert uni_char('') is True
    assert uni_char('goo') is False
    assert uni_char('abcdefg') is True