import tkinter as tk
from tkinter import messagebox
from des_keys_generator import generate_round_keys

def display_round_keys():
    key_input = key_entry.get()
    if len(key_input) != 64 or not set(key_input).issubset({'0', '1'}):
        messagebox.showerror("Input Error", "Cheia trebuie să conțină 64 de biți (0 și 1)!")
        return

    key = [int(bit) for bit in key_input]
    round_keys = generate_round_keys(key)

    result_text.delete(1.0, tk.END)
    for i, round_key in enumerate(round_keys, start=1):
        result_text.insert(tk.END, f"K{i}: {''.join(map(str, round_key))}\n")

app = tk.Tk()
app.title("DES Round Key Generator")

tk.Label(app, text="Introduceți cheia de 64 biți:").pack(pady=5)
key_entry = tk.Entry(app, width=64)
key_entry.pack(pady=5)

tk.Button(app, text="Generează Cheile de Rundă", command=display_round_keys).pack(pady=5)

result_text = tk.Text(app, width=80, height=20)
result_text.pack(pady=5)

app.mainloop()
