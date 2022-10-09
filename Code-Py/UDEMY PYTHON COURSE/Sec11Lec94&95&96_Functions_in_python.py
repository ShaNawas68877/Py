####def python_food():
####    print("spam and eggs")
####
#####call the function
####python_food()
######print(python_food())#prints spam and eggs and none because it has no arguments
####
##
##def python_food():
##    width=80
##    text = "spam and eggs"
##    left_margin =(width - len(text)) // 2
##    print(" " * left_margin, text)
##
##
##def centre_text(*txt):#txt is a parameter which is a variable
##    txt = str(txt)#changing 12 into str
##    left_margin =(80 - len(txt)) // 2
##    print(" " * left_margin, txt)
##    
##    
###call the function
###python_food()
##centre_text("spam and eggs")#value of parameter is an argument
##centre_text("spam, spam and eggs", 15, "quite", "nicely")
##centre_text(12)#will give an error because it has no len as it is an integer
##centre_text("spam, spam, spam and spam")
##
###*parameter IN THE FUNCTION DEFINITION HELPS US TO PASS AS MANY ARGUMENTS AS WE WANT 

####
####def centre_txt(*args, sep=' ', end='\n', file=None, flush=False):
####    txt = ""
####    for arg in args:
####        txt += str(arg) + sep
####    left_margin = (80 - len(txt)) // 2
####    print(" " * left_margin, txt, end=end, file=file, flush=flush)
####    
####    
####centre_text("spam and eggs")#value of parameter is an argument
####centre_text("spam, spam and eggs")
####centre_text(12)#will give an error because it has no len as it is an integer
####centre_text("spam, spam, spam and spam")
####
####centre_text("first", "second", 3, 4, "spam", sep=":")
####print()


#Lecture 96
def python_food():
    width=80
    text = "spam and eggs"
    left_margin =(width - len(text)) // 2
    print(" " * left_margin, text)


def centre_text(*args, sep=' ', file=):
    txt = ""
    for arg in args:
        txt += str(arg) + sep
    left_margin = (80 - len(txt)) // 2
    return " " * left_margin + txt
    
#with open("centred", mode='w') as centred_file:
##print(centre_text("spam and eggs"))#value of parameter is an argument
##print(centre_text("spam, spam and eggs"))
##print(centre_text(12))#will give an error because it has no len as it is an integer
##print(centre_text("spam, spam, spam and spam"))
##
##print(centre_text("first", "second", 3, 4, "spam", sep=":"))

with open("menu", "w") as menu:
    s1 = centre_text("spam and eggs")#value of parameter is an argument
    print(s1, file=menu)
    s2 = centre_text("spam, spam and eggs")
    print(s2, file=menu)
    print(centre_text(12), file=menu)#will give an error because it has no len as it is an integer
    print(centre_text("spam, spam, spam and spam"), file=menu)
    s5 = centre_text("first", "second", 3, 4, "spam", sep=":")
    print(s5, file=menu)


print("="+ str(12*3))
print(sorted(["b","d","c","a"]))
