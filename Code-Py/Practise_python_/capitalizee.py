#Exercise 89 : Capitalize it

def capitalize(text):
    result = text.upper()
    return result
def main():
    text = str(input("Enter the text :"))
    capitalized = capitalize(text)
    print(capitalized)
main()
