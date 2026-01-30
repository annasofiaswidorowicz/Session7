text =  "Hello World"
print(text)
text = 'Hello World 2'
print(text)
print(text[4]) #prints 4th letter of the text
print(len(text))
text = ""
print(len(text))

text = "Bob"
print(text[-1]) #prints the last character of the string
#numbers can be float (decimals) or intergers
print(text[6//3]) #with // it's interger division

#you can add 2 strings
s1 = "hello"
s2 = "bye"
print (s1+s2)
print (s1*4)

#string is iterable, you can use for over it
s1 = "Hello my name is Bob"
for c in s1:
    print(c)

s1 = "I like to give hi fives"
#print this string, but replace 'i' with 'y'
s1_new= ""
for c in s1:
    if c == "i":
        s1_new += "y"
    elif c == "I":
        s1_new += "Y"
    else:
        s1_new = s1_new + c
print(s1_new)