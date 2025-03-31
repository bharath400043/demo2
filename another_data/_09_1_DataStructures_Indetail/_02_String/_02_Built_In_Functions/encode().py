"""
The encode() method encodes the string, using the specified encoding. If no encoding is specified, UTF-8 will be used.
Syntax: string.encode(encoding=encoding, errors=errors)
* encoding - Optional. A String specifying the encoding to use. Default is UTF-8
* errors - Optional. A String specifying the error method. Legal values are:
'backslashreplace'	- uses a backslash instead of the character that could not be encoded
'ignore'	- ignores the characters that cannot be encoded
'namereplace'	- replaces the character with a text explaining the character
'strict'	- Default, raises an error on failure
'replace'	- replaces the character with a questionmark
'xmlcharrefreplace'	- replaces the character with an xml character
"""

# Encode to Default Utf-8 Encoding
# unicode string
string = 'pythön!'
# print string
print('The string is:', string)
# default encoding to utf-8
string_utf = string.encode()
# print result
print('The encoded version is:', string_utf)

# Encoding with error parameter
# unicode string
string = 'pythön!'
# print string
print('The string is:', string)
# ignore error
print('The encoded version (with ignore) is:', string.encode("ascii", "ignore"))
# replace error
print('The encoded version (with replace) is:', string.encode("ascii", "replace"))

txt = "My name is Ståle"

print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))
