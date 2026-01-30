s = "cat"
s = "r" + s[1:] #strings are immutable, so we create a new one to change it
print(s)

s1 = "bob"
s2 = "banana"
print(s1 < s2)

s1 = "BOB"
s2 = "bob"
print(s1 > s2)

#in operator checks if a string is part of another
print("ana" in "banana")
print("Ana" in "banana")
