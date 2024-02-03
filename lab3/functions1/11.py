def check(word):
    if word == word[::-1]:
        return True
    else:
        return False


word = input()
print(check(word))