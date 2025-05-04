% MINAT JURUSAN KULIAH

% DATABASE
:- dynamic minat_pos/1.
:- dynamic minat_neg/1.

% FAKTA & ATURAN
jurusan("Teknik Informatika").
jurusan("Kedokteran").
jurusan("Akuntansi").
jurusan("Hukum").
jurusan("Sastra Inggris").
jurusan("Desain Komunikasi Visual").
jurusan("Psikologi").

% MINAT-MINAT
minat(tertarik_pemrograman, "Teknik Informatika").
minat(logika_kuat, "Teknik Informatika").
minat(suka_matematika, "Teknik Informatika").
minat(tertarik_anatomi, "Kedokteran").
minat(sabar_dan_teliti, "Kedokteran").
minat(suka_biologi, "Kedokteran").
minat(suka_menganalisis_data, "Akuntansi").
minat(tertarik_keuangan, "Akuntansi").
minat(teratur_dan_rinci, "Akuntansi").
minat(tertarik_perdebatan, "Hukum").
minat(berpikir_kritis, "Hukum").
minat(percaya_diri_dalam_berargumen, "Hukum").
minat(suka_membaca_fiksi, "Sastra Inggris").
minat(tertarik_budaya_asing, "Sastra Inggris").
minat(suka_menulis, "Sastra Inggris").
minat(suka_menggambar, "Desain Komunikasi Visual").
minat(kreatif_dan_imajinatif, "Desain Komunikasi Visual").
minat(tertarik_desain, "Desain Komunikasi Visual").
minat(peduli_perasaan_orang, "Psikologi").
minat(tertarik_dengan_perilaku_manusia, "Psikologi").
minat(suka_mendengarkan_cerita_orang, "Psikologi").

% PERTANYAAN
pertanyaan(tertarik_pemrograman, "Apakah Anda tertarik dengan pemrograman atau membuat aplikasi?").
pertanyaan(logika_kuat, "Apakah Anda merasa memiliki kemampuan logika yang baik?").
pertanyaan(suka_matematika, "Apakah Anda suka pelajaran matematika?").
pertanyaan(tertarik_anatomi, "Apakah Anda tertarik mempelajari anatomi tubuh manusia?").
pertanyaan(sabar_dan_teliti, "Apakah Anda orang yang sabar dan teliti?").
pertanyaan(suka_biologi, "Apakah Anda suka pelajaran biologi?").
pertanyaan(suka_menganalisis_data, "Apakah Anda suka menganalisis data atau angka?").
pertanyaan(tertarik_keuangan, "Apakah Anda tertarik dengan dunia keuangan atau akuntansi?").
pertanyaan(teratur_dan_rinci, "Apakah Anda orang yang teratur dan detail?").
pertanyaan(tertarik_perdebatan, "Apakah Anda suka berdiskusi atau berdebat tentang hukum dan isu sosial?").
pertanyaan(berpikir_kritis, "Apakah Anda sering berpikir secara kritis terhadap suatu peristiwa?").
pertanyaan(percaya_diri_dalam_berargumen, "Apakah Anda percaya diri saat menyampaikan argumen di depan orang?").
pertanyaan(suka_membaca_fiksi, "Apakah Anda suka membaca novel atau cerita fiksi?").
pertanyaan(tertarik_budaya_asing, "Apakah Anda tertarik dengan bahasa dan budaya asing?").
pertanyaan(suka_menulis, "Apakah Anda suka menulis puisi, cerita, atau artikel?").
pertanyaan(suka_menggambar, "Apakah Anda suka menggambar atau mendesain?").
pertanyaan(kreatif_dan_imajinatif, "Apakah Anda merasa memiliki imajinasi dan kreativitas yang tinggi?").
pertanyaan(tertarik_desain, "Apakah Anda tertarik dengan desain grafis atau visual?").
pertanyaan(peduli_perasaan_orang, "Apakah Anda peka terhadap perasaan orang lain?").
pertanyaan(tertarik_dengan_perilaku_manusia, "Apakah Anda tertarik memahami perilaku dan pikiran manusia?").
pertanyaan(suka_mendengarkan_cerita_orang, "Apakah Anda suka mendengarkan cerita dan membantu orang lain?").
