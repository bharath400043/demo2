"""The join() string method returns a string by joining all the elements of an iterable,
separated by a string separator
*The join() method provides a flexible way to create strings from iterable objects.
It joins each element of an iterable (such as list, string, and tuple) by a string separator
(the string on which the join() method is called) and returns the concatenated string.
* The join() method takes an iterable (objects capable of returning its members one at a time) as its parameter.
** In this join() method takes a parameter that one is iterable means in the paranthasis string or sequence is iterable
** The join() method returns a string created by joining the elements of an iterable by string separator
** If the iterable contains any non-string values, it raises a TypeError exception
Syntax : string.join(iterable) """

s1 = "yogi"
s2 = "123"

print("s1.join(s2):", s1.join(s2))  # each element of s2 is seperated by s1 and here s2 is iterable
print("s2.join(s1):", s2.join(s1))  # each element of s1 is seperated by s2

list1 = ["python", "ruby", "java"]
s = ":"
print("s.join(list1): ", s.join(list1))
# print("list1.join(s): ", list1.join(s))   IT'S SHOW ERROR BECAUSE LIST OBJECT HAS NO ATTRIBUTE JOIN

set1 = {"yogi", "swaroop", "ramu"}
s1 = "&"
print("s1.join(set1): ", s1.join(set1))

# .join() with dictionaries
test = {'mat': 1, 'that': 2}
s = '-->'
# joins the keys only
print(s.join(test))

test = {1: 'mat', 2: 'that'}
s = ', '
# this gives error since key isn't string
# print(s.join(test))