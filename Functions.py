
def say_hi():
    print("Hello User")

print("Top")
say_hi()
print("bottom")


def say_hi(name):
    print("Hello " + name)

say_hi("Steve")
say_hi("Mike")
say_hi("Don")


def say_hi(name, age):
    print("Hello " + name + ", you are " + age)

say_hi("Steve", "35")
say_hi("Mike", "42")
say_hi("Don", "56")