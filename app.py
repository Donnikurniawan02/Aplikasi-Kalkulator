import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

# Variabel simbolik
x = sp.symbols('x')

# Fungsi input dari pengguna
fungsi_input = input("Masukkan fungsi aljabar dalam x: ")
fungsi = sp.sympify(fungsi_input)

# Menu pilihan
print("\nPilih operasi:")
print("1. Turunan")
print("2. Integral")
pilihan = input("Masukkan pilihan (1/2): ")

# Operasi berdasarkan pilihan
if pilihan == '1':
    turunan = sp.diff(fungsi, x)
    print(f"\nHasil turunan simbolik dari {fungsi_input}:")
    print("Turunan:", turunan)
    
    # Evaluasi turunan secara numerik
    f_turunan_lambdified = sp.lambdify(x, turunan, modules=['numpy'])
    x_vals = np.linspace(-10, 10, 400)
    y_vals = f_turunan_lambdified(x_vals)
    
    # Gambar grafik
    plt.plot(x_vals, y_vals, label=f"Turunan dari {fungsi_input}")
    plt.title("Grafik Turunan")
    plt.xlabel("x")
    plt.ylabel("f'(x)")
    plt.grid(True)
    plt.legend()
    plt.show()

elif pilihan == '2':
    integral = sp.integrate(fungsi, x)
    print(f"\nHasil integral simbolik dari {fungsi_input}:")
    print("Integral:", integral, "+ C")

    # Evaluasi integral secara numerik (jika fungsi bisa diintegrasi)
    f_integral_lambdified = sp.lambdify(x, integral, modules=['numpy'])
    x_vals = np.linspace(-10, 10, 400)
    y_vals = f_integral_lambdified(x_vals)

    # Gambar grafik
    plt.plot(x_vals, y_vals, label=f"Integral dari {fungsi_input}")
    plt.title("Grafik Integral")
    plt.xlabel("x")
    plt.ylabel("∫f(x) dx")
    plt.grid(True)
    plt.legend()
    plt.show()

else:
    print("Pilihan tidak valid. Silakan pilih 1 atau 2.")
