import time
import tkinter as tk
from pytube import YouTube
from tkinter import messagebox

root = tk.Tk()
root.title("YouTube Downloader")


# Funzione per il download del video
def download():
    try:
        # Ottieni il link dallo spazio di input di testo
        link = YouTube(link_entry.get())

        # Ottieni la cartella di destinazione dallo spazio di input di testo
        destination_folder = destination_entry.get()

        # Scarica il video nella cartella di destinazione
        video = link.streams.first()
        video.download(destination_folder)

        # Mostra il messaggio di conferma del download
        messagebox.showinfo("Download completato", "Il video è stato scaricato con successo!")

    except:
        # Mostra un messaggio di errore se il download fallisce
        messagebox.showerror("Errore", "Si è verificato un errore durante il download del video.")

# Dimensioni generiche della finestra
root.geometry("800x600+100+100")


# Spazio di input di testo per il link del video
link_label = tk.Label(root,height=2,text="Inserisci il link del video:", font=("Helvetica"))
link_label.pack()
link_entry = tk.Entry(root, width=50)
link_entry.pack()

# Spazio di input di testo per la cartella di destinazione
destination_label = tk.Label(root,height=2, text="Inserisci il percorso della cartella di destinazione:", font=("Helvetica"))
destination_label.pack()
destination_entry = tk.Entry(root, width=50)
destination_entry.pack()

# Aggiungi uno spaziatore verticale
spacer = tk.Label(root, height=1)
spacer.pack()

# Bottone per avviare il download
download_button = tk.Button(root,height=3, text="Download", font=("Helvetica"), background="Orange", command=download)
download_button.pack()

# language
Lang= tk.StringVar()
check= tk.Checkbutton(root, height=15, text="Italiano", font="Arial", variable=Lang)
check.pack()
root.mainloop()
