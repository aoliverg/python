import torch
import warnings
from transformers import pipeline, logging as transformers_logging

# 1. NETEJA DE CONSOLA: Silenciem avisos informatius
warnings.filterwarnings("ignore")
transformers_logging.set_verbosity_error()

def genera_resposta(prompt, model_id):
    """
    Funció bàsica per enviar una sola pregunta a la IA i rebre una resposta.
    """
    # Configurem la pipeline amb les millors pràctiques actuals
    pipe = pipeline(
        "text-generation",
        model=model_id,
        device_map="auto",
        trust_remote_code=True,
        dtype="auto", 
        # Per defecte fem servir 'sdpa' (natiu de PyTorch), que és més ràpid que 'eager'
        model_kwargs={"attn_implementation": "sdpa"} 
    )

    # En aquest script bàsic, la llista de missatges només conté la pregunta actual
    messages = [
        {"role": "user", "content": prompt},
    ]
    
    print(f"IA està processant la teva consulta...")
    
    # Execució amb els paràmetres nets per evitar avisos
    resultat = pipe(
        messages, 
        max_new_tokens=200, 
        do_sample=True,      # Necessari per usar temperature
        temperature=0.7, 
        return_full_text=False,
        max_length=None      # Evita el conflicte amb el valor per defecte del model
    )
    
    return resultat[0]['generated_text']

if __name__ == "__main__":
    # Recomanem fer servir la versió 3.5 per millor qualitat en català
    model_id = "microsoft/Phi-3.5-mini-instruct"
    
    usuari_prompt = "Explica'm en una frase què és la intel·ligència artificial."
    
    resposta = genera_resposta(usuari_prompt, model_id)
    
    print("\n" + "-" * 30)
    print(f"PREGUNTA: {usuari_prompt}")
    print(f"RESPOSTA: {resposta}")
    print("-" * 30)
