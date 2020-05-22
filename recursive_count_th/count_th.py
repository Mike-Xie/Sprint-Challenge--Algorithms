'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word: str, substring: str = "th"):
    # base case nothing
    if word == "":
    	return 0
    # seperate into head and tail
    # recursively call on tail
    # increment count by len of substr if found and consume next part
    if word[:len(substring)] == substring:
    	return 1 + count_th(word[len(substring):])
    # not increment count and consume next part
    else:
    	return 0 + count_th(word[1:])