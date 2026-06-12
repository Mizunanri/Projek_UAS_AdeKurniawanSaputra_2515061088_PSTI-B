def tampilkan_matriks(m):
    for baris in m:
        print(baris)

def penjumlahan_matriks_2x2(A, B):
    hasil = []
    for i in range(2):
        baris = []
        for j in range(2):
            baris.append(A[i][j] + B[i][j])
        hasil.append(baris)
    return hasil

def penjumlahan_matriks_3x3(A, B):
    hasil = []
    for i in range(3):
        baris = []
        for j in range(3):
            baris.append(A[i][j] + B[i][j])
        hasil.append(baris)
    return hasil

def pengurangan_matriks_2x2(A, B):
    hasil = []
    for i in range(2):
        baris = []
        for j in range(2):
            baris.append(A[i][j] - B[i][j])
        hasil.append(baris)
    return hasil

def pengurangan_matriks_3x3(A, B):
    hasil = []
    for i in range(3):
        baris = []
        for j in range(3):
            baris.append(A[i][j] - B[i][j])
        hasil.append(baris)
    return hasil

def perkalian_matriks_2x2(A, B):
    hasil = []
    for i in range(2):
        baris = []
        for j in range(2):
            total = 0
            for k in range(2):
                total += A[i][k] * B[k][j]
            baris.append(total)
        hasil.append(baris)
    return hasil

def perkalian_matriks_3x3(A, B):
    hasil = []
    for i in range(3):
        baris = []
        for j in range(3):
            total = 0
            for k in range(3):
                total += A[i][k] * B[k][j]
            baris.append(total)
        hasil.append(baris)
    return hasil

def determinan_2x2(m):
    return (m[0][0] * m[1][1]) - (m[0][1] * m[1][0])

def determinan_3x3(m):
    return (
        m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
        - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
        + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
    )

def transpose_2x2(m):
    return [
        [m[0][0], m[1][0]],
        [m[0][1], m[1][1]]
    ]

def transpose_3x3(m):
    return [
        [m[0][0], m[1][0], m[2][0]],
        [m[0][1], m[1][1], m[2][1]],
        [m[0][2], m[1][2], m[2][2]]
    ]