class KontoBankoweMeta(type):
    def __init__(cls, name, bases, dct):
        print("To jest konto PKO")
        super().__init__(name, bases, dct)

class KontoBankowe(metaclass=KontoBankoweMeta):
    def __init__(self, stan_poczatkowy=0):
        self.stan = stan_poczatkowy

    def przelew(self, kwota, konto_docelowe):
        if isinstance(konto_docelowe, KontoBankowe):
            if self.stan >= kwota:
                self.stan -= kwota
                konto_docelowe.stan += kwota
                print("Przelew udany.")
            else:
                print("Niewystarczające środki na koncie.")
        else:
            print("Podany obiekt nie jest kontem bankowym.")

# Przykładowe użycie
konto1 = KontoBankowe(1000)
konto2 = KontoBankowe(500)

print("Stan konta 1 przed przelewem:", konto1.stan)
print("Stan konta 2 przed przelewem:", konto2.stan)

konto1.przelew(300, konto2)

print("Stan konta 1 po przelewie:", konto1.stan)
print("Stan konta 2 po przelewie:", konto2.stan)