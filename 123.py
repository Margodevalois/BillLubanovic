# Introducing Python. Modern Computing in Simple Packages.Bill Lubanovic

# PY FILLING

# # Ex.1-3 - print list with conditions
# years_list = [1993, 1994, 1995, 1996, 1997, 1998]
# print(years_list[3])
# print(max(years_list))

# # Ex.4-7 - change list
# things = ['mozzarella', 'cinderella', 'salmonella']
# things[1] = things[1].title()
# print(things)
# things[0] = things[0].upper()
# print(things)
# things.pop(2)
# print(things)

# # Ex.8,9 - change list
# suprise = ['Groucho', 'Chico', 'Harpo']
# suprise[-1] = suprise[-1].lower()[::-1].capitalize()
# #suprise[-1] = suprise[-1][::-1]
# #suprise[-1] = suprise[-1].capitalize()
# print(suprise)

# # Ex.10-14 - deals with dict
# e2f = {'dog': 'chien', 'cat': 'chat', 'walrus': 'morse'}
# print(e2f)
# print(e2f['walrus'])
# f2e = dict(e2f.items())
# print(f2e)
# keys = [k for k, v in f2e.items() if v == 'chien']
# print(keys)
# print(set(e2f))

# # Ex.15-18 - multilayers dict
# life = {'animals': {'cats': ['Henri', 'Grumpy', 'Lucy'],
#                     'octopi': {},
#                     'emus': {}},
#         'plants': {},
#         'other': {}}
# print(life.keys())
# print(life['animals'].keys())
# print(life['animals']['cats'])

# PY CRUST

# # Ex.1,2 - if, else, elif
# guess_me = 7
# start = 1
# # if guess_me < 7:
# #     print('too low')
# # elif guess_me > 7:
# #     print('too high')
# # else: print('just right')
# while start <= guess_me:
#     if start < guess_me:
#         print('too low')
#     else:
#     # elif start == guess_me:
#         print('found it!')
#         break
#     start += 1
# else:
#     if start > guess_me:
#         print

# # Ex.3 - for
# l1 = [3, 2, 1, 0]
# for i in l1:
#     print(i)

# # Ex.4 - list comprehensions
# l2 = [i for i in range(10) if i % 2 == 1]
# print(l2)

# # Ex.5 - dict comprehensions
# # s = range(10)
# squares = {s: pow(s, 2) for s in range(10)}
# print(squares)

# # Ex.6 - set comprehensions
# odd = {i for i in range(10) if i % 2 == 0}
# print(odd)

# # Ex.7 - generator comprehensions
# generator1 = [i for i in range(10)]
# for x in generator1:
#     print(x)
# print('Got', len(generator1))

# # Ex.8
# def good():
#     list = ['Harry', 'Ron', 'Hermione']
#     return list
# print(good())

# # Ex.9 - generators
# def get_odds():
#     output = []
#     for x in range(1, 10):
#      if x % 2 == 0:
#         output.append(x)
#     return output
# for i in get_odds():
#     if i == get_odds()[2]:
#         print(i)

# # Ex.10 - decorator
# def test(func):
#     def wrapper():
#         print('start of function func()')
#         func()
#         print('end, all good')
#     return wrapper
#
# @test
# def test1():
#     print('lll')
# test1()

# # Ex.12 - dict from lists by zip
# titles = ['Creature of habit', 'Crewel Fate']
# plots = ['A nun turns into a monster', 'A haunted yarn shop']
# print(dict(zip(titles, plots)))

#  OBJECTS AND CLASSES

# # Ex.1
# class Thing:
#     pass
#
# example = Thing()
# print(Thing)
# print(example)

# # Ex.2
# class Thing2:
#    letters = 'abc'
# print(Thing2.letters)

# # Ex.3
# class Thing3:
#     def __init__(self, letters):
#         self.letters = letters
#
# smth = Thing3()
# smth.letters = "xyz"
# print(smth.letters)

# # Ex. 4-7
# class Element:
#     def __init__(self, name, symbol, number):
#         self.name = name
#         self.symbol = symbol
#         self.number = number
#
#     def __str__(self):
#         return ('name=%s, symbol=%s, number=%s' %
#               (self.name, self.symbol, self.number))

# hydrogen = Element('Hydrogen', 'H', 1)
# print(hydrogen.name)

# D = {
#     'name': 'Hydrogen',
#     'symbol': 'H',
#     'number': 1
# }
# hydrogen = Element(D['name'], D['symbol'], D['number'])
# hydrogen = Element(**D)
# hydrogen.dump()

