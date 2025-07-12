import tkinter as tk
from tkinter import messagebox
from sympy import symbols, diff, integrate, lambdify, sympify
import matplotlib.pyplot as plt
import numpy as np

# Inisialisasi variabel simbolik
x = symbols('x')

def hitung():
    fungsi_input = entry.get()
    try:
        fungsi = sympify(fungsi_input)

        turunan = diff(fungsi, x)
        integral = integrate(fungsi, x)

        result_text = f"Fungsi: {fungsi}\n"
        result_text += f"Turunan: {turunan}\n"
        result_text += f"Integral: {integral}\n"

        result_label.config(text=result_text)
        plot_fungsi(fungsi, turunan)

    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {e}")

def plot_fungsi(f, turunan_f):
    fx = lambdify(x, f, 'numpy')
    fdx = lambdify(x, turunan_f, 'numpy')

    X = np.linspace(-10, 10, 400)
    Y = fx(X)
    Y_diff = fdx(X)

    plt.figure(figsize=(8, 4))
    plt.plot(X, Y, label='Fungsi Asli', color='blue')
    plt.plot(X, Y_diff, label='Turunan', color='red', linestyle='--')
    plt.title("Grafik Fungsi dan Turunannya")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

# GUI
app = tk.Tk()
app.title("Kalkulator Integral dan Turunan")

tk.Label(app, text="Masukkan Fungsi (gunakan x):").pack()
entry = tk.Entry(app, width=40)
entry.pack()

tk.Button(app, text="Hitung", command=hitung).pack(pady=10)

result_label = tk.Label(app, text="", justify="left")
result_label.pack()

app.mainloop()
