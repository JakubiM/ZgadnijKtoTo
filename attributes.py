from enum import Enum


class Sex(Enum):
    male = "mężczyzna"
    female = "kobieta"


class Skin(Enum):
    white = "biały"
    mulatto = "mulat"
    black = "czarny"


class Hair(Enum):
    long = "długie"
    short = "krótkie"
    bald = "łysy"


class HairColour(Enum):
    red = "rudy"
    grey = "siwy"
    blond = "blond"
    dark = "brązowy"
    black = "czarny"


class Eyes(Enum):
    brown = "piwne"
    blue = "niebieskie"


class Glasses(Enum):
    yes = "ma"
    no = "nie ma"


class Earrings(Enum):
    yes = "ma"
    no = "nie ma"


class Beard(Enum):
    moustache = "wąsy"
    beard = "broda"
    beard_moustache = "broda i wąsy"
    none = "brak"


class Cap(Enum):
    yes = "ma"
    no = "nie ma"


class HairAccessories(Enum):
    yes = "ma"
    no = "nie ma"

class Nose(Enum):
    big = "duży"
    small = "mały"

Att = [('Sex', 'Płeć'),
       ('Skin', 'Kolor skóry'),
       ('Hair', 'Włosy'),
       ('HairColour', 'Kolor włosów'),
       ('Eyes', 'Kolor oczu'),
       ('Glasses', 'Okulary'),
       ('Earrings', 'Kolczyki'),
       ('Beard', 'Zarost'),
       ('Cap', 'Czapka'),
       ('HairAccessories', 'Akcesoria na glowie'),
       ('Nose', 'Nos')
       ]
attdict = {
    'Sex': 'Płeć',
    'Skin': 'Kolor skóry',
    'Hair': 'Włosy',
    'HairColour': 'Kolor włosów',
    'Eyes': 'Kolor oczu',
    'Glasses': 'Okulary',
    'Earrings': 'Kolczyki',
    'Beard': 'Zarost',
    'Cap': 'Czapka',
    'HairAccessories': 'Akcesoria na glowie',
    'Nose' : 'Nos',
    '': ''
}
reqdict = {
    'yes': 'Tak',
    'no' : 'Nie',
    '': ''
}

typdict = {
    'male' : 'mężczyzna',
    'female' : 'kobieta',
    'white' : 'biały',
    'mulatto' : 'mulat',
    'black' : 'czarny',
    'long': 'długie',
    'short' : 'krótkie',
    'bald' : 'łysy',
    'red' : 'rudy',
    'grey' : 'siwy',
    'blond' : 'blond',
    'dark' : 'brązowe',
    'brown' : 'piwne',
    'blue' : 'niebieskie',
    'yes' : 'ma',
    'no' : 'nie ma',
    'moustache' : 'wąsy',
    'beard' : 'broda',
    'beard_moustache' : 'broda i wąsy',
    'none' : 'brak',
    'big' : 'duży',
    'small' : 'mały',
    '': ''
}