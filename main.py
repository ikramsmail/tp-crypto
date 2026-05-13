import tkinter as tk
from tkinter import ttk
import importlib


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
        "DSA": "signatures.signature_dsa",
        "RSA": "signatures.signature_rsa",
        "ElGamal": "signatures.signature_el_gamal"
    }
}


root = tk.Tk()
root.title("CryptoSecure")
root.geometry("1200x720")
root.configure(bg="#0b1120")
root.minsize(1100, 680)

style = ttk.Style()
style.theme_use("clam")

style.configure(
    "Custom.TCombobox",
    fieldbackground="#111827",
    background="#111827",
    foreground="white",
    bordercolor="#2563eb",
    lightcolor="#2563eb",
    darkcolor="#2563eb",
    arrowcolor="white",
    padding=8
)

header = tk.Frame(root, bg="#111827", height=80)
header.pack(fill="x")

title = tk.Label(
    header,
    text="Advanced Cryptography Algorithms",
    bg="#111827",
    fg="white",
    font=("Segoe UI", 24, "bold")
)

title.place(x=25, y=18)

subtitle = tk.Label(
    header,
    text="",
    bg="#111827",
    fg="#9ca3af",
    font=("Segoe UI", 10)
)

subtitle.place(x=28, y=55)

container = tk.Frame(root, bg="#0b1120")
container.pack(fill="both", expand=True, padx=20, pady=20)

left_panel = tk.Frame(
    container,
    bg="#111827",
    width=420,
    highlightbackground="#1f2937",
    highlightthickness=1
)

left_panel.pack(side="left", fill="y")

right_panel = tk.Frame(
    container,
    bg="#111827",
    highlightbackground="#1f2937",
    highlightthickness=1
)

right_panel.pack(side="right", fill="both", expand=True, padx=(20, 0))

panel_title = tk.Label(
    left_panel,
    text="Configuration",
    bg="#111827",
    fg="white",
    font=("Segoe UI", 18, "bold")
)

panel_title.pack(anchor="w", padx=25, pady=(25, 5))

panel_subtitle = tk.Label(
    left_panel,
    text="Configure your cryptographic algorithm",
    bg="#111827",
    fg="#9ca3af",
    font=("Segoe UI", 10)
)

panel_subtitle.pack(anchor="w", padx=25, pady=(0, 25))

def create_label(parent, text):

    return tk.Label(
        parent,
        text=text,
        bg="#111827",
        fg="#d1d5db",
        font=("Segoe UI", 10, "bold")
    )

label_type = create_label(left_panel, "Algorithm Type")
label_type.pack(anchor="w", padx=25)

combo_type = ttk.Combobox(
    left_panel,
    values=list(ALGO_TYPES.keys()),
    state="readonly",
    width=35,
    style="Custom.TCombobox",
    font=("Segoe UI", 10)
)

combo_type.pack(padx=25, pady=(8, 20))

label_algo = create_label(left_panel, "Algorithm")
label_algo.pack(anchor="w", padx=25)

combo_algo = ttk.Combobox(
    left_panel,
    state="readonly",
    width=35,
    style="Custom.TCombobox",
    font=("Segoe UI", 10)
)

combo_algo.pack(padx=25, pady=(8, 20))

label_text = create_label(left_panel, "Input Text")
label_text.pack(anchor="w", padx=25)

entry_text = tk.Entry(
    left_panel,
    bg="#0f172a",
    fg="white",
    insertbackground="white",
    relief="flat",
    font=("Consolas", 11),
    width=38,
    bd=12
)

entry_text.pack(padx=25, pady=(8, 20))

label_key = create_label(left_panel, "Key")
label_key.pack(anchor="w", padx=25)

entry_key = tk.Entry(
    left_panel,
    bg="#0f172a",
    fg="white",
    insertbackground="white",
    relief="flat",
    font=("Consolas", 11),
    width=38,
    bd=12
)

entry_key.pack(padx=25, pady=(8, 25))

frame_ops = tk.Frame(left_panel, bg="#111827")
frame_ops.pack(pady=10)

var_option = tk.IntVar(value=0)

