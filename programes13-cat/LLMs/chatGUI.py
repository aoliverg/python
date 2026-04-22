import torch
import threading
import warnings
import tkinter as tk
from tkinter import scrolledtext, messagebox
from transformers import pipeline, logging as transformers_logging

# 1. NETEJA DE CONSOLA
warnings.filterwarnings("ignore")
transformers_logging.set_verbosity_error()

class IAPlayground:
    def __init__(self, root):
        self.root = root
        self.root.title("Python AI Playground - Phi-3.5")
        self.root.geometry("800x1000")  # Una mica més alta per seguretat
        self.root.configure(bg="#f0f2f5")

        self.model_id = "microsoft/Phi-3.5-mini-instruct"
        self.pipe = None
        self.historial = [
            {"role": "system", "content": "Ets un assistent útil que respon en català."}
        ]

        # Creem la interfície abans de carregar el model
        self.crear_interficie()
        
        # Fil per carregar el model
        threading.Thread(target=self.carregar_model, daemon=True).start()

    def crear_interficie(self):
        # --- CONTENIDOR PRINCIPAL ---
        main_frame = tk.Frame(self.root, bg="#f0f2f5")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # 1. TÍTOL I SORTIDA (A DALT)
        tk.Label(main_frame, text="RESPOSTA DE LA IA:", bg="#f0f2f5", font=("Arial", 10, "bold")).pack(anchor="w")
        self.txt_sortida = scrolledtext.ScrolledText(main_frame, height=15, font=("Consolas", 11), state='disabled', bg="#ffffff")
        self.txt_sortida.pack(fill=tk.BOTH, expand=True, pady=(0, 15))

        # 2. TÍTOL I ENTRADA (AL MIG)
        tk.Label(main_frame, text="EL TEU PROMPT (ESCRIU AQUÍ):", bg="#f0f2f5", font=("Arial", 10, "bold")).pack(anchor="w")
        self.txt_entrada = scrolledtext.ScrolledText(main_frame, height=5, font=("Arial", 11))
        self.txt_entrada.pack(fill=tk.X, pady=(0, 10))

        # 3. BOTÓ (A BAIX DE L'ENTRADA)
        self.boto_enviar = tk.Button(
            main_frame, 
            text="GENERAR RESPOSTA", 
            command=self.executar_ia, 
            bg="#28a745", 
            fg="white", 
            font=("Arial", 10, "bold"),
            relief=tk.RAISED,
            cursor="hand2"
        )
        self.boto_enviar.pack(ipadx=20, ipady=8)

        # 4. BARRA D'ESTAT (A BAIX DE TOT)
        self.status_var = tk.StringVar(value="⏳ Carregant model... espera.")
        self.status_bar = tk.Label(self.root, textvariable=self.status_var, bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def carregar_model(self):
        params = {
            "device_map": "auto",
            "trust_remote_code": True,
            "dtype": "auto",
            "model_kwargs": {}
        }
        
        te_cuda = torch.cuda.is_available()
        try:
            import flash_attn
            params["model_kwargs"]["attn_implementation"] = "flash_attention_2"
            params["dtype"] = torch.bfloat16
        except ImportError:
            params["model_kwargs"]["attn_implementation"] = "sdpa" if te_cuda else "eager"

        try:
            self.pipe = pipeline("text-generation", model=self.model_id, **params)
            self.root.after(0, lambda: self.status_var.set("✅ Model a punt. Escriu el teu prompt."))
        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror("Error", f"No s'ha pogut carregar el model: {e}"))

    def executar_ia(self):
        prompt = self.txt_entrada.get("1.0", tk.END).strip()
        if not prompt or self.pipe is None:
            return

        self.boto_enviar.config(state=tk.DISABLED, text="Processant...", bg="#6c757d")
        self.status_var.set("🧠 La IA està treballant en la resposta...")
        
        threading.Thread(target=self.generar_text, args=(prompt,), daemon=True).start()

    def generar_text(self, prompt):
        self.historial.append({"role": "user", "content": prompt})
        try:
            resultats = self.pipe(
                self.historial, 
                max_new_tokens=500,
                do_sample=True,
                temperature=0.7, 
                return_full_text=False
            )
            resposta = resultats[0]['generated_text']
            self.historial.append({"role": "assistant", "content": resposta})
            self.root.after(0, lambda: self.actualitzar_interficie(resposta))
        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror("Error", str(e)))
        finally:
            self.root.after(0, self.restablir_interficie)

    def actualitzar_interficie(self, text):
        self.txt_sortida.configure(state='normal')
        self.txt_sortida.delete("1.0", tk.END)
        self.txt_sortida.insert(tk.END, text)
        self.txt_sortida.configure(state='disabled')
        self.txt_entrada.delete("1.0", tk.END) # Netegem l'entrada per a la següent

    def restablir_interficie(self):
        self.boto_enviar.config(state=tk.NORMAL, text="GENERAR RESPOSTA", bg="#28a745")
        self.status_var.set("✅ Resposta completada.")

if __name__ == "__main__":
    root = tk.Tk()
    app = IAPlayground(root)
    root.mainloop()
