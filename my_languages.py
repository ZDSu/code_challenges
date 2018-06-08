"""
https://www.codewars.com/kata/mylanguages/train/python


"""

def my_languages(results):
    final = {}
    for k,v in results.items():
        if results[k] >= 60:
            final[k] = v
    return sorted(final.items())