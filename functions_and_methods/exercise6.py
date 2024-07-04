# What does the following code print?
def scream(words):
    words = words + '!!!!'
    return
    print(words)

scream('Yipeee')
# Nothing, return terminates the function before print
# At first I thought it would return an error, but it doesn't