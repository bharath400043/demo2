## initializing the string
string = "I am a python programmer."
## finding all character exclusing spaces
chars = [char for char in string if char != " "]
print(chars)
## getting number of spaces using count method
spaces_count = string.count(' ')
## multiplying the space with spaces_count to get all the spaces at front of the ne
new_string = " " * spaces_count
## appending characters to the new_string
new_string += "".join(chars)
## priting the new_string
print(new_string)
