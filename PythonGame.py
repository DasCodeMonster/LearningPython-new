import pygame


class Player:
    def __init__(self, name, age):
        name: str
        # assert isinstance(name, str)
        self.Name = name
        assert isinstance(age, int)
        self.Age = age


def main():
    Player(4, 4)
    Player()
