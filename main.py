import tkinter as tk
from tkinter import ttk
import importlib
from rich.console import Console

console = Console()

ALGO_TYPES = {
    "Classique": {
        "César": "classical.cesar",
        "Affine": "classical.affine",
        "Hill": "classical.hill",
        "Playfair": "classical.playfair",
        "Vigenère": "classical.vigenere"
    },
    "Moderne Symétrique": {
        "AES": "modern.aes",
        "DES": "modern.des",
        "RC4": "modern.rc4",
        "RC6": "modern.rc6"
    },
    "Asymétrique": {
        "RSA": "asymmetric.rsa",
        "ElGamal": "asymmetric.elgamal",
        "Diffie-Hellman": "key_exchange.diffie_hellman"
    },
    "Hashage": {
        "MD5": "hashing.md5",
        "SHA-256": "hashing.sha256"
    },
    "Signature": {
        "DSA": "signatures.signature_dsa"
    }
}

root = tk.Tk()
root.title("Interface Cryptographie")
root.configure(bg="lightblue")
root.geometry("850x550")

# Widgets communs
tk.Label(root, text="Type d'algorithme :", bg="lightblue").grid(row=0, column=0, sticky="w", padx=10, pady=5)
combo_type = ttk.Combobox(root, values=list(ALGO_TYPES.keys()), state="readonly", width=40)
combo_type.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Algorithme :", bg="lightblue").grid(row=1, column=0, sticky="w", padx=10, pady=5)
combo_algo = ttk.Combobox(root, state="readonly", width=40)
combo_algo.grid(row=1, column=1, padx=10, pady=5)

label_text = tk.Label(root, text="Texte :", bg="lightblue")
label_text.grid(row=2, column=0, sticky="w", padx=10, pady=5)
entry_text = tk.Entry(root, width=50)
entry_text.grid(row=2, column=1, padx=10, pady=5)

label_key = tk.Label(root, text="Clé :", bg="lightblue")
label_key.grid(row=3, column=0, sticky="w", padx=10, pady=5)
entry_key = tk.Entry(root, width=50)
entry_key.grid(row=3, column=1, padx=10, pady=5)

frame_ops = tk.Frame(root, bg="lightblue")
frame_ops.grid(row=4, column=0, columnspan=2, pady=10)
var_option = tk.IntVar(value=0)

def update_algos(event):
    algo_type = combo_type.get()
    if algo_type:
        combo_algo['values'] = list(ALGO_TYPES[algo_type].keys())
        combo_algo.set("")

combo_type.bind("<<ComboboxSelected>>", update_algos)

def update_options(event):
    algo_type = combo_type.get()
    algo = combo_algo.get()
    for widget in frame_ops.winfo_children():
        widget.pack_forget()

    # Réinitialiser champs
    label_text.grid(row=2, column=0, sticky="w", padx=10, pady=5)
    entry_text.grid(row=2, column=1, padx=10, pady=5)
    label_key.grid(row=3, column=0, sticky="w", padx=10, pady=5)
    entry_key.grid(row=3, column=1, padx=10, pady=5)

    if algo_type == "Hashage":
        label_key.grid_remove()
        entry_key.grid_remove()

    elif algo_type == "Signature":
        label_key.grid_remove()
        entry_key.grid_remove()
        tk.Radiobutton(frame_ops, text="Signer", variable=var_option, value=0, bg="lightblue").pack(side="left", padx=10)
        tk.Radiobutton(frame_ops, text="Vérifier", variable=var_option, value=1, bg="lightblue").pack(side="left", padx=10)

    elif algo == "Diffie-Hellman":
        label_text.grid_remove()
        entry_text.grid_remove()
        label_key.config(text="Taille de clé (bits) :")
        label_key.grid(row=3, column=0, sticky="w", padx=10, pady=5)
        entry_key.grid(row=3, column=1, padx=10, pady=5)

    elif algo in ["RSA", "ElGamal"]:
        label_key.grid_remove()
        entry_key.grid_remove()
        tk.Radiobutton(frame_ops, text="Chiffrer", variable=var_option, value=0, bg="lightblue").pack(side="left", padx=10)
        tk.Radiobutton(frame_ops, text="Déchiffrer", variable=var_option, value=1, bg="lightblue").pack(side="left", padx=10)

    else:
        tk.Radiobutton(frame_ops, text="Chiffrer", variable=var_option, value=0, bg="lightblue").pack(side="left", padx=10)
        tk.Radiobutton(frame_ops, text="Déchiffrer", variable=var_option, value=1, bg="lightblue").pack(side="left", padx=10)

combo_algo.bind("<<ComboboxSelected>>", update_options)


last_signature_data = None

def executer():
    global last_signature_data
    algo_type = combo_type.get()
    algo = combo_algo.get()
    if not algo_type or not algo:
        console.print("Veuillez choisir un type et un algorithme.", style="bold red")
        return
    module_name = ALGO_TYPES[algo_type][algo]
    try:
        module = importlib.import_module(module_name)
        text = entry_text.get() if entry_text.winfo_ismapped() else None
        key = entry_key.get() if entry_key.winfo_ismapped() else None
        option = var_option.get()


        if algo == "DSA":
            if option == 0:  # Signer
                result = module.process(option, text)
                last_signature_data = result
                console.print(f"[Signature - DSA] signer : {result}", style="bold magenta")
            else:  # Vérifier
                if last_signature_data is None:
                    console.print("Erreur : aucune signature disponible pour vérifier.", style="bold red")
                    return
                result = module.process(option, text, last_signature_data)
                console.print(f"[Signature - DSA] vérifier signature : {result}", style="bold magenta")
            return

        result = module.process(option, text, key)

        if algo == "Diffie-Hellman":
            console.print(f"[{algo_type} - {algo}] Clé partagée : {result}", style="bold magenta")
        elif algo in ["RSA", "ElGamal"]:
            if option == 0:
                console.print(f"[{algo_type} - {algo}] Texte chiffré : {result}", style="bold magenta")
            else:
                console.print(f"[{algo_type} - {algo}] Texte déchiffré : {result}", style="bold magenta")
        elif algo in ["MD5","SHA-256"]:
            console.print(f"[{algo_type} - {algo}] Hash: {result}", style="bold yellow")
        else:
            if option == 0:
                console.print(f"[{algo_type} - {algo}] Résultat chiffrement : {result}", style="bold green")
            else:
                console.print(f"[{algo_type} - {algo}] Résultat déchiffrement : {result}", style="bold blue")

    except Exception as e:
        console.print(f"Erreur ({algo}) : {e}", style="bold red")

tk.Button(root, text="Exécuter", command=executer, bg="lightgreen", width=20).grid(row=5, column=0, columnspan=2, pady=20)

root.mainloop()
