from dataclasses import dataclass
import os
from pathlib import Path
import unicodedata
from turtle import Pen, Screen

PKG_PATH = Path(__file__).parent
screen = Screen()

emojis = (
    # Unicode emojis de animais
#     0     1     2     3     4     5     6     7     8     9
    '🐶', '🐱', '🐭', '🐹', '🐰', '🦊', '🐻', '🐼', '🐨', '🐯', # Linha 0
    '🦁', '🐷', '🐸', '🐵', '🐔', '🐧', '🐦', '🐤', '🦆', '🦅', # Linha 1
    '🦉', '🦇', '🐺', '🦄', '🐝', '🐛', '🐌', '🐞', '🐜', '🦂', # Linha 2
    '🦟', '🦗', '🐢', '🐍', '🦎', '🦖', '🦕', '🐙', '🦑', '🦐', # Linha 3
    '🦞', '🦀', '🐡', '🐠', '🐟', '🐬', '🐳', '🐋', '🐊', '🐅', # Linha 4
    '🐆', '🦓', '🦍', '🦧', '🐘', '🦛', '🦏', '🐪', '🐫', '🦒', # Linha 5
    '🦘', '🦬', '🐃', '🐄', '🐎', '🐖', '🐏', '🐑', '🦙', '🐐', # Linha 6
    '🦌', '🐕', '🐩', '🦮', '🐈', '🐓', '🦃', '🦤', '🦚', '🦜', # Linha 7
    '🦢', '🦩', '🐇', '🐁', '🐀', '🦔'                          # Linha 8
)

emojis_names = tuple([unicodedata.name(emoji).lower() for emoji in emojis])
#emoji_animal = dict(zip(emojis_names, emojis))

emoji_animal = {
    'ant': '🐜',
    'chick': '🐤',
    'camel': '🐫',
    'bat': '🦇',
    'bird': '🐦',
    'bison': '🦬',
    'blowfish': '🐡',
    'bug': '🐛',
    'cat': '🐈',
    'cow': '🐄',
    'crab': '🦀',
    'cricket': '🦗',
    'crocodile': '🐊',
    'deer': '🦌',
    'dodo': '🦤',
    'dog': '🐕',
    'dolphin': '🐬',
    'dromedary': '🐪',
    'duck': '🦆',
    'eagle': '🦅',
    'elephant': '🐘',
    'fish': '🐟',
    'flamingo': '🦩',
    'giraffe': '🦒',
    'goat': '🐐',
    'gorilla': '🦍',
    'hedgehog': '🦔',
    'hippopotamus': '🦛',
    'honeybee': '🐝',
    'horse': '🐎',
    'kangaroo': '🦘',
    'ladybeetle': '🐞',
    'leopard': '🐆',
    'lizard': '🦎',
    'llama': '🦙',
    'lobster': '🦞',
    'mosquito': '🦟',
    'mouse': '🐁',
    'octopus': '🐙',
    'orangutan': '🦧',
    'owl': '🦉',
    'parrot': '🦜',
    'peacock': '🦚',
    'penguin': '🐧',
    'pig': '🐖',
    'poodle': '🐩',
    'rabbit': '🐇',
    'ram': '🐏',
    'rat': '🐀',
    'rhinoceros': '🦏',
    'rooster': '🐓',
    'sauropod': '🦕',
    'scorpion': '🦂',
    'sheep': '🐑',
    'shrimp': '🦐',
    'snail': '🐌',
    'snake': '🐍',
    'squid': '🦑',
    'swan': '🦢',
    't-rex': '🦖',
    'tiger': '🐅',
    'turkey': '🦃',
    'turtle': '🐢',
    'buffalo': '🐃',
    'whale': '🐋'
 }

animal_names = [
    'ant', 'chick', 'camel', 'bat', 'bird', 'bison', 'blowfish',
    'bug', 'cat', 'cow', 'crab', 'cricket', 'crocodile', 'deer',
    'dodo', 'dog', 'dolphin', 'dromedary', 'duck', 'eagle', 'elephant',
    'fish', 'flamingo', 'giraffe', 'goat', 'gorilla', 'hedgehog', 'hippopotamus',
    'honeybee', 'horse', 'kangaroo', 'ladybeetle', 'leopard', 'lizard', 'llama',
    'lobster', 'mosquito', 'mouse', 'octopus', 'orangutan', 'owl', 'parrot',
    'peacock', 'penguin', 'pig', 'poodle', 'rabbit', 'ram', 'rat',
    'rhinoceros', 'rooster', 'sauropod', 'scorpion', 'sheep', 'shrimp', 'snail',
    'snake', 'squid', 'swan', 't-rex', 'tiger', 'turkey', 'turtle',
    'buffalo', 'whale'
]

class Animal:
    def __init__(self, name: str):
        assert name in animal_names, f'Animal {name} not found.'
        self._name: str = name
        self._left_shape: str = f'_{name}.gif'
        self._right_shape: str = f'{name}_.gif'
        self._emoji: str = emoji_animal.get(name)
        self._pen: Pen = Pen()
        self._load_img()

    def _load_img(self):
        cwd: str = os.getcwd()
        os.chdir(PKG_PATH/'images'/'72')
        screen.register_shape(self._left_shape)
        screen.register_shape(self._right_shape)
        os.chdir(cwd)
        self.left()

    def left(self):
        self._pen.shape(self._left_shape)

    def right(self):
        self._pen.shape(self._right_shape)

    def __str__(self):
        return f'{self.emoji} - {self.name}'

    def __repr__(self):
        return self.__str__()
    