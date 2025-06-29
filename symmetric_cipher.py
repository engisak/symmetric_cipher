import tkinter as tk
from tkinter import ttk, messagebox

# Charset of 72 characters
CHARSET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()"

def char_to_index(c):
    return CHARSET.index(c)

def index_to_char(i):
    return CHARSET[i % len(CHARSET)]

def derive_round_key(master_key, round_num):
    return [(k ^ round_num) % 10 for k in master_key]

def encrypt(plaintext, master_key, rounds=2, salt="@#"):
    full_input = salt + plaintext.replace(" ", "")
    indexes = [char_to_index(c) for c in full_input]
    for r in range(1, rounds + 1):
        key = derive_round_key(master_key, r)
        indexes = [((idx ^ key[i % 8]) + (i + 1) + r) % len(CHARSET) for i, idx in enumerate(indexes)]
    return ''.join(index_to_char(i) for i in indexes)

def decrypt(ciphertext, master_key, rounds=2, salt_len=2):
    indexes = [char_to_index(c) for c in ciphertext]
    for r in range(rounds, 0, -1):
        key = derive_round_key(master_key, r)
        indexes = [((idx - (i + 1) - r) % len(CHARSET)) ^ key[i % 8] for i, idx in enumerate(indexes)]
    return ''.join(index_to_char(i) for i in indexes)[salt_len:]

def run_cipher():
    try:
        text = text_input.get("1.0", tk.END).strip().replace(" ", "")
        rounds = int(rounds_input.get())
        key = [int(x) for x in key_input.get().strip().split()]
        if len(key) != 8:
            raise ValueError("Master key must contain exactly 8 integers.")
        if mode.get() == "Encrypt":
            result = encrypt(text, key, rounds)
        else:
            result = decrypt(text, key, rounds)
        result_output.config(state="normal")
        result_output.delete(0, tk.END)
        result_output.insert(0, result)
        result_output.config(state="readonly")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI Layout
root = tk.Tk()
root.title("🔐 Symmetric Encryption GUI (KDF Based)")
root.geometry("650x450")
root.resizable(False, False)
root.configure(bg="#f2f2f2")

tk.Label(root, text="Symmetric Encryption Tool with KDF", bg="#f2f2f2", font=("Helvetica", 16, "bold")).pack(pady=10)

container = tk.Frame(root, bg="#f2f2f2")
container.pack(pady=5, padx=20, fill="x")

tk.Label(container, text="Enter Text:", bg="#f2f2f2", font=("Helvetica", 10)).grid(row=0, column=0, sticky="e")
text_input = tk.Text(container, width=50, height=3, font=("Courier", 10))
text_input.grid(row=0, column=1, padx=10, pady=5)

tk.Label(container, text="Rounds:", bg="#f2f2f2", font=("Helvetica", 10)).grid(row=1, column=0, sticky="e")
rounds_input = tk.Entry(container, width=10)
rounds_input.insert(0, "")
rounds_input.grid(row=1, column=1, sticky="w", pady=5)

tk.Label(container, text="Master Key (8 numbers):", bg="#f2f2f2", font=("Helvetica", 10)).grid(row=2, column=0, sticky="e")
key_input = tk.Entry(container, width=40)
key_input.insert(0, "")
key_input.grid(row=2, column=1, pady=5)

mode = tk.StringVar(value="Encrypt")
mode_frame = tk.Frame(root, bg="#f2f2f2")
mode_frame.pack(pady=5)
ttk.Label(mode_frame, text="Mode:").pack(side="left", padx=(0, 10))
ttk.Radiobutton(mode_frame, text="Encrypt", variable=mode, value="Encrypt").pack(side="left")
ttk.Radiobutton(mode_frame, text="Decrypt", variable=mode, value="Decrypt").pack(side="left")

tk.Button(root, text="Run", font=("Helvetica", 11, "bold"), bg="#4CAF50", fg="white", padx=20, pady=5, command=run_cipher).pack(pady=10)

tk.Label(root, text="Result:", bg="#f2f2f2", font=("Helvetica", 10)).pack()
result_output = tk.Entry(root, width=70, font=("Courier", 10), state="readonly", justify="center")
result_output.pack(pady=(0, 15))

tk.Label(root, text="© 2025 - Custom Symmetric Cipher with KDF - Ahmed Ak", bg="#f2f2f2", font=("Arial", 8)).pack(side="bottom", pady=5)

root.mainloop()
