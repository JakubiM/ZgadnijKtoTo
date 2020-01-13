import attributes


class Character:

    def __init__(self, name, sex, skin, hair, hairclr, eyes, glasses, ear, beard, cap, hairacc):

        self.Sex = sex
        self.Skin = skin
        self.Hair = hair
        self.HairColour = hairclr
        self.Eyes = eyes
        self.Glasses = glasses
        self.Earrings = ear
        self.Beard = beard
        self.Cap = cap
        self.HairAccessories = hairacc
        self.name = name
        self.visibility = True
        self.filename = "img/{}.png".format(self.name)





Adam = Character("Adam", "mężczyzna", "biały", "krótkie", "rudy", "niebieskie", "ma", "nie ma", "brak", "nie ma", "nie ma")
Agnieszka = Character("Agnieszka", "kobieta", "biały", "długie", "ciemny", "piwne", "nie ma", "nie ma", "brak", "ma", "nie ma")
Andrzej = Character("Andrzej", "mężczyzna", "czarny", "krótkie", "rudy", "piwne", "nie ma", "nie ma", "brak", "nie ma", "nie ma")
Ania = Character("Ania", "kobieta", "biały", "długie", "ciemny", "piwne", "nie ma", "ma", "brak", "nie ma", "ma")
Artur = Character("Artur", "mężczyzna", "mulat", "krótkie", "siwy", "piwne", "ma", "nie ma", "brak", "nie ma", "nie ma")
Daniel = Character("Daniel", "mężczyzna", "mulat", "krótkie", "ciemny", "piwne", "nie ma", "nie ma", "wąsy", "ma", "nie ma")
Grzes = Character("Grześ", "mężczyzna", "mulat", "długie", "blond", "piwne", "nie ma", "nie ma", "brak", "nie ma", "ma")
Iwona = Character("Iwona", "kobieta", "mulat", "długie", "rudy", "piwne", "nie ma", "ma", "brak", "ma", "nie ma")
Jan = Character("Jan", "mężczyzna", "mulat", "krótkie", "ciemny", "piwne", "ma", "nie ma", "wąsy", "ma", "nie ma")
Justyna = Character("Justyna", "kobieta", "czarny", "długie", "ciemny", "piwne", "ma", "ma", "brak", "nie ma", "nie ma")
Kamila = Character("Kamila", "kobieta", "czarny", "długie", "ciemny", "niebieskie", "nie ma", "nie ma", "brak", "nie ma", "nie ma")
Karol = Character("Karol", "mężczyzna", "mulat", "krótkie", "siwy", "piwne", "nie ma", "nie ma", "broda", "nie ma", "nie ma")
Kasia= Character("Kasia", "kobieta", "mulat", "długie", "ciemny", "niebieskie", "nie ma", "nie ma", "brak", "nie ma", "ma")
Lukasz = Character("Łukasz", "mężczyzna", "biały", "łysy", "rudy", "piwne", "nie ma", "nie ma", "broda i wąsy", "nie ma", "nie ma")
Maciek = Character("Maciek", "mężczyzna", "czarny", "krótkie", "siwy", "piwne", "nie ma", "nie ma", "wąsy", "nie ma", "nie ma")
Magda = Character("Magda", "kobieta", "czarny", "długie", "rudy", "piwne", "ma", "nie ma", "brak", "nie ma", "nie ma")
Marta = Character("Marta", "kobieta", "czarny", "długie", "blond", "piwne", "nie ma", "nie ma", "brak", "nie ma", "nie ma")
Michal = Character("Michał", "mężczyzna", "czarny", "łysy", "ciemny", "piwne", "nie ma", "ma", "broda i wąsy", "nie ma", "nie ma")
Ola = Character("Ola", "kobieta", "mulat", "długie", "blond", "piwne", "nie ma", "nie ma", "brak", "nie ma", "nie ma")
Pawel = Character("Paweł", "mężczyzna", "czarny", "krótkie", "ciemny", "piwne", "nie ma", "nie ma", "broda i wąsy", "nie ma", "nie ma")
Robert = Character("Robert", "mężczyzna", "biały", "krótkie", "blond", "niebieskie", "nie ma", "nie ma", "brak", "nie ma", "nie ma")
Weronika = Character("Weronika", "kobieta", "biały", "krótkie", "siwy", "piwne", "nie ma", "nie ma", "brak", "nie ma", "ma")
Wojtek = Character("Wojtek", "mężczyzna", "biały", "krótkie", "blond", "piwne", "nie ma", "nie ma", "brak", "ma", "nie ma")
Zosia = Character("Zosia", "kobieta", "biały", "długie", "siwy", "niebieskie", "ma", "ma", "brak", "nie ma", "ma")
characters = [Adam, Agnieszka, Andrzej, Ania, Artur, Daniel, Grzes, Iwona, Jan, Justyna, Kamila, Karol, Kasia, Lukasz, Maciek, Magda, Marta, Michal, Ola, Pawel, Robert, Weronika, Wojtek, Zosia]
