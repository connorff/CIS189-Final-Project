import tkinter as tk

from MorseButton import MorseButton

root = tk.Tk()

m_button = MorseButton(.5)

button = tk.Button(root, text="Morse Button")
button.pack(side=tk.LEFT)
button.bind('<ButtonPress-1>', m_button.button_pressed)
button.bind('<ButtonRelease-1>', m_button.button_release)
root.mainloop()
