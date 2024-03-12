class Kalkulator:
    pass
class dodawanie(a,b):
    def dodaj(self, a, b):
        return a + b
class odejmowanie(a,b):
    def odejmij(self, a, b):
        return a - b
class mnożenie(a,b):
    def pomnoz(self, a, b):
        return a * b
class dzielenie(a,b):
    def podziel(self, a, b):
        if b != 0:
            return a / b
        else:
            print("Błąd: Nie można dzielić przez zero.")
        return None


obiekt1=Kalkulator()

obiekt1.