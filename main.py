# - tkinter - para interface gráfica
from tkinter import *
from tkinter import filedialog
from tkinter import ttk

# - pytube - para download de videos
from pytube import YouTube

# - os - para escolher onde salvar o vídeo
import os



# Funções
def ChooseDir():
    path = filedialog.askdirectory()
    print(path)
    path_var.set(path)

def DownloadVideo(URL):
    yt = YouTube(URL)
        
    stream = yt.streams.get_highest_resolution()
    stream.download(path_var.get())
    
    status_label['text'] = 'Video |' + yt.title + '| Baixado com Sucesso'


root = Tk()
root.title('Tube Downloader')

# Variaveis
url_var = StringVar()
path_var = StringVar()

# Estilos
style = ttk.Style()
style.configure('default')

style.configure('TEntry', padding=(10, 5))

# Frame de titulo
title_frame = ttk.Frame(root, padding=(50, 10))
title_frame.grid(column=0, row=0)

status_label = ttk.Label(title_frame)
status_label.grid(column=0, row=0)

# Frame principal
mainframe = ttk.Frame(root, padding=(50, 10))
mainframe.grid(column=0, row=1)

url_label = ttk.Label(mainframe, text='URL do Vídeo')
url_label.grid(column=0, row=0, sticky=W)

url_entry = ttk.Entry(mainframe, textvariable=url_var)
url_entry.grid(column=0, columnspan=2, row=1, sticky=EW)

path_label = ttk.Label(mainframe, text='Caminho')
path_label.grid(column=0, row=2, sticky=W)

path_var.set(os.getcwd() + '/videos')
path_entry = ttk.Entry(mainframe, textvariable=path_var, width=100)
path_entry.grid(column=0, row=3)

path_button = ttk.Button(mainframe, text='Procurar')
path_button['command'] = ChooseDir
path_button.grid(column=1, row=3, sticky=NSEW)

download_button = ttk.Button(mainframe, text='Download')
download_button['command'] = lambda: DownloadVideo(url_var.get())
download_button.grid(column=0, columnspan=2, row=4, sticky=EW)


root.mainloop()