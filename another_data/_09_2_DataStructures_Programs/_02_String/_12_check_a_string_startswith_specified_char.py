
# Using Built-in-function startswith
text = "Python is easy to learn."

result = text.startswith('is easy')
# returns False
print(result)

result = text.startswith('Python is ')
# returns True
print(result)

# Without built-in
text = "yogeswar"
def check_startswith(msg):

    if text[0] == "y":
        print(" text startswith y: ", True)
    else:
        print(" text startswith y: ", False)

check_startswith(text)
