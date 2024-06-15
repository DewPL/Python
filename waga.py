'''
**************************************************
Opis:   Tworzy bazę danych, dodaje dane edytuje je
        oraz umożliwia usuwanie dodanych danych
        wylicza różnicę wagową wprowadzonych danych
Autor:  Dominik Kolasiński
**************************************************
'''


from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import sqlite3



    # Połączenie z bd
def create_database():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS waga (
                 id INTEGER PRIMARY KEY, 
                 data TEXT, 
                 firma TEXT, 
                 rejestracja TEXT,
                 waga_wjazd REAL, 
                 waga_wyjazd REAL,
                 roznica REAL)''')
    conn.commit()
    conn.close()

    # Dodawanie danych do db
def query_save():
    no_reg_entry = no_reg.get()
    com_name_entry = com_name.get()
    weight_entry_value = weight_entry.get()
    weight_out_value = weight_out.get()
    now = datetime.now()
    data = now.strftime("%x %X")

    if no_reg_entry and com_name_entry and weight_entry_value and weight_out_value:
        conn = sqlite3.connect('example.db')
        c = conn.cursor()
        c.execute("INSERT INTO waga (data, firma, rejestracja, waga_wjazd, waga_wyjazd) VALUES (?, ?, ?, ?, ?)", 
                  (data, com_name_entry, no_reg_entry, weight_entry_value, weight_out_value))
        conn.commit()
        conn.close()
        query_database()
        no_reg.delete(0, tk.END)
        com_name.delete(0, tk.END)
        weight_entry.delete(0, tk.END)
        weight_out.delete(0, tk.END)

    # Pobieranie danych z db
def query_database():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('''SELECT *,
                ABS(waga_wjazd - waga_wyjazd) AS roznica
                FROM waga;''')
    records = c.fetchall()
    conn.close()

    # Wyczyść poprzednie dane w Treeview
    for item in list_trv.get_children():
        list_trv.delete(item)
    
    # Dodaj nowe dane do Treeview
    for row in records:
        list_trv.insert("", tk.END, values=row)
    
def search():
    q2 = q.get()
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('''SELECT 
                id, 
                data, 
                firma, 
                rejestracja,
                waga_wjazd,
                waga_wyjazd
                FROM waga
                WHERE data LIKE ? OR firma LIKE ? OR rejestracja LIKE ?''', 
              ('%' + q2 + '%', '%' + q2 + '%', '%' + q2 + '%'))
    records = c.fetchall()
    conn.close()
    
    # Wyczyść poprzednie dane w Treeview
    for item in list_trv.get_children():
        list_trv.delete(item)
    
    # Dodaj nowe dane do Treeview
    for row in records:
        list_trv.insert("", tk.END, values=row)

    # Pobieranie daty z systemu
def get_date():
    now = datetime.now()
    data = now.strftime("%x %X")
    data_label.config(text=data)


def getrow(event):
    rowid = list_trv.identify_row(event.y)
    item = list_trv.item(list_trv.focus())
    t1.set(item['values'][0])
    t2.set(item['values'][1])
    t3.set(item['values'][2])
    t4.set(item['values'][3])
    t5.set(item['values'][4])
    t6.set(item['values'][5])


def update_data():
    data_id = t1.get()
    data = t2.get()
    firma = t3.get()
    rejestracja = t4.get()
    wjazd = t5.get()
    wyjazd = t6.get()
    roznica = abs(float(wjazd) - float(wyjazd))

    if data_id:
        conn = sqlite3.connect('example.db')
        c = conn.cursor()
        try:
            c.execute('''UPDATE waga SET data = ?, firma = ?, rejestracja = ?, waga_wjazd = ?, waga_wyjazd = ?, roznica = ? 
                         WHERE id = ?''', (data, firma, rejestracja, wjazd, wyjazd, roznica, data_id))
            conn.commit()
            query_database()  # Odśwież dane w Treeview
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
        finally:
            conn.close()

def delete_data():
    data_id = t1.get()
    if data_id:
        response = messagebox.askyesno("Potwierdzenie", "Czy na pewno chcesz usunąć ten wpis?")
        if response:
            conn = sqlite3.connect('example.db')
            c = conn.cursor()
            try:
                c.execute("DELETE FROM waga WHERE id = ?", (data_id,))
                conn.commit()
                query_database()
            except sqlite3.Error as e:
                print(f"An error occurred: {e}")
            finally:
                conn.close()







root = Tk()
q = StringVar()
root.geometry('1050x600+100+100')
root.title('Waga v1.0.')
t1 = StringVar()
t2 = StringVar()
t3 = StringVar()
t4 = StringVar()
t5 = StringVar()
t6 = StringVar()

# ramki
main_frame = LabelFrame(root, text='Zarządzanie danymi')
main_frame.pack(fill='both', expand='yes', padx=20, pady=20)

left_frame = Frame(main_frame)
left_frame.pack(side=LEFT, fill='both', expand=True, padx=10, pady=10)

right_frame = Frame(main_frame)
right_frame.pack(side=RIGHT, fill='both', expand=True, padx=10, pady=10)

frame_two = LabelFrame(root, text='Lista')
frame_two.pack(fill='both', expand='yes', padx=20, pady=20)
# /ramki

# pola etykiety... 
    # lewa ramka
no_reg_label = Label(left_frame, text='Numer rejestracyjny')
no_reg_label.grid(row=0, column=0, padx=10, pady=5)
no_reg = Entry(left_frame, width=20)
no_reg.grid(row=0, column=1, padx=10, pady=5)

name_label = Label(left_frame, text='Przewoźnik')
name_label.grid(row=1, column=0, padx=10, pady=5)
com_name = Entry(left_frame, width=20)
com_name.grid(row=1, column=1, padx=10, pady=5)


weight_entry_label = Label(left_frame, text='Waga wjazd')
weight_entry_label.grid(row=2, column=0, padx=10, pady=5)
weight_entry = Entry(left_frame, width=20)
weight_entry.grid(row=2, column=1, padx=10, pady=5)

weight_out_label = Label(left_frame, text='Waga wyjazd')
weight_out_label.grid(row=3, column=0, padx=10, pady=5)
weight_out = Entry(left_frame, width=20)
weight_out.grid(row=3, column=1, padx=10, pady=5)

# przyciski
data_btn = Button(left_frame, text='Dodaj datę', command=get_date)
data_btn.grid(row=4, column=0, pady=10)

data_label = Label(left_frame, text='', font='Arial 10')
data_label.grid(row=4, column=1, pady=10)

add_db_btn = Button(left_frame, text='Zapisz', command=query_save)
add_db_btn.grid(row=6, column=0, columnspan=2, pady=10)
# /przyciski
    # /lewa ramka
# /pola etykiety...

# prawa ramka
edit_label = Label(right_frame, text='Edycja danych')
edit_label.grid(row=0, column=0, padx=10, pady=5)

# sekcja wyszukiwania
search_label = Label(right_frame, text='Szukaj')
search_label.grid(row=1, column=0, padx=10, pady=5)
q = Entry(right_frame, width=20)
q.grid(row=1, column=1, padx=10, pady=5)
search_btn = Button(right_frame, text='Szukaj', command=search)
search_btn.grid(row=1, column=2, padx=10, pady=5)
db_clear_btn = Button(right_frame, text='Wyczyść', command=query_database)
db_clear_btn.grid(row=1, column=3, padx=10, pady=5)

    # edycja danych
lb_id = Label(right_frame, textvariable=t1)
lb_data = Label(right_frame, textvariable=t2)
lb1 = Label(right_frame, text='Nr. rejestracyjny')
lb1.grid(row=2, column=0, padx=10, pady=5)
ent1 = Entry(right_frame, textvariable=t3)
ent1.grid(row=2, column=1, padx=5, pady=5)

lb2 = Label(right_frame, text='Przewoźnik')
lb2.grid(row=3, column=0, padx=10, pady=5)
ent2 = Entry(right_frame, textvariable=t4)
ent2.grid(row=3, column=1, padx=5, pady=5)

lb3 = Label(right_frame, text='Waga wjazdowa')
lb3.grid(row=4, column=0, padx=10, pady=5)
ent3 = Entry(right_frame, textvariable=t5)
ent3.grid(row=4, column=1, padx=5, pady=5)

lb4 = Label(right_frame, text='Waga wyjazdowa')
lb4.grid(row=5, column=0, padx=10, pady=5)
ent4 = Entry(right_frame, textvariable=t6)
ent4.grid(row=5, column=1, padx=5, pady=5)

up_btn = Button(right_frame, text='Edytuj', command=update_data)
delete_btn = Button(right_frame, text='Usuń', command=delete_data)
up_btn.grid(row=6, column=1, padx=10, pady=5)
delete_btn.grid(row=6, column=2, padx= 10, pady=5)
    # /edycja danych

# /prawa ramka

# frame_two
db_btn = Button(frame_two, text='Załaduj dane', command=query_database)
db_btn.pack(pady=10)


# treeview
columns = ('ID', 'Data', 'Przewoźnik', 'Numer rejestracyjny', 'Waga wjazd', 'Waga wyjazd', 'Różnica')
list_trv = ttk.Treeview(frame_two, columns=columns, show='headings', height='6')
for col in columns:
    list_trv.heading(col, text=col)
    # Ustawienie szerokości kolumn
    if col == 'ID':
        list_trv.column(col, width=50)
    else:
        list_trv.column(col, width=150)
list_trv.pack(fill='both', expand='yes', padx=20, pady=20)
list_trv.bind('<Double-1>', getrow)
# /treeview
# /frame_two

root.mainloop()