class Kalkulator:
    def dodawanie(self, x, y):
        return x + y

    def odejmowanie(self, x, y):
        return x - y

    def mnozenie(self, x, y):
        return x * y

    def dzielenie(self, x, y):
        if y != 0:
            return x / y
        else:
            return "Nie można dzielić przez zero!"

# Tworzymy obiekt klasy Kalkulator
kalk = Kalkulator()

# Przykładowe użycie metod
print("Dodawanie: ", kalk.dodawanie(5, 3))
print("Odejmowanie: ", kalk.odejmowanie(5, 3))
print("Mnożenie: ", kalk.mnozenie(5, 3))
print("Dzielenie: ", kalk.dzielenie(5, 3))