import tkinter as tk
from tkinter import ttk
from pyswip import Prolog
from tkinter import messagebox

# Inisialisasi Prolog
prolog = Prolog()
prolog.consult("t4_pakar_gayabelajar_gui.pl")

gaya_belajar = list()
ciri = dict()
index_gaya_belajar = 0
index_ciri = 0
current_gaya_belajar = ""
current_ciri = ""

def mulai_penentuan():
        global gaya_belajar, ciri, index_gaya_belajar, index_ciri

        # Bersihkan database Prolog
        prolog.retractall("ciri_pos(_)")
        prolog.retractall("ciri_neg(_)")

        start_btn.configure(state=tk.DISABLED)
        yes_btn.configure(state=tk.NORMAL)
        no_btn.configure(state=tk.NORMAL)

        # Mendapatkan daftar gaya_belajar dan ciri
        gaya_belajar = [p["X"].decode() for p in list(prolog.query("gaya_belajar(X)"))]
        for p in gaya_belajar:
                ciri[p] = [g["X"] for g in list(prolog.query(f'ciri(X, "{p}")'))]

        index_gaya_belajar = 0
        index_ciri = -1

        pertanyaan_selanjutnya()

def pertanyaan_selanjutnya(ganti_gaya_belajar=False):
        global current_gaya_belajar, current_ciri, index_gaya_belajar, index_ciri

        # Atur index gaya belajar
        if ganti_gaya_belajar:
            # Ganti ke gaya belajar selanjutnya
                index_gaya_belajar += 1
                index_ciri = -1

        # Apabila daftar gaya belajar sudah habis berarti tidak terdeteksi gaya_belajar
        if index_gaya_belajar >= len(gaya_belajar):
                hasil_penentuan()
                return
        current_gaya_belajar = gaya_belajar[index_gaya_belajar]

        # Atur index ciri
        index_ciri += 1

        # Apabila semua ciri dari gaya_belajar habis, berarti terdeteksi gaya_belajar tsb
        if index_ciri >= len(ciri[current_gaya_belajar]):
                hasil_penentuan(current_gaya_belajar)
                return
        current_ciri = ciri[current_gaya_belajar][index_ciri]

        #  Cek status ciri di database prolog
        if list(prolog.query(f"ciri_pos({current_ciri})")):
                pertanyaan_selanjutnya()
                return
        elif list(prolog.query(f"ciri_neg({current_ciri})")):
                pertanyaan_selanjutnya(ganti_gaya_belajar=True)
                return

        # Mendapatkan pertanyaan baru
        pertanyaan = list(prolog.query(f"pertanyaan({current_ciri}, Y)"))[0]["Y"].decode()
        
        # Set pertanyaan ke kotak pertanyaan
        tampilkan_pertanyaan(pertanyaan)

def tampilkan_pertanyaan(pertanyaan):
        kotak_pertanyaan.configure(state=tk.NORMAL)
        kotak_pertanyaan.delete(1.0, tk.END)
        kotak_pertanyaan.insert(tk.END, pertanyaan)
        kotak_pertanyaan.configure(state=tk.DISABLED)

def jawaban(jwb):
        if jwb:
                prolog.assertz(f"ciri_pos({current_ciri})")
                pertanyaan_selanjutnya()
        else:
                prolog.assertz(f"ciri_neg({current_ciri})")
                pertanyaan_selanjutnya(ganti_gaya_belajar=True)

def hasil_penentuan(_=None):
        hasil = dict()

        for gb in gaya_belajar:
                jumlah_cocok = 0
                for c in ciri[gb]:
                        if list(prolog.query(f"ciri_pos({c})")):
                                jumlah_cocok += 1
                hasil[gb] = jumlah_cocok

        gaya_terbaik = max(hasil, key=hasil.get)
        if hasil[gaya_terbaik] > 0:
                messagebox.showinfo("Hasil Penentuan", f"Anda terdeteksi {gaya_terbaik}.")
        else:
                messagebox.showinfo("Hasil Penentuan", "Tidak terdeteksi gaya belajar.")

        yes_btn.configure(state=tk.DISABLED)
        no_btn.configure(state=tk.DISABLED)
        start_btn.configure(state=tk.NORMAL)

# GUI

root = tk.Tk()
root.title("Sistem Pakar Penentuan Gaya Belajar")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Label(mainframe, text="Aplikasi Penentuan Gaya Belajar", font=("Arial", 16)).grid(column=0, row=0, columnspan=3)
ttk.Label(mainframe, text="Kolom Pertanyaan:").grid(column=0, row=1)

kotak_pertanyaan = tk.Text(mainframe, height=5, width=43, state=tk.DISABLED)
kotak_pertanyaan.grid(column=0, row=2, columnspan=3)

no_btn = ttk.Button(mainframe, text="Tidak", state=tk.DISABLED, command=lambda: jawaban(False))
no_btn.grid(column=1, row=3, sticky=(tk.W, tk.E))

yes_btn = ttk.Button(mainframe, text="Ya", state=tk.DISABLED, command=lambda: jawaban(True))
yes_btn.grid(column=2, row=3, sticky=(tk.W, tk.E))

start_btn = ttk.Button(mainframe, text="Mulai Penentuan", command=mulai_penentuan)
start_btn.grid(column=1, row=4, columnspan=2, sticky=(tk.W, tk.E))

for widget in mainframe.winfo_children():
        widget.grid_configure(padx=5, pady=5)

root.mainloop()