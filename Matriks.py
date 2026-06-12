import Ade088

A = [
    [2, 5, 1],
    [5, 0, 6],
    [1, 8, 8]
]

B = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

C = [
    [1, 2],
    [3, 4]
]

D = [
    [5, 6],
    [7, 8]
]

print("=== MATRIKS 3x3 ===")

print("\nPenjumlahan:")
Ade088.tampilkan_matriks(Ade088.penjumlahan_matriks_3x3(A, B))

print("\nPengurangan:")
Ade088.tampilkan_matriks(Ade088.pengurangan_matriks_3x3(A, B))

print("\nPerkalian:")
Ade088.tampilkan_matriks(Ade088.perkalian_matriks_3x3(A, B))

print("\nDeterminan:")
print(Ade088.determinan_3x3(A))

print("\nTranspose:")
Ade088.tampilkan_matriks(Ade088.transpose_3x3(A))


print("\n=== MATRIKS 2x2 ===")

print("\nPenjumlahan:")
Ade088.tampilkan_matriks(Ade088.penjumlahan_matriks_2x2(C, D))

print("\nPengurangan:")
Ade088.tampilkan_matriks(Ade088.pengurangan_matriks_2x2(C, D))

print("\nPerkalian:")
Ade088.tampilkan_matriks(Ade088.perkalian_matriks_2x2(C, D))

print("\nDeterminan:")
print(Ade088.determinan_2x2(C))

print("\nTranspose:")
Ade088.tampilkan_matriks(Ade088.transpose_2x2(C))