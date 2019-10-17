import unittest


def has_palindrome_permutation(the_string):

    # Check if any permutation of the input is a palindrome


    return False


















# Tests

class Test(unittest.TestCase):

    def test_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcbcd')
        self.assertTrue(result)

    def test_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabccbdd')
        self.assertTrue(result)

    def test_no_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcd')
        self.assertFalse(result)

    def test_no_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabbcd')
        self.assertFalse(result)

    def test_empty_string(self):
        result = has_palindrome_permutation('')
        self.assertTrue(result)

    def test_one_character_string(self):
        result = has_palindrome_permutation('a')
        self.assertTrue(result)


unittest.main(verbosity=2)


"""
Hash Table/Hashing Coding Interview Questions

MillionGazillion »
I'm making a new search engine called MillionGazillion(tm), and I need help figuring out what data structures to use.
https://www.interviewcake.com/question/python/compress-url-list

Inflight Entertainment »
Writing a simple recommendation algorithm that helps people choose which movies to watch during flights
https://www.interviewcake.com/question/python/inflight-entertainment

Permutation Palindrome »
Check if any permutation of an input string is a palindrome.

Top Scores »
Efficiently sort numbers in an array, where each number is below a certain maximum.
https://www.interviewcake.com/question/python/top-scores

Word Cloud Data »
You're building a word cloud. Write a function to figure out how many times each word appears so we know how big to make each word in the cloud.
https://www.interviewcake.com/question/python/word-cloud

Find Duplicate Files »
Your friend copied a bunch of your files and put them in random places around your hard drive. Write a function to undo the damage.
https://www.interviewcake.com/question/python/find-duplicate-files
"""
