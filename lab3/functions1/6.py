def reverse_sentence(sentence):
    return " ".join(sentence.split()[::-1])

sent = input()
sent = str(sent)
print(reverse_sentence(sent))