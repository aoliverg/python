import torch
import warnings
from transformers import pipeline, logging as transformers_logging

# 1. LIMPIEZA DE CONSOLA: Silenciamos avisos informativos
warnings.filterwarnings("ignore")
transformers_logging.set_verbosity_error()

def genera_respuesta(prompt, model_id):
    """
    Función básica para enviar una sola pregunta a la IA y recibir una respuesta.
    """
    # Configuramos la pipeline con las mejores prácticas actuales
    pipe = pipeline(
        "text-generation",
        model=model_id,
        device_map="auto",
        trust_remote_code=True,
        dtype="auto", 
        # Por defecto utilizamos 'sdpa' (nativo de PyTorch), que es más rápido que 'eager'
        model_kwargs={"attn_implementation": "sdpa"} 
    )

    # En este script básico, la lista de mensajes solo contiene la pregunta actual
    messages = [
        {"role": "user", "content": prompt},
    ]
    
    print(f"La IA está procesando tu consulta...")
    
    # Ejecución con los parámetros limpios para evitar avisos
    resultado = pipe(
        messages, 
        max_new_tokens=200, 
        do_sample=True,      # Necesario para usar temperature
        temperature=0.7, 
        return_full_text=False,
        max_length=None      # Evita el conflicto con el valor por defecto del modelo
    )
    
    return resultado[0]['generated_text']

if __name__ == "__main__":
    # Recomendamos utilizar la versión 3.5 para mejor calidad en castellano
    model_id = "microsoft/Phi-3.5-mini-instruct"
    
    usuario_prompt = "Explícame en una frase qué es la inteligencia artificial."
    
    respuesta = genera_respuesta(usuario_prompt, model_id)
    
    print("\n" + "-" * 30)
    print(f"PREGUNTA: {usuario_prompt}")
    print(f"RESPUESTA: {respuesta}")
    print("-" * 30)
