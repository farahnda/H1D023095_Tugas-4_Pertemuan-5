% CIRI CIRI GAYA BELAJAR

% DATABASE
:- dynamic ciri_pos/1.
:- dynamic ciri_neg/1.

% FAKTA & ATURAN
gaya_belajar("Visual").
gaya_belajar("Auditori").
gaya_belajar("Kinestetik").

ciri(suka_melihat_gambar, "Visual").
ciri(suka_mendengar_penjelasan, "Auditori").
ciri(suka_berbicara, "Auditori").
ciri(suka_praktik_langsung, "Kinestetik").
ciri(suka_bergerak, "Kinestetik").
ciri(menggambar, "Visual").
ciri(mendengarkan_dengan_tekun, "Auditori").
ciri(menulis_catatan, "Visual").

pertanyaan(suka_melihat_gambar, Y) :-
        Y = "Apakah Anda suka melihat gambar atau grafik saat belajar?".
pertanyaan(suka_mendengar_penjelasan, Y) :-
        Y = "Apakah Anda lebih suka mendengarkan penjelasan daripada membaca?".
pertanyaan(suka_berbicara, Y) :-
        Y = "Apakah Anda suka berbicara atau berdiskusi dalam kelompok saat belajar?".
pertanyaan(suka_praktik_langsung, Y) :-
        Y = "Apakah Anda lebih suka belajar dengan cara langsung mempraktekkan?".
pertanyaan(suka_bergerak, Y) :-
        Y = "Apakah Anda merasa lebih nyaman belajar dengan bergerak?".
pertanyaan(menggambar, Y) :-
        Y = "Apakah Anda lebih suka menggambar atau mencatat dengan gambar?".
pertanyaan(mendengarkan_dengan_tekun, Y) :-
        Y = "Apakah Anda lebih suka mendengarkan penjelasan dengan teliti?".
pertanyaan(menulis_catatan, Y) :-
        Y = "Apakah Anda suka menulis catatan saat belajar?".