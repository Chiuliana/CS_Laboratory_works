import tkinter as tk
from tkinter import messagebox
from des_keys_generator import generate_round_keys

def display_round_keys():
    key_input = key_entry.get().replace(" ", "").strip()
    if len(key_input) != 64 or not set(key_input).issubset({'0', '1'}):
        messagebox.showerror("Input Error", "The key must contain exactly 64 bits (0 and 1)!")
        return

    key = [int(bit) for bit in key_input]
    intermediate_steps = generate_round_keys(key)

    # Display results
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, "Intermediate Steps and Generated Round Keys:\n\n")

    # PC-1 Table Result
    result_text.insert(tk.END, "PC-1 Result:\n")
    result_text.insert(tk.END, f"{''.join(map(str, intermediate_steps['PC-1']))}\n\n")

    # Shifts and PC-2 Results
    for i, (shifts, pc2) in enumerate(zip(intermediate_steps["Shifts"], intermediate_steps["PC-2"]), start=1):
        left_half, right_half = shifts
        result_text.insert(tk.END, f"Round {i}:\n")
        result_text.insert(tk.END, f"  Left Half (C{i}): {''.join(map(str, left_half))}\n")
        result_text.insert(tk.END, f"  Right Half (D{i}): {''.join(map(str, right_half))}\n")
        result_text.insert(tk.END, f"  PC-2 Result: {''.join(map(str, pc2))}\n\n")

    # Round Keys
    result_text.insert(tk.END, "Final Round Keys:\n")
    for i, round_key in enumerate(intermediate_steps["Round Keys"], start=1):
        result_text.insert(tk.END, f"K{i}: {''.join(map(str, round_key))}\n")

# GUI Setup
app = tk.Tk()
app.title("DES Key Generation with Intermediate Steps")

tk.Label(app, text="Enter the 64-bit key (0 and 1):").pack(pady=5)
key_entry = tk.Entry(app, width=64)
key_entry.pack(pady=5)

tk.Button(app, text="Generate Round Keys", command=display_round_keys).pack(pady=5)

result_text = tk.Text(app, width=100, height=30)
result_text.pack(pady=10)

app.mainloop()
