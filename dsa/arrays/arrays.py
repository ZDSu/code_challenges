# anagram check
def anagram(s1,s2):
    s1 = s1.strip()
    s2 = s2.strip()
    chars = {}

    for char in s1:
        if char != ' ':
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1

    for char in s2:
        if char != ' ':
            if char in chars:
                chars[char] -= 1
                if chars[char] == 0:
                    del chars[char]
            else:
                return False

    return not chars 


# array pair sum
def pair_sum(arr,k):
    seen = set()
    pairs = []
    for num in arr:
        temp = k - num
        if temp in seen:
            pair = sorted((num, temp))
            if pair not in pairs:
                pairs.append(pair)
        seen.add(num)
    return len(pairs)


# find the missing element
def finder(arr1,arr2):
    arr1.sort()
    arr2.sort()

    for i in range(len(arr2)):
        if arr1[i] != arr2[i]:
            return arr1[i]
    return arr1[-1]


# largest continuous sum
def large_cont_sum(arr):
    largest = current = arr[0]
    for num in arr[1:]:
        current = max(current + num, num)
        # if current > largest:
        #     largest = current
        largest = max(largest, current)
    return largest


# sentence reversal
def rev_word(s):
    # return (' ').join(reversed(s.split()))

    word = ''
    words = []
    for char in s:
        if char != ' ':
            word += char
        else:
            if word:
                words.append(word)
            word = ''
    if word:
        words.append(word)

    result = ''
    for each in words[::-1]:
        result += each + ' '
    return result[:-1]


# string compression
def compress(s):
    if not s:
        return s
    count = 1
    curr = s[0]
    result = ''

    for char in s[1:]:
        if char == curr[0]:
            count += 1
        else:
            result += curr + str(count)
            count = 1
            curr = char
    result += curr + str(count)
    return result


# unique characters in string
def uni_char(s):
    chars = set()
    for char in s:
        if char in chars:
            return False
        chars.add(char)
    return True