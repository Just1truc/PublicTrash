from tkinter import *
from turtle import color

from cairo import FontWeight

def showPassword():
    print(entry_point.get())

def askInfoWindow( Verify):

    global entry_point
    global window

    # Init window
    window = Tk()
    window.title("Argos")

    # frames
    frame = Frame(window, bg="#202020", relief= 'sunken')
    frame.pack(fill= BOTH, expand= True)

    # Init labels

    title_label = Label(frame, text="Admin password", fg="white", bg="#202020", font=('Roboto', '11', 'bold'))

    title_label.grid(row=0, column=0, padx=25, pady=10, sticky=W)

    info = ""
    entry_point = Entry(frame, textvariable=info, show='*', bg ='#333333', fg='white', insertbackground="white", validate="none", selectborderwidth=0, borderwidth=10, relief=FLAT)

    entry_point.focus_set()

    entry_point.grid(row = 1, column = 0, padx=25)

    url_label = Label(frame, text="Server Url", fg="white", bg="#202020", font=('Roboto', '11', 'bold'))

    url_label.grid(row=2, column=0, padx=25, pady=10, sticky=W)

    url = ""
    url_entry_point = Entry(frame, textvariable=url, bg ='#333333', fg='white', insertbackground="white", validate="none", selectborderwidth=0, borderwidth=10, relief=FLAT)

    url_entry_point.focus_set()

    url_entry_point.grid(row = 3, column = 0, padx=25)

    # Validate Button

    button = Button(frame, text='Validate', command = Verify, bg="lightgreen", borderwidth=0, cursor="hand2", font=('Roboto', '11', 'bold'))
    button.grid(row = 4, column = 0, ipadx = 10, pady = 20)

    window.mainloop()

askInfoWindow(Verify=showPassword)

