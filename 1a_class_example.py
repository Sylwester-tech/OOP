class Kalkulator:
    pass

class Dodawanie:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def dodaj(self):
        return self.a + self.b

class Odejmowanie:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def odejmij(self):
        return self.a - self.b

class Mnożenie:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def pomnóż(self):
        return self.a * self.b

class Dzielenie:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def podziel(self):
        if self.b != 0:
            return self.a / self.b
        else:
            print("Błąd: Nie można dzielić przez zero.")
            return None

# Example usage:
obiekt1 = Dodawanie(3, 5)
wynik = obiekt1.dodaj()
print(wynik)