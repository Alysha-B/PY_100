foo = 'bar'

def set_foo():
    foo = 'qux'

set_foo()
print(foo)
# What does this program print? Why?
# prints bar
# Because the variable foo is defined globaly
# foo created within the local scope of the variable doesn't print

print()
foo = 'bar'

def set_foo():
    foo = 'qux'
    print(foo)

set_foo()
print(foo)
# This would print both variable values, one from the local scope
# The other from the global scope