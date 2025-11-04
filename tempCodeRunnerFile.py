
import tkinter as tk
root = tk.Tk()

label1 = tk.Label(root, text="Kiri (anchor='w')", width=25, anchor="w", bg="lightblue")
label1.pack(pady=5)

label2 = tk.Label(root, text="Tengah (anchor='center')", width=25, anchor="center", bg="lightgreen")
label2.pack(pady=5)

label3 = tk.Label(root, text="Kanan (anchor='e')", width=25, anchor="e", bg="lightyellow")
label3.pack(pady=5)

root.mainloop()
