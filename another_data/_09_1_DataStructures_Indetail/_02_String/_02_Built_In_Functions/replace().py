"""
The replace() method returns a copy of the string where all occurrences of a substring is replaced with another substring.
Syntax: str.replace(old, new [, count])
old - old substring you want to replace
new - new substring which will replace the old substring
count (optional) - the number of times you want to replace the old substring with the new substring
* If count is not specified, the replace() method replaces all occurrences of the old substring with the new substring.
* The replace() method returns a copy of the string where the old substring is replaced with the new substring. The original string is unchanged.
If the old substring is not found, it returns the copy of the original string.
"""

song = 'cold, cold heart'
# replacing 'cold' with 'hurt'
print(song.replace('cold', 'hurt'))

song = 'Let it be, let it be, let it be, let it be'
# replacing only two occurences of 'let'
print(song.replace('let', "don't let", 2))

song = 'cold, cold heart'
replaced_song = song.replace('o', 'e')
# The original string is unchanged
print('Original string:', song)
print('Replaced string:', replaced_song)

song = 'let it be, let it be, let it be'
# maximum of 0 substring is replaced
# returns copy of the original string
print(song.replace('let', 'so', 0))

str = "this is string example....wow!!! this is really string"
print (str.replace("is", "was"))
print (str.replace("is", "was", 3))