# # Ex.8 - modyfing Element
# class Element:
#     def __init__(self, name, symbol, number):
#         self.__name = name
#         self.__symbol = symbol
#         self.__number = number
#     @property
#     def name(self):
#         return self.__name
#     @property
#     def ymbol(self):
#         return self.__symbol
#     @property
#     def number(self):
#         return self.__number
#
#
# hydrogen = Element('Hydrogen', 'H', 1)
# print(hydrogen.name)

# # Ex.9
# class Bear:
#     def eats(self):
#         return 'berries'
# class Rabbit:
#     def eats(self):
#         return 'clover'
# class Octothorpe:
#     def eats(self):
#         return 'campers'
#
# B = Bear()
# R = Rabbit()
# O = Octothorpe()
#
# print(B.eats())
# print(R.eats())
# print(O.eats())

# # Ex.10
# class Laser:
#     def does(self):
#         return 'disintegrate'
#
# class Claw:
#     def does(self):
#         return 'crush'
#
# class SmartPhone:
#     def does(self):
#         return 'ring'
#
# class Robot:
#     def __init__(self):
#         self.laser = Laser()
#         self.claw = Claw()
#         self.smartphone = SmartPhone()
#     def does(self):
#         print(self.laser.does(), self.claw.does(), self.smartphone.does())
#
# R = Robot()
# print(R.does())

# # MANAGE WITH DATA

# # Ex.1 - unicode
# import unicodedata
# mystery = '\U0001f4a9'
# print(mystery)
# print(unicodedata.name(mystery))

# # Ex.2 - UTF-8
# pop_bytes = mystery.encode('utf-8')
# print(pop_bytes)

# # Ex.3 - decode
# pop_string = pop_bytes.decode('utf-8')
# print(pop_string)

# # Ex.4 - old style
# # R = 'roast beef', H = 'ham', H1 = 'head', C = 'clam' print('''My kitty cat likes %s, My kitty cat likes %s, My kitty cat fell on his %s, And now thinks he's a %s''' % (R, H, H1, C))
# poem = '''My kitty cat likes %s,
# My kitty cat likes %s,
# My kitty cat fell on his %s,
# And now thinks he's a %s'''
# args = ('roast beef', 'ham', 'head', 'clam')
# print(poem % args)

# # Ex. 5,6 - new style
# letter = ('''Dear {salutation} {name},
# Thank you for your letter. We are sorry that our {product} {verbed} in your {room}.
# Please note that it should never be used in a {room}, especially near any {animals}.
# Send us your receipt and {amount} for shipping and handling. We will send you
# another {product} that, in our tests, is {percent}% less likely to have {verbed}.
# Thank you for your support.
# Sincerely,
# {spokeman}
# {job_title}
# ''')
# response = {
#     "salutation": 'fff',
#     'name': 'ggg',
#     'product': 'ddd',
#     'verbed': 'rrr',
#     'room': 'qqq',
#     'animals': 'eee',
#     'amount': '444',
#     'percent': '3',
#     'spokeman': 'ttt',
#     'job_title': 'yyy'
# }
# print(letter.format(**response))

# # Ex.7-11 - regular expressions
# import re
# mammoth = '''We have seen the Queen of cheese,
# Laying quietly at your ease,
# Gently fanned by evening breeze --
# Thy fair form no flies dare seize.
# All gaily dressed soon you'll go
# To the great Provincial Show,
# To be admired by many a beau
# In the city of Toronto.
# Cows numerous as a swarm of bees --
# Or as the leaves upon the trees --
# It did require to make thee please,
# And stand unrivalled Queen of cheese.
# May you not receive a scar as
# We have heard that Mr. Harris
# Intends to send you off as far as
# The great World's show at Paris.
# Of the youth -- beware of these --
# For some of them might rudely squeeze
# And bite your cheek; then songs or glees
# We could not sing o' Queen of cheese.
# We'rt thou suspended from baloon,
# You'd cast a shade, even at noon;
# Folks would think it was the moon
# About to fall and crush them soon.'''
# # find all words start from c
# print(re.findall(r'\bc\w*', mammoth))
# # find all 4-letters words start from c
# print(re.findall(r'\bc...\b', mammoth))
# print(re.findall(r'\bc\w{3}\b', mammoth))
# # print all words ens with r
# print(re.findall(r'\b\w*r\b', mammoth))
# # all words with three vowels one by one
# print(re.findall(r'\b\w*[aeiou]{3}[^aeiou\s]*\w*\b', mammoth))

#  Ex.12
import binascii
hex_str = '47494638396101000100800000000000ffffff21f9' + '0401000000002c000000000100010000020144003b'
gif = binascii.unhexlify(hex_str)
print(len(gif))
print(gif[:6] == b'GIF89a')
import struct
width, height = struct.unpack('<HH', gif[6:10])
print(width, height)

