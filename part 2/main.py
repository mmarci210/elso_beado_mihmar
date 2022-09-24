def elso_beado_2resz(szam, mertekegy):
    #### mondat bekerese
    szam = szam.lower()
    mertekegy = mertekegy.lower()

    #### szamolas elvegzese
    if  mertekegy == "cm":
        a = int(szam) * 2.54
        print(a, "inches")
    elif mertekegy == "inch":
        a = int(szam) / 2.54
        print(a, "cm")
    else:
        print("Not correct unit!")

if __name__ == '__main__':
    print("Adjon meg egy számot és egy mértékegységet (cm/inch):")
    szam = input()
    mertekegy = input()
    elso_beado_2resz(szam, mertekegy)
