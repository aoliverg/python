import torch
import warnings
import logging
from transformers import pipeline, logging as transformers_logging

# 1. LIMPIEZA DE CONSOLA: Silenciamos avisos informativos y de deprecación
warnings.filterwarnings("ignore")
transformers_logging.set_verbosity_error()

def detectar_mejor_configuracion():
    """
    Analiza el sistema para elegir la mejor implementación de atención (Attention).
    """
    # Configuración base
    params = {
        "device_map": "auto",
        "trust_remote_code": True,
        "dtype": "auto",
        "model_kwargs": {}
    }

    tiene_cuda = torch.cuda.is_available()
    
    # Intentamos detectar Flash Attention 2
    tiene_flash_attn = False
    try:
        import flash_attn
        tiene_flash_attn = True
    except ImportError:
        pass

    # Selección del motor según el hardware
    if tiene_cuda and tiene_flash_attn:
        print("🚀 [MODO]: Flash Attention 2 (Máximo rendimiento)")
        params["model_kwargs"]["attn_implementation"] = "flash_attention_2"
        params["dtype"] = torch.bfloat16
    elif tiene_cuda:
        print("✅ [MODO]: GPU activo (SDPA)")
        params["model_kwargs"]["attn_implementation"] = "sdpa"
    else:
        print("💻 [MODO]: CPU activo (Modo lento)")
        params["model_kwargs"]["attn_implementation"] = "eager"
        params["dtype"] = torch.float32
        params["device_map"] = "cpu"

    return params

def iniciar_chat():
    # Modelo de Microsoft Phi-3.5 optimizado
    model_id = "microsoft/Phi-3.5-mini-instruct"
    
    config_params = detectar_mejor_configuracion()
    
    print(f"Cargando el modelo {model_id}...\n(Esto puede tardar unos segundos)")
    
    # Inicializamos la pipeline una sola vez
    pipe = pipeline(
        "text-generation",
        model=model_id,
        **config_params
    )

    # Lista de mensajes que actúa como memoria (Contexto)
    # El mensaje 'system' define el comportamiento de la IA
    historial = [
        {"role": "system", "content": "Eres un asistente útil y amable que responde siempre en castellano."}
    ]

    print("\n" + "="*50)
    print("🤖 CHAT INTERACTIVO CON PHI-3.5")
    print("Escribe 'salir' para cerrar el programa.")
    print("="*50)

    while True:
        # Entrada del usuario
        usuario_input = input("\nTú: ")
        
        if usuario_input.lower() in ["salir", "exit", "quit", "adios"]:
            print("IA: ¡Adiós! Que tengas un buen día.")
            break
            
        # Guardamos la pregunta en el historial
        historial.append({"role": "user", "content": usuario_input})
        
        # Generación de la respuesta
        print("La IA está pensando...", end="\r")
        
        resultados = pipe(
            historial, 
            max_new_tokens=500,
            do_sample=True,      # Activa el uso de la temperatura
            temperature=0.7, 
            return_full_text=False,
            clean_up_tokenization_spaces=True
        )
        
        respuesta_text = resultados[0]['generated_text']
        
        # Guardamos la respuesta de la IA en el historial para mantener el contexto
        historial.append({"role": "assistant", "content": respuesta_text})
        
        # Mostramos el resultado final limpio
        print(f"IA: {respuesta_text}")

if __name__ == "__main__":
    try:
        iniciar_chat()
    except KeyboardInterrupt:
        print("\n\nSe ha cerrado el chat de forma abrupta. ¡Hasta la próxima!")
