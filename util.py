import msvcrt as m
import os

def clear(): return os.system('cls')

def wait():
    m.getch()