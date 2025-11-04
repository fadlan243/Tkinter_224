import tkinter as tk
import tkinter.messagebox as msg
top =  tk.Tk()
top.title ("My tkinter window")
top.geometry("400x300")
top.configure(bg="blue")
def pesanHello():
    msg.showinfo("Pesan", "Assalamualaikum all")
tombol = tk.Button (top, text="klik saya", command = pesanHello)
checkVar1 = tk.IntVar()
checkVar2 =tk.IntVar()
check1=tk.Checkbutton(top, text = "Pilihan 1", variable = checkVar1)
check2=tk.Checkbutton(top, text = "Pilihan 2", variable = checkVar2)
check1.pack()
check2.pack()
tombol.pack() #pady=20
L1=tk.Label(top, text = "Masukkan Nama:")
L1.pack(side = tk.LEFT)
E1=tk.Entry(top, bd = 5)
E1.pack(side = tk.RIGHT)
def tampilkanNama():
    nama = E1.get()
    msg.showinfo("Nama Anda", f"Nama Anda adalah: {nama}")
tombolNama = tk.Button(top, text="Tampilkan Nama",
                       comman=tampilkanNama)
tombolNama.pack(side=tk.BOTTOM)
top.mainloop()

