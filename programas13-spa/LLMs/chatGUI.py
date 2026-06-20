import torch
import threading
import warnings
import tkinter as tk
from tkinter import scrolledtext, messagebox
from transformers import pipeline, logging as transformers_logging

# 1. LIMPIEZA DE CONSOLA
warnings.filterwarnings("ignore")
transformers_logging.set_verbosity_error()

class IAPlayground:
    def __init__(self, root):
        self.root = root
        self.root.title("Python AI Playground - Phi-3.5")
        self.root.geometry("800x1000")  # Un poco más alta por seguridad
        self.root.configure(bg="#f0f2f5")

        self.model_id = "microsoft/Phi-3.5-mini-instruct"
        self.pipe = None
        self.historial = [
            {"role": "system", "content": "Eres un asistente útil que responde en castellano."}
        ]

        # Creamos la interfaz antes de cargar el modelo
        self.crear_interfaz()
        
        # Hilo para cargar el modelo
        threading.Thread(target=self.cargar_model, daemon=True).start()

    def crear_interfaz(self):
        # --- CONTENEDOR PRINCIPAL ---
        main_frame = tk.Frame(self.root, bg="#f0f2f5")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # 1. TÍTULO Y SALIDA (ARRIBA)
        tk.Label(main_frame, text="RESPUESTA DE LA IA:", bg="#f0f2f5", font=("Arial", 10, "bold")).pack(anchor="w")
        self.txt_salida = scrolledtext.ScrolledText(main_frame, height=15, font=("Consolas", 11), state='disabled', bg="#ffffff")
        self.txt_salida.pack(fill=tk.BOTH, expand=True, pady=(0, 15))

        # 2. TÍTULO Y ENTRADA (EN MEDIO)
        tk.Label(main_frame, text="TU PROMPT (ESCRIBE AQUÍ):", bg="#f0f2f5", font=("Arial", 10, "bold")).pack(anchor="w")
        self.txt_entrada = scrolledtext.ScrolledText(main_frame, height=5, font=("Arial", 11))
        self.txt_entrada.pack(fill=tk.X, pady=(0, 10))

        # 3. BOTÓN (ABAJO DE LA ENTRADA)
        self.boto_enviar = tk.Button(
            main_frame, 
            text="GENERAR RESPUESTA", 
            command=self.ejecutar_ia, 
            bg="#28a745", 
            fg="white", 
            font=("Arial", 10, "bold"),
            relief=tk.RAISED,
            cursor="hand2"
        )
        self.boto_enviar.pack(ipadx=20, ipady=8)

        # 4. BARRA DE ESTADO (ABAJO DEL TODO)
        self.status_var = tk.StringVar(value="⏳ Cargando modelo... espera.")
        self.status_bar = tk.Label(self.root, textvariable=self.status_var, bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def cargar_model(self):
        params = {
            "device_map": "auto",
            "trust_remote_code": True,
            "dtype": "auto",
            "model_kwargs": {}
        }
        
        tiene_cuda = torch.cuda.is_available()
        try:
            import flash_attn
            params["model_kwargs"]["attn_implementation"] = "flash_attention_2"
            params["dtype"] = torch.bfloat16
        except ImportError:
            params["model_kwargs"]["attn_implementation"] = "sdpa" if tiene_cuda else "eager"

        try:
            self.pipe = pipeline("text-generation", model=self.model_id, **params)
            self.root.after(0, lambda: self.status_var.set("✅ Modelo listo. Escribe tu prompt."))
        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror("Error", f"No se ha podido cargar el modelo: {e}"))

    def ejecutar_ia(self):
        prompt = self.txt_entrada.get("1.0", tk.END).strip()
        if not prompt or self.pipe is None:
            return

        self.boto_enviar.config(state=tk.DISABLED, text="Procesando...", bg="#6c757d")
        self.status_var.set("🧠 La IA está trabajando en la respuesta...")
        
        threading.Thread(target=self.generar_text, args=(prompt,), daemon=True).start()

    def generar_text(self, prompt):
        self.historial.append({"role": "user", "content": prompt})
        try:
            resultados = self.pipe(
                self.historial, 
                max_new_tokens=500,
                do_sample=True,
                temperature=0.7, 
                return_full_text=False
            )
            respuesta = resultados[0]['generated_text']
            self.historial.append({"role": "assistant", "content": respuesta})
            self.root.after(0, lambda: self.actualizar_interfaz(respuesta))
        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror("Error", str(e)))
        finally:
            self.root.after(0, self.restablecer_interfaz)

    def actualizar_interfaz(self, text):
        self.txt_salida.configure(state='normal')
        self.txt_salida.delete("1.0", tk.END)
        self.txt_salida.insert(tk.END, text)
        self.txt_salida.configure(state='disabled')
        self.txt_entrada.delete("1.0", tk.END) # Limpiamos la entrada para la siguiente

    def restablecer_interfaz(self):
        self.boto_enviar.config(state=tk.NORMAL, text="GENERAR RESPUESTA", bg="#28a745")
        self.status_var.set("✅ Respuesta completada.")

if __name__ == "__main__":
    root = tk.Tk()
    app = IAPlayground(root)
    root.mainloop()
