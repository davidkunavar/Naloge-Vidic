

predmeti = ["SLO", "ANJ", "MAT", "PNA", "NSVO", "ŠVZ", "NAR", "IEKI"]


# a) izpis stavka
def izpiši():
    i = len(predmeti)
    for i in range(i):
        print(predmeti[i] + ",", end= "")

#b) razvrsti od a do ž

def razvrsti():
    i = len(predmeti)
    predmeti.sort()
    for i in range(i):
        print(predmeti[i] + ",", end= "")

#c) razvrsti od a do ž

def razvrsti():
    i = len(predmeti)
    predmeti.sort(reverse=True)
    for i in range(i):
        print(predmeti[i] + ",", end= "")

print("Prva naloga a) primer:")
izpiši()

print("\n")

print("Prva naloga b) primer:")
razvrsti()

# tretja nevem kaj hoče

