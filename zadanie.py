import sqlite3

conn = sqlite3.connect('zadanie_DB.sqlite')
cur = conn.cursor()

# Tworzenie DB
cur.execute('DROP TABLE IF EXISTS Zadanie') # Usunie DB jeśli istnieje
cur.execute('''CREATE TABLE Zadanie
                (kategoria TEXT, nazwa TEXT, cena FLOAT, data TEXT)''')

# Wstawianie danych
cur.execute("""INSERT INTO Zadanie VALUES
                ('Samochody',
                'BMW 325',
                50000,
                '2005')""")

cur.execute("""INSERT INTO Zadanie VALUES
                ('Samochody',
                'Mercedes SLK',
                60000,
                '2005')""")
            
cur.execute("""INSERT INTO Zadanie VALUES
                ('Samochody',
                'Fiat 126p',
                200,
                '2000')""")

cur.execute("""INSERT INTO Zadanie VALUES
                ('Samochody',
                'Peugeot 3008',
                3500,
                '2015')""")

cur.execute("""INSERT INTO Zadanie VALUES
                ('Motocykle',
                'Kawasaki EL250',
                6500,
                '2000')""")

cur.execute("""INSERT INTO Zadanie VALUES
                ('Motocykle',
                'Ducati 1199 Panigale',
                65000,
                '2012')""")

cur.execute("""INSERT INTO Zadanie VALUES
                ('Motocykle',
                'Harley Davidson Fat Boy 114',
                '------',
                '2023')""")

# zapisanie zmian
conn.commit()

# Odczyt danych z SQLite
print('Odczytanie danych Zapytanie sql select *')
print('Baza danych | Marka model  |  cena  | rok')
cur.execute("SELECT * FROM Zadanie")

for row in cur:
    print(row)
print()

# odczyt danych według daty ASC
print('Odczytanie danych według daty rosnąco')
print('Baza danych | Marka model  |  cena  | rok')
cur.execute("SELECT * FROM Zadanie ORDER BY data ASC")

for row in cur:
    print(row)

print()

# odczyt danych według daty DESC
print('Odczytanie danych według daty malejąco')
print('Baza danych | Marka model  |  cena  | rok')
cur.execute("SELECT * FROM Zadanie ORDER BY data DESC")

for row in cur:
    print(row)

print()

# odczyt danych po kategoriach
print('Odczytanie danych po kategorii')
print('Baza danych | Marka model  |  cena  | rok')
cur.execute("SELECT * FROM Zadanie WHERE kategoria = 'Motocykle'")

for row in cur:
    print(row)

print()

#  suma wszystkiego w DB
print('Sumuje wszystko w bazie po cenie')
print('SUMA:')
cur.execute("SELECT SUM(cena) FROM Zadanie")

for row in cur:
    print(row)

print()

# odczyt danych według daty podanej przez użytkownika
print('Odczytanie danych według daty podanej przez użytkownika')
print('Baza danych | Marka model  |  cena  | rok')
data_IN = input("Podaj rok produkcji: ")
cur.execute("SELECT * FROM Zadanie WHERE data =" + data_IN)

for row in cur:
    print(row)

print()

# Suma dla wybranej daty
print('Odczytanie danych według daty podanej przez użytkownika')
print('Baza danych | Marka model  |  cena  | rok')
data_IN = input("Podaj rok produkcji: ")
cur.execute("SELECT SUM(cena) FROM Zadanie WHERE data =" + data_IN)

for row in cur:
    print(row)

print()


# zamknięcie połączenia
conn.close()