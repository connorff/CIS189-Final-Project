import tkinter as tk

from MorseButton import MorseButton

root = tk.Tk()

morse_text = tk.Text(root, height=2, width=45)
morse_text.pack()

m_button = MorseButton(.5, morse_text)

morse_button = tk.Button(root, text="Morse Button")
morse_button.pack(side=tk.LEFT)
space_button = tk.Button(root, text="Add Space", command=m_button.add_space)
space_button.pack(side=tk.LEFT)
audio_button = tk.Button(root, text="Play Audio", command=m_button.play_audio)
audio_button.pack(side=tk.RIGHT)
clear_button = tk.Button(root, text="Clear", command=m_button.clear_morse)
clear_button.pack(side=tk.RIGHT)
morse_button.bind('<ButtonPress-1>', m_button.button_pressed)
morse_button.bind('<ButtonRelease-1>', m_button.button_release)

root.mainloop()