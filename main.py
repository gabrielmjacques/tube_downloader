# - tkinter - para interface gráfica
from tkinter import *
from tkinter import filedialog
from tkinter import ttk

# - pytube - para download de videos
from pytube import YouTube

# - os - para escolher onde salvar o vídeo
import os

# - threading - para executar o download em outra thread, evitando que o programa trave
import threading



# Funções
def ChooseDir():
    path = filedialog.askdirectory()
    print(path)
    path_var.set(path)


def DownloadVideo():
    try:
        yt = YouTube(url_var.get())
        
        status_label['foreground'] = 'black'
        status_label['text'] = f'Baixando Video: {yt.title} de {yt.author}. . .'
        
        stream = yt.streams.filter(file_extension='mp4').get_highest_resolution()
        stream.download(path_var.get())
        
        status_label['foreground'] = 'green'
        status_label['text'] = yt.title + ' Baixado com Sucesso'
    except:
        status_label['foreground'] = 'red'
        status_label['text'] = 'Erro: URL Inválida'
        


root = Tk()
root.configure(background='white')
root.title('Tube Downloader')

# Variaveis
url_var = StringVar()
path_var = StringVar()

# Estilos
style = ttk.Style()
style.theme_use('default')

style.configure('TLabel', font='Roboto 12 bold', background='white', padding=(0, 10))

style.configure("TEntry", padding=(10, 5))
style.map("TEntry", fieldbackground=[('!focus', '#F4F4F4')])

style.configure('TButton', font='Roboto 10 bold', foreground='white')
style.map('TButton', background=[('!active', '#E74040'), ('active', '#D23D3D')])

# Frame de informações
info_frame = Frame(root, background='white', padx=50, pady=10)
info_frame.grid(column=0, row=0)

status_label = ttk.Label(info_frame)
status_label.grid(column=0, row=0)

# Frame principal
mainframe = Frame(root, background='white', padx=50, pady=5)
mainframe.grid(column=0, row=1)

url_label = ttk.Label(mainframe, text='URL do Vídeo')
url_label.grid(column=0, row=0, sticky=W)

url_entry = ttk.Entry(mainframe, textvariable=url_var)
url_entry.grid(column=0, columnspan=2, row=1, sticky=EW)

path_label = ttk.Label(mainframe, text='Local de Download')
path_label.grid(column=0, row=2, sticky=W)

path_var.set(os.getcwd() + '/videos')
path_entry = ttk.Entry(mainframe, textvariable=path_var, width=100)
path_entry.grid(column=0, row=3)

path_button = ttk.Button(mainframe, text='Procurar')
path_button['command'] = ChooseDir
path_button.grid(column=1, row=3, sticky=NSEW)

# Download Frame
buttons_frame = Frame(root, padx=50, pady=10, background='white')
buttons_frame.grid(column=0, row=2)

download_button = ttk.Button(buttons_frame, text='Download', width=100)
download_button['command'] = lambda: threading.Thread(target=DownloadVideo).start()
download_button.grid(column=0, row=4, sticky=EW)


root.mainloop()