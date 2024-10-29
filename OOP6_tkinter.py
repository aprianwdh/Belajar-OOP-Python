import tkinter as tk

main_window = tk.Tk(screenName="latihan")

label1 = tk.Label(main_window,text="Label 1")
label2 = tk.Label(main_window,text="Label 2")

button1 = tk.Button(main_window,text="tombol 1")

label1.pack()
label2.pack()
button1.pack()

main_window.mainloop()