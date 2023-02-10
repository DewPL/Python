
import sqlite3

conn = sqlite3.connect('zadanie_DB.sqlite')
cur = conn.cursor()

# Tworzenie DB
cur.execute('DROP TABLE IF EXISTS Zadanie') # Usunie DB jeśli istnieje
cur.execute('''CREATE TABLE Zadanie
                (category TEXT, name TEXT, amount FLOAT, date TEXT);''')

# Wstawianie danych
cur.execute("""INSERT INTO Zadanie VALUES
            ('1',
            'apples',
            2.40,
            '2021-02-03');""")

cur.execute("""INSERT INTO Zadanie VALUES
            ('1',
            'bread',
            2.00,
            '2021-02-03');""")

cur.execute("""INSERT INTO Zadanie VALUES
            ('1',
            'salami',
            4.30,
            '2021-02-02');""")

cur.execute("""INSERT INTO Zadanie VALUES
            ('1',
            'butter',
            5.20,
            '2021-02-02');""")

cur.execute("""INSERT INTO Zadanie VALUES
            ('1',
            'butter',
            5.20,
            '2020-12-27');""")

cur.execute("""INSERT INTO Zadanie VALUES
            ('2',
            'rent',
            000.00,
            '2021-02-04');""")

cur.execute("""INSERT INTO Zadanie VALUES
            ('2',
            'rent',
            000.00,
            '2020-12-27');""")

cur.execute("""INSERT INTO Zadanie VALUES
            ('2',
            'electricity',
            42.00,
            '2021-02-04');""")

cur.execute("""INSERT INTO Zadanie VALUES
            ('2',
            'electricity',
            42.00,
            '2020-12-07');""")

cur.execute("""INSERT INTO Zadanie VALUES
            ('3',
            'trousers',
            110.00,
            '2021-02-04');""")

cur.execute("""INSERT INTO Zadanie VALUES
            ('3',
            'shirt',
            60.00,
            '2021-01-16');""")

cur.execute("""INSERT INTO Zadanie VALUES
            ('3',
            'shirt',
            60.00,
            '2020-12-25');""")

# zapisanie zmian
conn.commit()

# sortowanie danych w bazie poprzez zapytania SQL i 
# Odczyt danych z bazy
print('Odczytanie danych Zapytanie sql select *')
print('| kat. |  nazwa  | cena | data |')
cur.execute("SELECT * FROM Zadanie;")

for row in cur:
    print(row)
print()

# odczyt danych według daty ASC
print('Odczytanie danych według daty rosnąco')
print('| kat. |  nazwa  | cena | data |')
cur.execute("SELECT * FROM Zadanie ORDER BY date ASC;")

for row in cur:
    print(row)

print()

# odczyt danych według daty DESC
print('Odczytanie danych według daty malejąco')
print('| kat. |  nazwa  | cena | data |')
cur.execute("SELECT * FROM Zadanie ORDER BY date DESC;")

for row in cur:
    print(row)

print()

#  suma wszystkiego w DB
print('Sumuje wszystko w bazie po cenie')
print('SUMA:')
cur.execute("SELECT SUM(amount) FROM Zadanie;")

for row in cur:
    print(row)

print()

# odczyt danych po kategoriach
print('Odczytanie danych po kategorii')
kat = input("Podaj kategorię: ")
print('| kat. |  nazwa  | cena | data |')
cur.execute("SELECT * FROM Zadanie WHERE category = " + kat)

for row in cur:
    print(row)

print()

# Suma dla wybranej daty
# q SQL użyć można DATEPART i funkcji GETDATE()
print('Odczytanie danych według daty podanej przez użytkownika')
data_IN = input("Podaj datę: ")
print('SUMA')
cur.execute("SELECT SUM(amount) FROM Zadanie WHERE date >= " + data_IN)
# cur = self.conn.cursor()
# cur.execute("SELECT datetime('now', 'localtime')")

for row in cur:
    print(row)

print()

# odczyt danych według daty podanej przez użytkownika
print('Odczytanie danych według daty podanej przez użytkownika')
data_IN = input("Podaj od: ")
data_OUT = input("Podaj do: ")
print('| kat. |  nazwa  | cena | data |')
cur.execute("SELECT * FROM Zadanie WHERE date >= " + data_IN + " AND date <= " + data_OUT)

for row in cur:
    print(row)

print()

# zamknięcie połączenia
conn.close()