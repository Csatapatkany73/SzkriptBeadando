import random
import matplotlib.pyplot as plt
from SzRT_modul import SzRTClass, szrt_function

# Alap GUI ablak
import tkinter as tk

def main():
    root = tk.Tk()
    root.title("App - Szentpéteri Roland Tamás")

    # Saját modul osztályának használata
    obj = SzRTClass("Példa")
    tk.Label(root, text=obj.describe()).pack()

    # Eseménykezelés
    def plot_chart():
        data = [random.randint(1, 100) for _ in range(10)]
        szrt_function(data)  # Hívás a saját függvényre
        plt.plot(data)
        plt.title("Random Adatok Grafikonja")
        plt.show()

    tk.Button(root, text="Grafikon Generálása", command=plot_chart).pack()

    root.mainloop()

if __name__ == "__main__":
    main()
