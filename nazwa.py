import sys
from os import system
import datetime
from prettytable import PrettyTable

lista_pacjentow = []


def init():
    file = open("baza pacjentow.txt", "r")
    lista_pacjentow = read_file(file)
    file.close()
    system('cls')
    main_menu()
    stan = "main"
    return stan

def read_file(file):
    for line in file:
        if line[len(line) - 1] == "\n":
            temp = line[:len(line) -1].split(", ")
        else:
            temp = line.split(", ")
        add(temp[0], temp[1], temp[2], temp[3], temp[4])

def save_file(filename):
    file = open(filename, "w")
    for pacjent in lista_pacjentow:
        for dana in pacjent:
            if dana != "pesel":
                file.write(str(pacjent[dana]) + ", ")
            else:
                file.write(str(pacjent[dana]))
        if lista_pacjentow.index(pacjent) != len(lista_pacjentow) - 1:
          file.write("\n")  
    file.close()

def display():
    table = PrettyTable()
    table.field_names = ["Lp. ", "Imię", "Nazwisko", "Data Urodzenia", "Płeć", "PESEL"]
    for pacjent in lista_pacjentow:
        temp = []
        temp.append(str(lista_pacjentow.index(pacjent) + 1) + ".")
        for element in pacjent:
            temp.append(pacjent[element])
        table.add_row(temp)
    print(table)
        

def add(imie, nazwisko, data, plec, pesel):
    pacjent = {"imie": imie,
                "nazwisko": nazwisko,
                "data": data,
                "plec": plec,
                "pesel": pesel}
    lista_pacjentow.append(pacjent)
    save_file("baza pacjentow.txt")

def check_name(name):
    for letter in name:
        if letter.isdigit() == True:
            return False
    return True

def check_date(date):
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        return False
    return True

def check_plec(plec):
    if plec == "M" or plec == "K":
        return True
    return False

def check_pesel(pesel):
    for letter in pesel:
        if letter.isdigit() == False:
            return False
        if len(pesel) != 11:
            return False
        return True
    
def main_menu():
    print("****************PRZYCHODNIA LEKARSKA*******************")
    print()
    print("1. Wyświetl pacjentów")
    print("2. Dodaj pacjenta")
    print("3. Usuń pacjenta")
    print("0. Wyjdź")
   
def display_menu():
    print("****************PRZYCHODNIA LEKARSKA*******************")
    print()
    display()
    print("0 <----- Cofnij")

def add_menu():
    dane_poprawne = True
    while True:
        if not dane_poprawne:
            system('cls')
        print("****************PRZYCHODNIA LEKARSKA*******************")
        print()
        if dane_poprawne:
            print("Wpisz dane pacjenta: ")
        else:
            print("Błąd, ponownie wprowadź dane pacjenta: ")
            
        imie = input("Imię: ")
        if not check_name(imie):
            dane_poprawne = False
            continue
        else:
            dane_poprawne = True
            
        nazwisko = input("Nazwisko: ")
        if not check_name(nazwisko):
            dane_poprawne = False
            continue
        else:
            dane_poprawne = True
            
        data = input("Data: (XXXX-XX-XX) ")
        if not check_date(data):
            dane_poprawne = False
            continue
        else:
            dane_poprawne = True
            
        plec = input("Płeć: (M/K) ").upper()
        if not check_plec(plec):
            dane_poprawne = False
            continue
        else:
            dane_poprawne = True
            
        pesel = input("PESEL: ")
        if not check_pesel(pesel):
            dane_poprawne = False
            continue
        else:
            dane_poprawne = True
            
        add(imie, nazwisko, data, plec, pesel)
        break
    
def remove_menu():
    print("****************PRZYCHODNIA LEKARSKA*******************")
    print()
    print("Wybierz numer pacjenta, którego chcesz usunąć!!!")
    print()
    display()
    print("0 <----- Cofnij")
    nr_pacjenta = int(input())
    if nr_pacjenta in range(1, len(lista_pacjentow) + 1):
        lista_pacjentow.remove(lista_pacjentow[nr_pacjenta-1])
        save_file("baza pacjentow.txt")

def wybor(stan, opcja):
    if stan == "main":
        if opcja == "0":
            sys.exit()
        elif opcja == "1":
            display_menu()
            stan = "display"
        elif opcja == "2":
            add_menu()
            stan = "add"
        elif opcja == "3":
            remove_menu()
            stan = "remove"
        else:
            main_menu()

    elif stan == "display":
        if opcja == "0":
            main_menu()
            stan = "main"
        else:
            display_menu()

    elif stan == "add":
        if opcja == "0":
            main_menu()
            stan = "main"
        else:
            add_menu()

    elif stan == "remove":
        if opcja == "0":
            main_menu()
            stan = "main"
        else:
            remove_menu()

    return stan
    
def main():
    stan = init()
    while True:
        if stan != "add" and stan != "remove":
            opcja = input()
            system('cls')
        else:
            stan = "main"
            system('cls')
            opcja = None
        stan = wybor(stan, opcja)

if __name__=="__main__":
    main()
