import random

# Komputer memilih angka secara acak dari 1 sampai 10
angka_rahasia = random.randint(1, 10)

print("Tebak angka dari 1 sampai 10")
tebakan = int(input("Masukkan tebakanmu: "))

# Cek tebakan
if tebakan == angka_rahasia:
    print("🎉 Selamat! Kamu menebak dengan benar.")
else:
    print(f"😢 Salah. Angka yang benar adalah {angka_rahasia}.")
