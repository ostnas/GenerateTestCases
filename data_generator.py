import rstr
import string
import numpy
import timeit
import random


# a = rstr.rstr('ABC', include='&')
# print(a)
#
#
# b= rstr.rstr(string.digits, exclude='5')
# print(b)
#
# c = rstr.rstr(['A', 'B', 'C'], 8, include = ['@'], exclude=('C',))
# print(c)
#
# d = rstr.punctuation(exclude=('!','@','#','$','%','^','&','*','(',')','<','>'))
# print(d)
#
# e= rstr.rstr(string.ascii_letters, 1)
# print(e)

valid_chars1 = ['latin_low', 'latin_up', 'cyrillic_low', 'cyrillic_up', 'digits', '%', '-']
valid_chars2 = ['T', 't', 'J', 'j', 'digits']
invalid_chars = []
# included_list=[string.ascii_letters]
excluded_list=['A','B','C']
maxlength = 100
chars_list = ['E','I','*',string.digits]
if maxlength is not None:
    f = rstr.rstr(chars_list, start_range=1, end_range=min(10, maxlength))


ranges = []

# str2 = ''
# print(chr(1040))
# print(chr(1071))
# print(chr(1072))
# print(chr(1103))

TEST1 ='''
def test2():
    str2 = ''
    for i in range (100):
        new_char=numpy.random.randint(1040, 1104)
        str2 += str(chr(new_char))
    print(str2)'''

# maxlength = 5
# p = numpy.random.randint(1040, 1104)
# print(p)
# for i in range(len(p)):
#     p[i] = chr(p[i])
# t = rstr.rstr(numpy.random.randint(1040, 1104), start_range=1, end_range=min(100, maxlength))
# print(t)

cyrillic_list = ''
for i in range(1040, 1104):
    cyrillic_list += str(chr(i))
print(cyrillic_list)
f = rstr.rstr(cyrillic_list, start_range=1, end_range=100)
print(f)
