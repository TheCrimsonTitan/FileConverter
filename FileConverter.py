from PIL import Image as img
import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo


class MyGUI:

    #The constructor for the GUI
    def __init__(self):
        self.root=tk.Tk()
        
        self.label = tk.Label(self.root, text="Select a File to convert", font=('Arial', 18))
        self.label.pack(padx=10, pady=10)
        self.root.geometry("500x500")

        self.button=tk.Button(self.root, text="Select video file", font=('Arial',18), command=self.SelectVideoFile)
        self.button.pack(padx=10,pady=10)

        self.button=tk.Button(self.root, text="Select Audio File", font=('Arial',18), command=self.SelectAudioFile)
        self.button.pack(padx=10,pady=10)




        self.root.mainloop()

#It is important that we have the word "self" in the parameters because we are in a class
    def SelectVideoFile(self):
        filetypes = (
            ('text files', '*.mp4'),
            ('audio files', '*.m4v'),
            ('All files', '*.*')
        )

        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)

        showinfo(
            title='You Have selected:',
            message=filename
        )


    def SelectAudioFile(self):
        filetypes = (
            ('text files', '*.mp3'),
            ('audio files', '*.m4a'),
            ('All files', '*.*')
        )

        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)

        showinfo(
            title='You Have selected:',
            message=filename
        )





def main():
    MyGUI()


if __name__ == '__main__':
    main()
