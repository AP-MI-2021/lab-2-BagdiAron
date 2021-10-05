import math
from datetime import date

# functie de verificare daca un numar este prim


def is_prime(n):
    if n < 1 or n % 2 == 0 and n != 2:
        return False
    for x in range(3, int(math.sqrt(n))+1, 2):
        if n % x == 0:
            return False
    return True

# functie care gaseste ultimul numar prim mai mic decat un numar dat


def get_largest_prime_below(n):
    for x in range(n-1, 1, -1):
        if is_prime(x) is True:
            return x

    return 'nu am gasit un numar adecvat'


def test_get_largest_prime_below():
    assert get_largest_prime_below(8) == 7
    assert get_largest_prime_below(3) == 2
    assert get_largest_prime_below(5) == 3
    assert get_largest_prime_below(100) == 97
    assert get_largest_prime_below(2) == 'nu am gasit un numar adecvat'


def get_age_in_days(birthday: date) -> int:
    return (date.today() - birthday).days.real


def test_get_age_in_days():
    assert get_age_in_days(12/12/1998) == 8329
    assert get_age_in_days(15/4/2004) == 6378


def main():
     indice = True
     while indice is True:
            print(""""
            apasa 1 pentru prima problema
            apasa 2 pentru a doua problema
            apasa 3 pentru a iesi     
                 """"")
            index = input("alege optiune ")
            if index == '1':
                y = int(input('numarul dat este', ))
                print(get_largest_prime_below(y))
            elif index == '2':
                z = input('data aleasa este', )
                v = z.split('/')
                birthday = date(int(v[2]), int(v[1]), int(v[0]))
                print(get_age_in_days(birthday))
            elif index == '3':
                break
            else:
                print("Nu ai ales o optiune buna")


if __name__ == '__main__':
    main()