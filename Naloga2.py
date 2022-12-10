import random
import string

prazen = []

for i in range(5):

    #Tuki določš random_število pač eno cifro k si izbere komp s fukcijo random.randrange. Prvi dve cifri povesta

    #od kje do kje hočš da izbere, treja pa krneki nima veze ahah.

    #pol pa z append fuknicijo to sa dodaš v prazen vektor, k sva ga določila zgori

    # in to nardiš 5x ker mava for i v dolžini 5

    random_število = random.randrange(0, 50, 3)
    prazen.append(random_število)
    print(prazen[i])


def sestej_vse():
    sestevek = sum(prazen)
    print(sestevek)

def najvecje_stev():
    dolzina_prazen = len(prazen)

    najvecje_stevilo = prazen[0]

    for i in range(dolzina_prazen):
        if prazen[i] > najvecje_stevilo:
            najvecje_stevilo = prazen[i]

    print(najvecje_stevilo)


print("\n")
print("Seštevek števil je:")
sestej_vse()
print("\n")
print("Največje število je:")
najvecje_stev()



