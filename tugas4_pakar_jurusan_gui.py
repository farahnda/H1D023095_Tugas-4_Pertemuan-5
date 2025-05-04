import tkinter as tk
from tkinter import ttk
from pyswip import Prolog
from tkinter import messagebox

# Inisialisasi Prolog
prolog = Prolog()
prolog.consult("tugas4_pakar_jurusan_gui.pl")

jurusan = list()
minat = dict()
index_jurusan = 0
index_minat = 0
current_jurusan = ""
current_minat = ""

def mulai_rekomendasi():
        global jurusan, minat, index_jurusan, index_minat

        # Bersihkan database Prolog
        prolog.retractall("minat_pos(_)")
        prolog.retractall("minat_neg(_)")

        start_btn.configure(state=tk.DISABLED)
        yes_btn.configure(state=tk.NORMAL)
        no_btn.configure(state=tk.NORMAL)

        # Mendapatkan daftar jurusan dan minat
        jurusan = [j["X"].decode() for j in list(prolog.query("jurusan(X)"))]
        for j in jurusan:
                minat[j] = [m["X"] for m in list(prolog.query(f'minat(X, "{j}")'))]

        index_jurusan = 0
        index_minat = -1

        pertanyaan_selanjutnya()

def pertanyaan_selanjutnya(ganti_jurusan=False):
        global current_jurusan, current_minat, index_jurusan, index_minat

        # Atur index jurusan
        if ganti_jurusan:
            # Ganti ke jurusan selanjutnya
                index_jurusan += 1
                index_minat = -1

        # Apabila daftar jurusan sudah habis berarti tidak terdeteksi jurusan
        if index_jurusan >= len(jurusan):
                hasil_rekomendasi()
                return
        current_jurusan = jurusan[index_jurusan]

        # Atur index minat
        index_minat += 1

        # Apabila semua minat dari jurusan habis, berarti terdeteksi jurusan tsb
        if index_minat >= len(minat[current_jurusan]):
                hasil_rekomendasi(current_jurusan)
                return
        current_minat = minat[current_jurusan][index_minat]

        #  Cek status minat di database prolog
        if list(prolog.query(f"minat_pos({current_minat})")):
                pertanyaan_selanjutnya()
                return
        elif list(prolog.query(f"minat_neg({current_minat})")):
                pertanyaan_selanjutnya(ganti_jurusan=True)
                return

        # Mendapatkan pertanyaan baru
        pertanyaan = list(prolog.query(f"pertanyaan({current_minat}, Y)"))[0]["Y"].decode()
        
        # Set pertanyaan ke kotak pertanyaan
        tampilkan_pertanyaan(pertanyaan)

def tampilkan_pertanyaan(pertanyaan):
        kotak_pertanyaan.configure(state=tk.NORMAL)
        kotak_pertanyaan.delete(1.0, tk.END)
        kotak_pertanyaan.insert(tk.END, pertanyaan)
        kotak_pertanyaan.configure(state=tk.DISABLED)

def jawaban(jwb):
        if jwb:
                prolog.assertz(f"minat_pos({current_minat})")
                pertanyaan_selanjutnya()
        else:
                prolog.assertz(f"minat_neg({current_minat})")
                pertanyaan_selanjutnya(ganti_jurusan=True)

def hasil_rekomendasi(_=None):
        hasil = dict()

        for jr in jurusan:
                jumlah_cocok = 0
                for c in minat[jr]:
                        if list(prolog.query(f"minat_pos({c})")):
                                jumlah_cocok += 1
                hasil[jr] = jumlah_cocok

        jurusan_terbaik = max(hasil, key=hasil.get)
        if hasil[jurusan_terbaik] > 0:
                messagebox.showinfo("Hasil Rekomendasi", f"Anda terdeteksi {jurusan_terbaik}.")
        else:
                messagebox.showinfo("Hasil Rekomendasi", "Tidak terdeteksi jurusan.")

        yes_btn.configure(state=tk.DISABLED)
        no_btn.configure(state=tk.DISABLED)
        start_btn.configure(state=tk.NORMAL)

# GUI
root = tk.Tk()
root.title("Sistem Pakar Rekomendasi Jurusan Kuliah")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Label(mainframe, text="Aplikasi Rekomendasi Jurusan Kuliah", font=("Arial", 16)).grid(column=0, row=0, columnspan=3)
ttk.Label(mainframe, text="Kolom Pertanyaan:").grid(column=0, row=1)

kotak_pertanyaan = tk.Text(mainframe, height=5, width=43, state=tk.DISABLED)
kotak_pertanyaan.grid(column=0, row=2, columnspan=3)

no_btn = ttk.Button(mainframe, text="Tidak", state=tk.DISABLED, command=lambda: jawaban(False))
no_btn.grid(column=1, row=3, sticky=(tk.W, tk.E))

yes_btn = ttk.Button(mainframe, text="Ya", state=tk.DISABLED, command=lambda: jawaban(True))
yes_btn.grid(column=2, row=3, sticky=(tk.W, tk.E))

start_btn = ttk.Button(mainframe, text="Mulai Rekomendasi", command=mulai_rekomendasi)
start_btn.grid(column=1, row=4, columnspan=2, sticky=(tk.W, tk.E))

for widget in mainframe.winfo_children():
        widget.grid_configure(padx=5, pady=5)

root.mainloop()