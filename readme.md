# ImaGeprek - A simple image compression tool

> Program kompresi gambar dengan memanfaatkan algoritma SVD dalam bentuk website lokal sederhana.
>
> > _Tugas Besar 2 IF2123 Aljabar Linier dan Geometri_ <br>  _Aplikasi Nilai Eigen dan Vektor Eigen dalam Kompresi Gambar_ <br> _Semester I 2021/2022_ <br>
## Table of Contents

- [General Info](#general-information)
- [Technologies Used](#technologies-used)
- [Features](#features)
- [Screenshots](#screenshots)
- [Setup](#setup)
- [Usage](#usage)
  <!-- * [Room for Improvement](#room-for-improvement) -->
  <!-- * [Acknowledgements](#acknowledgements) -->
- [Contact](#contact)

## General Information

<p> Gambar adalah salah satu bentuk media yang populer digunakan untuk menyajikan informasi. 
Gambar banyak dipertukarkan di dunia digital melalui file-file yang mengandung gambar tersebut.
Dalam transmisi dan penyimpanan gambar digital, seringkali ditemukan masalah karena ukuran file gambar digital yang cenderung
besar.
Untuk mengatasi hal tersebut, suatu gambar digital dapat dikompresi menjadi file gambar yang lebih kecil. 
Salah satu algoritma yang dapat digunakan untuk mengkompresi gambar adalah algoritma SVD (Singular Value Decomposition).
Algoritma SVD didasarkan pada teorema dalam aljabar linier yang mengatakan bahwa sebuah matriks dua dimensi dapat dipecah menjadi hasil perkalian 
dari 3 sub-matriks. 
Gambar digital direpresentasikan oleh matriks yang mengandung elemen-elemen gambar. 
Dengan SVD, matriks gambar tersebut dipecah menjadi 3 sub-matriks kemudian direkonstruksi dengan suatu batasan sehingga didapatkan gambar yang mirip dengan gambar yang aslinya dan tentunya dengan ukuran file yang lebih kecil dari file aslinya. </p> <br>

_Program ini dibuat sebagai pemenuhan Tugas Besar 2 IF2123 Aljabar Linier dan Geometri Semester I 2021/2022._

## Technologies Used

### Languages
- Python
- Javascript

### Frameworks / Libraries
- Connexion[swagger-ui] + Flask
- ReactJS
- Numpy / Jax Numpy
- Pillow

## Features

Fitur yang dihadirkan oleh website ini adalah:

- Menerima gambar dalam berbagai format (.jpg, .png, .jpeg, .gif, .bmp, .tiff, .psd, dst. [Support List](https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html)).
- Menampilkan gambar input, output, runtime algoritma, dan persentase hasil kompresi gambar (perubahan jumlah pixel gambar).
- Output hasil kompresi dapat diunduh melalui website
- Kompresi gambar tetap mempertahankan warna dari gambar asli
- Kompresi gambar tetap memertahankan transparansi dari gambar asli, misal untuk gambar dengan format .png dan background transparan

## Screenshots

<!-- ![Example screenshot](./img/screenshot.png)
If you have screenshots you'd like to share, include them here. -->

## Directory Listing

```
├── README.md
└── src
    ├── backend
    │   ├── api.py               [Main Operation API]
    │   ├── app.py               [App Factory]
    │   ├── requirements.txt     [Requirements List]
    │   └── swagger.yml          [API spec in OAS 3.0]
    ├── frontend
    │   ├── package-lock.json
    │   ├── package.json     
    │   ├── public               [Static Assets]
    │   └── src                  [JSX Source]
    │       └── components       [Components]
    └── library
        ├── alingeo
        │   ├── imaging
        │   │   └── compress.py  [Compress Class]
        │   └── matriks
        │       ├── eigen.py     [EigenSolver Class]
        │       └── svd.py       [SVDSolver Class]
        └── setup.py
```


## Setup

Clone repository ini terlebih dahulu.

### A. Frontend
1. **[RECOMMENDED]** Gunakan NodeJS, atau pastikan NodeJS sudah ter-_install_ di device.
2. Pastikan sedang berada di folder `src/frontend`.
3. Jalankan perintah `npm install` untuk memasang semua `node_modules` yang diperlukan.
4. Tunggu proses instalasi hingga selesai. 
<!-- What are the project requirements/dependencies? Where are they listed? A requirements.txt or a Pipfile.lock file perhaps? Where is it located?```

Proceed to describe how to install / setup one's local environment / get started with the project. -->
### B. Library
1. **[RECOMMENDED]** Gunakan virtual environment Python baru.
2. Change directory ke `src/library`.
3. Install package dengan command berikut:
    ```
    pip install .
    ```
    
    > Untuk pengembangan, jalankan `pip install -e .` sehingga package terinstall dalam edit mode.
4. **[OPTIONAL]** Untuk dapat menggunakan mode GPU, kamu **harus menginstall** CUDA dan cuDNN terlebih dahulu, kemudian `jaxlib`. Setelah itu, kamu dapat menginstall package dengan extras `gpu`
    ```
    pip install .[gpu]
    ```
    Perhatikan bahwa `jaxlib` hanya bisa dijalankan pada OS Linux/Mac. Untuk Windows, dapat menginstall CUDA, cuDNN dan `jaxlib` di WSL2. Cara instalasi dapat dilihat [disini](https://github.com/google/jax#pip-installation-gpu-cuda). Informasi lebih lanjut tentang JAX bisa lihat [disini](https://jax.readthedocs.io/en/latest/notebooks/quickstart.html).
    
    > Terdapat extras lain yaitu `jax-cpu` jika ingin menggunakan `jax` sebagai backend untuk mode CPU.

### C. Backend
1. **[RECOMMENDED]** Gunakan virtual environment yang sama dengan instalasi Library sebelumnya.
2. Pastikan library `alingeo` sebelumnya telah terinstall.
3. Change directory ke `src/backend`.
3. Install requirements dengan command:
    ```
    pip install -r requirements.txt
    ```

## Usage

### A. Frontend
1. Pastikan Anda berada di folder `src/frontend`
2. Jalankan perintah `npm start`
3. Website akan terbuka di _browser_ di port `localhost`
4. Ada beberapa opsi antarmuka yang dapat diubah sesuai keinginan:
    * _Slider_ rasio Eigen untuk menentukan kualitas hasil akhir kompresi (_default_ = 20)
    * Input skala resolusi untuk menentukan perbandingan resolusi akhir kompresi dalam persentase (_default_ = 100)
    * Input banyaknya iterasi untuk proses kompresi (_default_ = 2)
    * _Checkbox_ untuk kompresi gambar dengan layer _alpha_ 
5. Setelah mengisi semua opsi, gambar akan dikirim ke _backend_ untuk diproses. Apabila gambar selesai diproses, gambar akan dikirimkan ke _frontend_ beserta waktu dan persentase kompresi. Pengguna juga bisa mengunduh hasil gambar ke _local_.

### B. Library
Library dapat digunakan sebagai module python yang bisa diimport oleh program lain.
Beberapa sample program yang dapat digunakan sebagai referensi:
1. Melakukan pencarian nilai eigen dan vektornya

    ```py
    import numpy as np
    from alingeo.matriks.eigen import EigenSolver

    solver = EigenSolver()
    matrix = np.random(10, 10)
    eigen_vectors, eigen_values = solver.calcEigens(matrix)
    ```
2. Melakukan dekomposisi SVD dari sebuah matriks

    ```py
    import numpy as np
    from alingeo.matriks.svd import SVDSolver

    solver = SVDSolver()
    matrix = np.random(10,15)
    U, sigma, VT = solver.calculate(matrix)
    ```
3. Melakukan kompresi gambar dengan dekomposisi SVD

    ```py
    from io import BytesIO
    from alingeo.imaging.compress import CompressSVD

    compressor = CompressSVD()
    with open('sample.png', 'rb') as f:
        res, _, _ = compressor.compress(f, scale=0.3)
        res.save('sample-opt.png')
    ```
### C. Backend
1. Gunakan virtual environment sebelumnya, change directory ke `src/backend`. Pastikan package `alingeo` sudah terinstall.
2. Jalankan flask pada direktori yang sama dengan command berikut:
    ```
    flask run
    ```
3. Untuk melakukan kompresi, dapat melakukan pemanggilan pada endpoint `[POST] /v1/compress`
4. Backend dijalankan oleh spesifikasi OAS 3.0 dan memiliki `swagger-ui` sehingga dapat membaca dokumentasi dari API. Silahkan lihat dokumentasi pada endpoint `/v1/doc` untuk informasi cara menggunakan API lebih lanjut.
    
    > Untuk localhost, dokumentasi API dapat diakses pada URL `http://localhost/v1/doc`

<!-- ## Room for Improvement
Include areas you believe need improvement / could be improved. Also add TODOs for future development.

Room for improvement:
- Improvement to be done 1
- Improvement to be done 2

To do:
- Feature to be added 1
- Feature to be added 2 -->

<!-- ## Acknowledgements
Give credit here.
- This project was inspired by...
- This project was based on [this tutorial](https://www.example.com).
- Many thanks to... -->

## Contact

Dibuat oleh Kelompok 30 - Newo Social Credit
- Amar Fadil (13520103) <a href="https://github.com/marfgold1">GitHub</a>
- Owen Christian Wijaya (13520124) <a href="https://github.com/clumsyyyy">GitHub</a>
- Fachry Dennis Heraldi (13520139) <a href="https://github.com/dennisheraldi">GitHub</a>
