import tkinter as tk
from tkinter import messagebox

# === Membuat jendela utama ===
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("400x600")
root.configure(bg="#E3EAFD")

# === Judul Aplikasi ===
judul = tk.Label(
    root,
    text="Aplikasi Prediksi Prodi Pilihan",
    font=("Helvetica", 14, "bold"),
    bg="#E3F2FD",
    fg="#0D47A1"
)
judul.pack(pady=10)

# === Frame untuk input nilai ===
frame_nilai = tk.Frame(root, bg="#E3F2FD")
frame_nilai.pack(pady=10)

# Daftar mata pelajaran
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

# Dictionary untuk menyimpan input nilai
entries = {}

# Membuat 10 label dan entry
for mapel in mapel_list:
    frame_row = tk.Frame(frame_nilai, bg="#E3F2FD")
    frame_row.pack(pady=3)
    
    lbl = tk.Label(frame_row, text=mapel, width=15, anchor="w", bg="#E3F2FD")
    lbl.pack(side="left")
    
    ent = tk.Entry(frame_row, width=10)
    ent.pack(side="left")
    
    entries[mapel] = ent

# === Fungsi prediksi ===
def hasil_prediksi():
    try:
        # Ambil semua nilai dan hitung rata-rata
        nilai = [float(entries[m].get()) for m in mapel_list]
        rata = sum(nilai) / len(nilai)
        
        # Logika prediksi sederhana
        if rata >= 85:
            prediksi = "Teknik Informatika"
        elif rata >= 75:
            prediksi = "Sistem Informasi"
        elif rata >= 65:
            prediksi = "Manajemen"
        else:
            prediksi = "Ilmu Sosial"
        
        # Tampilkan hasil
        label_hasil.config(text=f"Hasil Prediksi: {prediksi}", fg="green")
    except ValueError:
        messagebox.showerror("Error", "Pastikan semua nilai diisi dengan angka!")

# === Tombol prediksi ===
btn_prediksi = tk.Button(
    root,
    text="Hasil Prediksi",
    font=("Helvetica", 11, "bold"),
    bg="#1565C0",
    fg="white",
    padx=10,
    pady=5,
    command=hasil_prediksi
)
btn_prediksi.pack(pady=20)

# === Label hasil ===
label_hasil = tk.Label(
    root,
    text="Hasil Prediksi: -",
    font=("Helvetica", 12),
    bg="#E3F2FD",
    fg="black"
)
label_hasil.pack(pady=10)

# === Jalankan aplikasi ===
root.mainloop()
