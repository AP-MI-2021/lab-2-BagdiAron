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


'''
    functia determina numarul de zile pe care le a trait un om fata de data curenta
'''


def get_age_in_days(birthday: date) -> int:
    return (date.today() - birthday).days.real


def test_get_age_in_days():
    assert get_age_in_days(12/12/1998) == 8329
    assert get_age_in_days(15/4/2004) == 6378


'''
    functia get_goldbach returneaza prin intermediul a 2 parametrii p1,p2 minimul respectiv maximul (numere prime)
    a caror suma este argumentul (numar natural strict mai mare decat 0) functiei 
'''


def get_goldbach(n) -> (int, int):
    if n <= 0:
        return "nu exista un astfel de numar"
    for a in range(2, n+1, 1):
        if is_prime(a) is True:
            p1 = a
            if is_prime(n - p1) is True:
                p2 = n - a
                return p1,p2
    return "nu exista un astfel de numar"


def test_get_goldbach(n):
    assert get_goldbach(5) == 2,3
    assert get_goldbach(7) == 2,5
    assert get_goldbach(8) == 3,5


def main():
     indice = True
     while indice is True:
            print("""
            apasa 1 pentru prima problema
            apasa 2 pentru a doua problema
            apasa 3 pentru a treia problema     
            apasa 4 pentru a iesi
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
                x = int(input('numarul ales este', ))
                print(get_goldbach(x))
            elif index == '4':
                break
            else:
                print("Nu ai ales o optiune buna")


if __name__ == '__main__':
    main()