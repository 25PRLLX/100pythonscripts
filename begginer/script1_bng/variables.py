name = input("What's your name?")
length = len(name)
print(length)

## exercise ##
a = input("Basic")
b = input("Assembly")

c = a
a = b
b = c

print("a: " + a)
print("b: " + b)