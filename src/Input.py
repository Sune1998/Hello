import sys

print("hello what is your name")

name = sys.stdin.readline()

print("hello", name)

print("enter your age")

age = int(sys.stdin.readline())
if age > 18:
    print("welcome")
else:
    print("you're not old enough")
