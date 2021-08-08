#Ez a függvény kiszámolja a Coulomb erő értékét
def coulomb_equation(q1,q2,r):
    k = 9*10**9
    F = q1*q2*k/r**2
    return F


def main():

    print("Mertekegysegnel a kovetkezoket irhatod: mC,mikroC,nC,cm,mm")
    q1 = int(input("Add meg az elso toltes erteket="))
    q1m = input('Ird be a mertekegyseget: ')
    q2 = int(input("Add meg a masodik toltes erteket="))
    q2m = input('Ird be a mertekegyseget: ')
    r = int(input("Add meg a toltesek kozotti tavolsagot="))
    rm = input('Ird be a mertekegyseget: ')


    szotar = {'mC':10**(-3),'mikroC':10**(-6),'nC':10**(-9),'cm':10**(-2),'mm':10**(-3)}
    for key,value in szotar.items():
        if key == q1m:
            q1 = q1*value
        if key == q2m:
            q2 = q2*value
        if key == rm:
            r = r*value
        


    print(f"A toltesek kozott van {coulomb_equation(q1,q2,r)} Coulomb ero")


    


if __name__=='__main__':
    main()

