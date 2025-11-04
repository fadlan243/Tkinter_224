import tkinter as tk

root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("500x600")
root.configure(bg="white")  

judul = tk.Label(
    root,
    text="Aplikasi Prediksi Prodi Pilihan",
    font=("ARIAL", 16, "bold"),
    bg="white",
    fg="black"
)
judul.grid(row=0, column=0, columnspan=2, pady=20)

mapel_list = [
    "Matematika",
    "Bahasa Indonesia",
    "Bahasa Inggris",
    "Fisika",
    "Kimia",
    "Biologi",
    "Ekonomi",
    "Geografi",
    "Sosiologi",
    "Sejarah"
]

# Dictionary untuk menampung entry nilai 
entries = {}

# Membuat label dan entry input nilai 
for i, mapel in enumerate(mapel_list):
    lbl = tk.Label(
        root,
        text=f"{i+1}. {mapel}",
        font=("Times New Roman", 11),
        anchor="w",
        bg="white"
    )
    lbl.grid(row=i+1, column=0, padx=30, pady=5, sticky="w")

    ent = tk.Entry(root, width=10, justify="center")
    ent.grid(row=i+1, column=1, pady=5)
    entries[mapel] = ent

#Fungsi tombol prediksi 
def hasil_prediksi():
    # Tidak peduli berapa nilai yang diinput, hasil selalu sama
    label_hasil.config(
        text="Hasil Prediksi: Teknologi Informasi",
        fg="green"
    )

# Tombol Hasil Prediksi 
btn_prediksi = tk.Button(
    root,
    text="Hasil Prediksi",
    font=("Helvetica", 12, "bold"),
    bg="blue",
    fg="white",
    padx=20,
    pady=8,
    command=hasil_prediksi
)
btn_prediksi.grid(row=len(mapel_list)+2, column=0, columnspan=2, pady=25)

# Label Luaran Hasil Prediksi 
label_hasil = tk.Label(
    root,
    text="Hasil Prediksi: -",
    font=("Helvetica", 12),
    bg="white",
    fg="black"
)
label_hasil.grid(row=len(mapel_list)+3, column=0, columnspan=2, pady=10)

# mengatur ukuran kolom agar proporsional 
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# menjalankan aplikasi
root.mainloop()
