import tkinter

window = tkinter.Tk()

window.columnconfigure(0, weight=1)
window.columnconfigure(0, weight=3)

list1 = ['Spotify', 'Youtube Music', 'Deezer', 'SoundCloud', 'Apple Music']
# noinspection PyTypeChecker

lista_items = tkinter.StringVar(value=list1)
listbox = tkinter.Listbox(window, height=10, listvariable=lista_items)
listbox.grid(column=0, row=0, sticky=tkinter.W)

window.mainloop()