# https://leetcode.com/problems/longest-word-in-dictionary/description/
# https://leetcode.com/articles/longest-word-in-dictionary/


class Solution:
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        result = ''
        for word in words:
            if word[:-1] in words:
                if len(word) > len(result):
                    result = word
                elif len(word) == len(result):
                    result = sorted([word, result])[0]
        return result


# test cases
# ["yo","ew","fc","zrc","yodn","fcm","qm","qmo","fcmz","z","ewq","yod","ewqz","y"] returns "yodn"
