#!/usr/bin/env python3

import random


class RandomCredentials:
    # sex-neutral surnames
    surnames = ['Nowak', 'Wójcik', 'Woźniak', 'Mazur', 'Krawczyk']
    cities = ['Warsaw', 'Cracow', 'Łódź']

    @staticmethod
    def phone():
        beginning = '7' + '{:02d}'.format(random.randint(0, 99))
        middle = '{:03d}'.format(random.randint(0, 999))
        end = '{:03d}'.format(random.randint(0, 999))
        return '-'.join([beginning, middle, end])

    @staticmethod
    def zipcode():
        beginning = '{:02d}'.format(random.randint(0, 99))
        end = '{:03d}'.format(random.randint(0, 999))
        return '{}-{}'.format(beginning, end)


class RandomMale():
    __names = ['Adam', 'Bartłomiej', 'Cezary', 'Dawid', 'Eugeniusz']
    __surnames = ['Kowalski', 'Wiśniewski', 'Dąbrowski']

    def __init__(self):
        self.name = random.choice(self.__names)
        self.phone = RandomCredentials.phone()
        self.zipcode = RandomCredentials.zipcode()
        self.surname = random.choice(
                self.__surnames + RandomCredentials.surnames)
        self.city = random.choice(RandomCredentials.cities)

    def say_hi(self):
        print('My name is {} {}.'.format(self.name, self.surname))
        print('I live in {} ({}).'.format(self.city, self.zipcode))
        print('Call me: {}.'.format(self.phone))


def main():
    guy = RandomMale()
    guy.say_hi()


if __name__ == '__main__':
    main()
