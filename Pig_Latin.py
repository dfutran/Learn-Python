#David Futran
#Last Modified 04/29/15
#Pig Latin Generator

a="go"
while(a):
    word = input("Enter a word and it will be translated into pig latin: ")
    temp = word
    if word[0] in "aeiou":
        word = word + "way"
    else:
        word= word[1:]+word[0]+"ay"
    print (temp," in pig latin is: ",word)
    a = input("enter 'go' to continue or press enter to quit: ")
print("Good bye!")
