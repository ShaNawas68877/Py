import nltk
##nltk.download('words')
words = set(nltk.corpus.words.words())
sent = "Io andiamo to the beach with my amico"
sent = " ".join(w for w in nltk.wordpunct_tokenize(sent) if w.lower() in words or not w.isalpha())
print(sent)

##file1 = open("fourToFivePages.txt","r")
##print(file1.read())