terminal_header = tk.Frame(
    right_panel,
    bg="#0f172a",
    height=45
)

terminal_header.pack(fill="x")

dot1 = tk.Label(
    terminal_header,
    text="●",
    fg="#ef4444",
    bg="#0f172a",
    font=("Arial", 12)
)

dot1.place(x=15, y=10)

dot2 = tk.Label(
    terminal_header,
    text="●",
    fg="#f59e0b",
    bg="#0f172a",
    font=("Arial", 12)
)

dot2.place(x=35, y=10)

dot3 = tk.Label(
    terminal_header,
    text="●",
    fg="#22c55e",
    bg="#0f172a",
    font=("Arial", 12)
)

dot3.place(x=55, y=10)

terminal_title = tk.Label(
    terminal_header,
    text="Secure Output Console",
    bg="#0f172a",
    fg="#9ca3af",
    font=("Consolas", 10)
)

terminal_title.pack(pady=10)

terminal_frame = tk.Frame(
    right_panel,
    bg="#020617"
)

terminal_frame.pack(fill="both", expand=True)

scrollbar = tk.Scrollbar(terminal_frame)
scrollbar.pack(side="right", fill="y")

terminal = tk.Text(
    terminal_frame,
    bg="#020617",
    fg="#22c55e",
    font=("Consolas", 11),
    relief="flat",
    bd=20,
    insertbackground="white",
    yscrollcommand=scrollbar.set,
    wrap="word"
)

terminal.pack(fill="both", expand=True)

scrollbar.config(command=terminal.yview)

terminal.tag_config("red", foreground="#ef4444")
terminal.tag_config("green", foreground="#22c55e")
terminal.tag_config("blue", foreground="#3b82f6")
terminal.tag_config("yellow", foreground="#facc15")
terminal.tag_config("cyan", foreground="#06b6d4")
terminal.tag_config("white", foreground="#f8fafc")
terminal.tag_config("magenta", foreground="#d946ef")

def terminal_print(message, color="white"):

    terminal.insert(tk.END, message + "\n", color)
    terminal.see(tk.END)

def update_algos(event):

    algo_type = combo_type.get()

    if algo_type:

        combo_algo["values"] = list(ALGO_TYPES[algo_type].keys())
        combo_algo.set("")

combo_type.bind("<<ComboboxSelected>>", update_algos)

def update_options(event):

    algo_type = combo_type.get()
    algo = combo_algo.get()

    for widget in frame_ops.winfo_children():
        widget.destroy()

    # RESET
    label_text.pack(anchor="w", padx=25)
    entry_text.pack(padx=25, pady=(8, 20))

    label_key.pack(anchor="w", padx=25)
    entry_key.pack(padx=25, pady=(8, 25))

    # DEFAULT
    label_key.config(text="Key")

    if algo_type == "Hashage":

        label_key.pack_forget()
        entry_key.pack_forget()

    elif algo_type == "Signature":

        label_key.pack_forget()
        entry_key.pack_forget()

        tk.Radiobutton(
            frame_ops,
            text="Sign",
            variable=var_option,
            value=0,
            bg="#111827",
            fg="white",
            selectcolor="#1e293b",
            font=("Segoe UI", 10)
        ).pack(side="left", padx=10)

        tk.Radiobutton(
            frame_ops,
            text="Verify",
            variable=var_option,
            value=1,
            bg="#111827",
            fg="white",
            selectcolor="#1e293b",
            font=("Segoe UI", 10)
        ).pack(side="left", padx=10)

    elif algo == "Affine":

        label_key.config(
            text="Key (ex: 2,3)"
        )

        tk.Radiobutton(
            frame_ops,
            text="Encrypt",
            variable=var_option,
            value=0,
            bg="#111827",
            fg="white",
            selectcolor="#1e293b",
            font=("Segoe UI", 10)
        ).pack(side="left", padx=10)

        tk.Radiobutton(
            frame_ops,
            text="Decrypt",
            variable=var_option,
            value=1,
            bg="#111827",
            fg="white",
            selectcolor="#1e293b",
            font=("Segoe UI", 10)
        ).pack(side="left", padx=10)

    elif algo == "Hill":

        label_key.config(
            text="Matrix Key (ex: 2,3,1,4)"
        )

        tk.Radiobutton(
            frame_ops,
            text="Encrypt",
            variable=var_option,
            value=0,
            bg="#111827",
            fg="white",
            selectcolor="#1e293b",
            font=("Segoe UI", 10)
        ).pack(side="left", padx=10)

        tk.Radiobutton(
            frame_ops,
            text="Decrypt",
            variable=var_option,
            value=1,
            bg="#111827",
            fg="white",
            selectcolor="#1e293b",
            font=("Segoe UI", 10)
        ).pack(side="left", padx=10)

    elif algo == "Diffie-Hellman":

        label_text.pack_forget()
        entry_text.pack_forget()

        label_key.config(
            text="Key Size (bits)"
        )

    else:

        tk.Radiobutton(
            frame_ops,
            text="Encrypt",
            variable=var_option,
            value=0,
            bg="#111827",
            fg="white",
            selectcolor="#1e293b",
            font=("Segoe UI", 10)
        ).pack(side="left", padx=10)

        tk.Radiobutton(
            frame_ops,
            text="Decrypt",
            variable=var_option,
            value=1,
            bg="#111827",
            fg="white",
            selectcolor="#1e293b",
            font=("Segoe UI", 10)
        ).pack(side="left", padx=10)

