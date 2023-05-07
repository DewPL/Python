import pygame

pygame.init()

print('''
Music Player with Python Shell
''')

dzwiek = input('Podaj nazwę utworu: ')

if dzwiek.find('mp3') >= 0:
    pygame.mixer.music.load(dzwiek)
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(loops=-1)

    while True:
        print('1. Stop')
        print('2. Start')
        print('3. Przewiń do wybranej pozycji')
        print('4. Zmień głośność')
        print('5. Wyjdź')
        choice = input('Wybierz opcję: ')

        if choice == '1':
            pygame.mixer.music.stop()
        elif choice == '2':
            pygame.mixer.music.play()
        elif choice == '3':
            pozycja = int(input('Podaj pozycję do której chcesz przewinąć utwór (w milisekundach): '))
            pygame.mixer.music.rewind()
            pygame.mixer.music.set_pos(pozycja / 1000)
        elif choice == '4':
            volume = float(input('Podaj nową głośność (0.0 - 1.0): '))
            pygame.mixer.music.set_volume(volume)
        elif choice == '5':
            pygame.mixer.music.stop()
            break

        
    pygame.quit()

elif dzwiek.find('wav') >= 0:
    pygame.mixer.music.load(dzwiek)
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(loops=-1)

    while True:
        print('1. Stop')
        print('2. Start')
        print('3. Przewiń do wybranej pozycji')
        print('4. Zmień głośność')
        print('5. Wyjdź')
        choice = input('Wybierz opcję: ')

        if choice == '1':
            pygame.mixer.music.stop()
        elif choice == '2':
            pygame.mixer.music.play()
        elif choice == '3':
            pozycja = int(input('Podaj pozycję do której chcesz przewinąć utwór (w milisekundach): '))
            pygame.mixer.music.rewind()
            pygame.mixer.music.set_pos(pozycja / 1000)
        elif choice == '4':
            volume = float(input('Podaj nową głośność (0.0 - 1.0): '))
            pygame.mixer.music.set_volume(volume)
        elif choice == '5':
            pygame.mixer.music.stop()
            break

    pygame.quit()
else:
    print('Nieznany format')

