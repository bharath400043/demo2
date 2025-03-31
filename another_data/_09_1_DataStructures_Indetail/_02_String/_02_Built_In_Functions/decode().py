"""
decode(): This method is used to convert from one encoding scheme, in which argument string is encoded to the desired encoding scheme.
This works opposite to the encode. It accepts the encoding of the encoding string to decode it and returns the original string.
Syntax: decode(encoding, error)
* encoding : Specifies the encoding on the basis of which decoding has to be performed.
* error : Decides how to handle the errors if they occur, e.g ‘strict’ raises Unicode error in case of exception and ‘ignore’ ignores the errors occurred.
* Returns : Returns the original string from the encoded string.

"""

str = "geeksforgeeks"

# encoding string
str_enc = str.encode('ascii', 'strict')

# printing the encoded string
print("The encoded string in base64 format is : ")
print(str_enc)

# printing the original decoded string
print("The decoded string is : ")
print(str_enc.decode('ascii', 'strict'))