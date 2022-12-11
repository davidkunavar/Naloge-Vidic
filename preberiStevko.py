

while True:
    print("Vnesi stevko")

    input_number = input()

    dolzina = len(input_number)

    if dolzina >= 4 and dolzina <= 6:
        print("juhu, uspelo ti je!")
        break
    else:
        print("jebiga treba bo še enkrat probat")

