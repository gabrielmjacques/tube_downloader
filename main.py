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
    print(res_var.get())
    try:
        yt = YouTube(url_var.get())
        
        status_label['foreground'] = 'black'
        status_label['text'] = f'Baixando Video: {yt.title} de {yt.author}. . .'
        
        stream = yt.streams.filter(res=res_var.get(), progressive=True).first()
        
        if stream is None:
            status_label['foreground'] = 'red'
            status_label['text'] = 'Stream com resolução escolhida não encontrado'
            return
        
        stream.download(output_path=path_var.get(), filename=f'{yt.title}_{res_var.get()}.mp4')
        
        status_label['foreground'] = 'green'
        status_label['text'] = yt.title + ' Baixado com Sucesso'
    except:
        status_label['foreground'] = 'red'
        status_label['text'] = 'Erro ao baixar o vídeo, tente novamente'        

        


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

# Frame de Resolução
res_frame = Frame(root, padx=50, pady=10, background='white')
res_frame.grid(column=0, row=3)

res_var = StringVar()
res_var.set("720p")
res480_radio = ttk.Radiobutton(res_frame, text="480p", value="480p", variable=res_var)
res480_radio.grid(column=0, row=0)

res720_radio = ttk.Radiobutton(res_frame, text="720p", value="720p", variable=res_var)
res720_radio.grid(column=1, row=0)

res1080_radio = ttk.Radiobutton(res_frame, text="1080p", value="1080p", variable=res_var)
res1080_radio.grid(column=2, row=0)

# Download Frame
buttons_frame = Frame(root, padx=50, pady=10, background='white')
buttons_frame.grid(column=0, row=4)

download_button = ttk.Button(buttons_frame, text='Download', width=100)
download_button['command'] = lambda: threading.Thread(target=DownloadVideo).start()
download_button.grid(column=0, row=4, sticky=EW)


root.mainloop()