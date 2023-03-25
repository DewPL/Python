from tkinter import *

okno = Tk()
okno.title('Moja Apka')
okno.geometry('400x600')
okno.resizable(False, False)

tekst1 = Label(okno, text='Witaj', font=20)
tekst1.pack()

tekst2 = Label(okno, text='Zmień mnie', font=20)
tekst2.pack()

def zmien_tekst():
    tekst1.config(text='Tekst został zmieniony')

def zmien_tekst_w():
    tekst2.config(text='Tekst został zmieniony 2')


przycisk1 = Button(text='Przycisk nr 1', width=10, command=lambda: zmien_tekst()).pack()
przycisk2 = Button(text='Przycisk nr 2', width=10, command=lambda: zmien_tekst_w()).pack()


# Wprowadzanie danych

tekst3 = Label(okno, text='Podaj liczbę')
entry1 = Entry(okno, width=50)
tekst3.pack()
entry1.pack()
 
def wejscie1():
    tekstWe1 = Label(okno, text='Podana liczta: ' + entry1.get())
    tekstWe1.pack()

btn1 = Button(okno, text='Podaj liczbę', command=wejscie1)
btn1.pack()

tekst4 = Label(okno, text='Podaj hasło')
entry2 = Entry(okno, width=50)
tekst4.pack()
entry2.pack()

def wejscie2():
    tekstWe2 = Label(okno, text='Hasło to: ' + entry2.get())
    tekstWe2.pack()

btn2 = Button(okno, text='Podaj hasło', command=wejscie2)
btn2.pack()


label01 = Label(okno, text='', font=40).pack()

label02 = Label(okno, text='hasło to: admin1234\nLogin: admin').pack()

logTx = Label(okno, text='Login: ')
pasTx = Label(okno, text='Hasło: ')

logEn = Entry(okno, width=40) # Wejście login
pasEn = Entry(okno, width=40) # Wejście hasło

logTx.pack()
logEn.pack()

pasTx.pack()
pasEn.pack()

def login():
    if logEn.get() == 'admin' and pasEn.get() == 'admin1234':
        labelPas = Label(okno, text='Użytkownik zalogowany')
        labelPas.pack()
    elif logEn.get() != 'admin':
        labelPas = Label(okno, text='Użytkownik nie istnieje')
        labelPas.pack()
    elif pasEn != 'admin1234':
        labelPas = Label(okno, text='Złe hasło')
        labelPas.pack()

btnLog = Button(okno, text='Zaloguj się', command=login)
btnLog.pack()



okno.mainloop()
