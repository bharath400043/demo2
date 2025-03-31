"""
The expandtabs() method returns a copy of string with all tab characters '\t' replaced with whitespace characters until the next multiple of tabsize parameter.
Syntax: string.expandtabs(tabsize)
* The expandtabs() takes an integer tabsize argument. The default tabsize is 8.
* The expandtabs() returns a string where all '\t' characters are replaced with whitespace characters until the next multiple of tabsize parameter.

"""
# expandtabs() With no Argument
str = 'xyz\t12345\tabc'

# no argument is passed
# default tabsize is 8
result = str.expandtabs()
print(result)
print(len(result))

# expandtabs() With Different Argument
str = "xyz\t12345\tabc"
print('Original String:', str)

# tabsize is set to 2
print('Tabsize 2:', str.expandtabs(2))
print(len(str.expandtabs(2)))

# tabsize is set to 3
print('Tabsize 3:', str.expandtabs(3))
print(len(str.expandtabs(3)))

# tabsize is set to 4
print('Tabsize 4:', str.expandtabs(4))
print(len(str.expandtabs(4)))

# tabsize is set to 5
print('Tabsize 5:', str.expandtabs(5))
print(len(str.expandtabs(5)))

# tabsize is set to 6
print('Tabsize 6:', str.expandtabs(6))
print(len(str.expandtabs(6)))

st = "i\tlove\tgfg"
# using expandtabs to insert spacing
print("Modified string using default spacing: ")
# print(st.expandtabs(10.5))    # TypeError: integer argument expected, got float
