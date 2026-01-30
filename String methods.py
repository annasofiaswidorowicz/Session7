print(dir("x")) #all methods that exist for strings
print(help("x".capitalize))
s = "bob ATE piZZA"
print(s.capitalize())
print(s.count("A"))
s = "banana"
print(s.count("ana"))
print(s.find("ana", 2))
#replace string inside string
print(s.replace("ana", "BOB"))
s = "I, like: to go out!"
print(s.split(" "))
punct = ",.!:"
for c in punct:
    s = s.replace(c, "")
print(s.split())
