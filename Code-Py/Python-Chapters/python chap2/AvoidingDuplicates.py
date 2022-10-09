word = input("please enter your words")
words = []
while word != "":
    if word not in words:
            words.append(word)
    word = input("please enter your words")
for word in words:
    print(word)
