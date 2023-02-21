# Introducing Python. Modern Computing in Simple Packages.Bill Lubanovic
# INTRODUCTION

# Ex.1-3 - print list with conditions
# years_list = [1993, 1994, 1995, 1996, 1997, 1998]
# print(years_list[3])
# print(max(years_list))
# # 4-7
# things = ['mozzarella', 'cinderella', 'salmonella']
# things[1] = things[1].title()
# print(things)
# things[0] = things[0].upper()
# print(things)
# things.pop(2)
# print(things)
# # 8,9
# suprise = ['Groucho', 'Chico', 'Harpo']
# suprise[-1] = suprise[-1].lower()[::-1].capitalize()
# #suprise[-1] = suprise[-1][::-1]
# #suprise[-1] = suprise[-1].capitalize()
# print(suprise)
# # 10-14
# e2f = {'dog': 'chien', 'cat': 'chat', 'walrus': 'morse'}
# print(e2f)
# print(e2f['walrus'])
# f2e = dict(e2f.items())
# print(f2e)
# keys = [k for k, v in f2e.items() if v == 'chien']
# print(keys)
# print(set(e2f))
# # 15-18
# life = {'animals': {'cats': ['Henri', 'Grumpy', 'Lucy'],
#                     'octopi': {},
#                     'emus': {}},
#         'plants': {},
#         'other': {}}
# print(life.keys())
# print(life['animals'].keys())
# print(life['animals']['cats'])

# 1,2
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
#         print('oops!')
#
# # 3 цикл for
# l1 = [3, 2, 1, 0]
# for i in l1:
#     print(i)
#
# # 4 включение списка
# l2 = [i for i in range(10) if i % 2 == 1]
# print(l2)
#
# # 5 включение словаря
# # s = range(10)
# squares = {s: pow(s, 2) for s in range(10)}
# print(squares)
#
# # 6 включение множества
# odd = {i for i in range(10) if i % 2 == 0}
# print(odd)
#
# # 7 включение генератора
#
# generator1 = [i for i in range(10)]
# for x in generator1:
#     print(x)
# print('Got', len(generator1))
#
# # 8
# def good():
#     list = ['Harry', 'Ron', 'Hermione']
#     return list
# print(good())
#
# # 9
# def get_odds():
#     output = []
#     for x in range(1, 10):
#      if x % 2 == 0:
#         output.append(x)
#     return output
# for i in get_odds():
#     if i == get_odds()[2]:
#         print(i)
#
# # 10 определение декоратора
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
#
# # 11 определение исключения
# # class OopsException(Exception):
# #     pass
# #
# #
# # words = ['lll', 'mmm', 'nnn']
# # for w in words:
# #     if w == 'nnn':
# #         raise OopsException(w)
# # try:
# #     raise OopsException('oooo')
# # except OopsException as exc:
# #     print(exc)
#
# # 12 с помощью zip создаем словрь из списков
# titles = ['Creature of habit', 'Crewel Fate']
# plots = ['A nun turns into a monster', 'A haunted yarn shop']
# print(dict(zip(titles, plots)))

# class 1
# class Thing:
#     pass
#
# example = Thing()
# print(Thing)
# print(example)
#
# # class 2
# class Thing2:
#    letters = 'abc'
#
# print(Thing2.letters)
#
# # class 3
# class Thing3:
#     def __init__(self, letters):
#         self.letters = letters
#
# smth = Thing3()
# smth.letters = "xyz"
# print(smth.letters)

# class 4, 5, 6, 7
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

# 8
class Element:
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number
    @property
    def name(self):
        return self.__name
    @property
    def ymbol(self):
        return self.__symbol
    @property
    def number(self):
        return self.__number


hydrogen = Element('Hydrogen', 'H', 1)
print(hydrogen.name)

# 9
class Bear:
    def eats(self):
        return 'berries'
class Rabbit:
    def eats(self):
        return 'clover'
class Octothorpe:
    def eats(self):
        return 'campers'

B = Bear()
R = Rabbit()
O = Octothorpe()

print(B.eats())
print(R.eats())
print(O.eats())

# 10
class Laser:
    def does(self):
        return 'disintegrate'

class Claw:
    def does(self):
        return 'crush'

class SmartPhone:
    def does(self):
        return 'ring'

class Robot:
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.smartphone = SmartPhone()
    def does(self):
        print(self.laser.does(), self.claw.does(), self.smartphone.does())

R = Robot()
print(R.does())