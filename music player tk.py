import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, master):
        self.master = master
        master.title("Odtwarzacz muzyki v.1.00")

        self.play_button = tk.Button(master, text="Odtwórz", command=self.play_music)
        self.play_button.pack()

        self.pause_button = tk.Button(master, text="Pauza", command=self.pause_music, state=tk.DISABLED)
        self.pause_button.pack()

        self.stop_button = tk.Button(master, text="Stop", command=self.stop_music, state=tk.DISABLED)
        self.stop_button.pack()

        self.choose_file_button = tk.Button(master, text="Wybierz plik", command=self.choose_file)
        self.choose_file_button.pack()

        self.filename_entry = tk.Entry(master)
        self.filename_entry.pack()

        self.file_path = None

    def choose_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Pliki muzyczne", "*.mp3")])
        self.filename_entry.delete(0, tk.END)
        self.filename_entry.insert(0, self.file_path)

    def play_music(self):
        if self.file_path is not None:
            pygame.mixer.init()
            pygame.mixer.music.load(self.file_path)
            pygame.mixer.music.play()
            self.play_button.config(state=tk.DISABLED)
            self.pause_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.NORMAL)

    def pause_music(self):
        pygame.mixer.music.pause()
        self.play_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

    def stop_music(self):
        pygame.mixer.music.stop()
        self.play_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.DISABLED)

root = tk.Tk()
root.geometry('400x200')
music_player = MusicPlayer(root)
root.mainloop()
