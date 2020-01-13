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
    dark = "ciemny"


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


Attributes = [["Płec", "mężczyzna", "kobieta"],
              ["Skóra", "biały", "mulat", "czarny"],
              ["Włosy", "długie", "krótkie", "łysy"],
              ["Kolor_włosów", "rudy", "siwy", "blond", "ciemny"],
              ["Oczy", "piwne", "niebieskie"],
              ["Okulary", "ma", "nie ma"],
              ["Zarost", "wąsy", "broda", "broda i wąsy", "brak"],
              ["Czapka", "ma", "nie ma"],
              ["Akcseroia_na_głowie", "ma", "nie ma"]]
# , "Skóra", "Włosy", "Kolor włosów", "Oczy", "Okulary", "Kolczyki", "Zarost", "Czapka", "Akcesoria na włosach"]
