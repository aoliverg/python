import torch
import warnings
import logging
from transformers import pipeline, logging as transformers_logging

# 1. NETEJA DE CONSOLA: Silenciem avisos informatius i de deprecació
warnings.filterwarnings("ignore")
transformers_logging.set_verbosity_error()

def detectar_millor_configuracio():
    """
    Analitza el sistema per triar la millor implementació d'atenció (Attention).
    """
    # Configuració base
    params = {
        "device_map": "auto",
        "trust_remote_code": True,
        "dtype": "auto",
        "model_kwargs": {}
    }

    te_cuda = torch.cuda.is_available()
    
    # Intentem detectar Flash Attention 2
    te_flash_attn = False
    try:
        import flash_attn
        te_flash_attn = True
    except ImportError:
        pass

    # Selecció del motor segons maquinari
    if te_cuda and te_flash_attn:
        print("🚀 [MODE]: Flash Attention 2 (Màxim rendiment)")
        params["model_kwargs"]["attn_implementation"] = "flash_attention_2"
        params["dtype"] = torch.bfloat16
    elif te_cuda:
        print("✅ [MODE]: GPU actiu (SDPA)")
        params["model_kwargs"]["attn_implementation"] = "sdpa"
    else:
        print("💻 [MODE]: CPU actiu (Mode lent)")
        params["model_kwargs"]["attn_implementation"] = "eager"
        params["dtype"] = torch.float32
        params["device_map"] = "cpu"

    return params

def iniciar_xat():
    # Model de Microsoft Phi-3.5 optimitzat
    model_id = "microsoft/Phi-3.5-mini-instruct"
    
    config_params = detectar_millor_configuracio()
    
    print(f"Carregant el model {model_id}...\n(Això pot trigar uns segons)")
    
    # Inicialitzem la pipeline una sola vegada
    pipe = pipeline(
        "text-generation",
        model=model_id,
        **config_params
    )

    # Llista de missatges que actua com a memòria (Context)
    # El missatge 'system' defineix el comportament de la IA
    historial = [
        {"role": "system", "content": "Ets un assistent útil i amable que respon sempre en català."}
    ]

    print("\n" + "="*50)
    print("🤖 XAT INTERACTIU AMB PHI-3.5")
    print("Escriu 'sortir' per tancar el programa.")
    print("="*50)

    while True:
        # Entrada de l'usuari
        usuari_input = input("\nTu: ")
        
        if usuari_input.lower() in ["sortir", "exit", "quit", "adeu"]:
            print("IA: Adeu! Que tinguis un bon dia.")
            break
            
        # Guardem la pregunta a l'historial
        historial.append({"role": "user", "content": usuari_input})
        
        # Generació de la resposta
        print("IA està pensant...", end="\r")
        
        resultats = pipe(
            historial, 
            max_new_tokens=500,
            do_sample=True,      # Activa l'ús de la temperatura
            temperature=0.7, 
            return_full_text=False,
            clean_up_tokenization_spaces=True
        )
        
        resposta_text = resultats[0]['generated_text']
        
        # Guardem la resposta de la IA a l'historial per mantenir el context
        historial.append({"role": "assistant", "content": resposta_text})
        
        # Mostrem el resultat final net
        print(f"IA: {resposta_text}")

if __name__ == "__main__":
    try:
        iniciar_xat()
    except KeyboardInterrupt:
        print("\n\nS'ha tancat el xat bruscament. Fins la propera!")