combo_algo.bind("<<ComboboxSelected>>", update_options)

last_signature_data = None

def executer():

    global last_signature_data

    algo_type = combo_type.get()
    algo = combo_algo.get()

    if not algo_type or not algo:

        terminal_print(
            "[ERROR] Please select algorithm type and algorithm.",
            "red"
        )

        return

    module_name = ALGO_TYPES[algo_type][algo]

    try:

        module = importlib.import_module(module_name)

        text = entry_text.get() if entry_text.winfo_ismapped() else None
        key = entry_key.get() if entry_key.winfo_ismapped() else None
        option = var_option.get()

        terminal_print(
            f"$ Running {algo}...",
            "cyan"
        )

        terminal_print(
            "--------------------------------------------------",
            "white"
        )

        if algo_type == "Signature":

            if option == 0:

                result = module.process(option, text)

                last_signature_data = result

                terminal_print(
                    "[SIGNATURE GENERATED]",
                    "magenta"
                )

                terminal_print(str(result), "green")

            else:

                if last_signature_data is None:

                    terminal_print(
                        "[ERROR] No signature available.",
                        "red"
                    )

                    return

                result = module.process(
                    option,
                    text,
                    last_signature_data
                )

                terminal_print(
                    f"[VERIFY RESULT] {result}",
                    "cyan"
                )

            terminal_print("", "white")
            return
        result = module.process(option, text, key)

        if algo == "Diffie-Hellman":

            terminal_print(
                f"[SHARED KEY]\n{result}",
                "cyan"
            )

        elif algo in ["MD5", "SHA-256"]:

            terminal_print(
                f"[HASH OUTPUT]\n{result}",
                "yellow"
            )

        else:

            if option == 0:

                terminal_print(
                    "[ENCRYPTED OUTPUT]",
                    "green"
                )

                terminal_print(str(result), "white")

            else:

                terminal_print(
                    "[DECRYPTED OUTPUT]",
                    "blue"
                )

                terminal_print(str(result), "white")

        terminal_print("", "white")

    except Exception as e:

        terminal_print(
            f"[ERROR] {e}",
            "red"
        )
execute_btn = tk.Button(
    left_panel,
    text="Execute",
    command=executer,
    bg="#2563eb",
    fg="white",
    activebackground="#1d4ed8",
    activeforeground="white",
    relief="flat",
    font=("Segoe UI", 12, "bold"),
    cursor="hand2",
    padx=15,
    pady=12
)

execute_btn.pack(fill="x", padx=25, pady=30)

footer = tk.Label(
    root,
    text="CryptoSecure © 2026 | Secure Cryptographic Environment",
    bg="#0b1120",
    fg="#6b7280",
    font=("Segoe UI", 9)
)

footer.pack(pady=10)

root.mainloop()