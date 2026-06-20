import argparse
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

def translate_nllb(text, model_name, source_lang, target_lang):
    """
    Traduce texto utilizando el modelo NLLB.
    """
    # 1. Cargar el tokenizador y el modelo
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    # 2. Preparar la entrada
    inputs = tokenizer(text, return_tensors="pt", padding=True)

    # 3. Generar la traducción especificando el código del idioma de destino
    forced_bos_token_id = tokenizer.convert_tokens_to_ids(target_lang)
    translated_tokens = model.generate(
        **inputs, 
        forced_bos_token_id=forced_bos_token_id
    )

    # 4. Decodificar el resultado
    result = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)
    return result

if __name__ == "__main__":
    # --- Configuración de argparse ---
    parser = argparse.ArgumentParser(description="Herramienta de traducción basada en el modelo NLLB de Facebook.")

    # Definición de los parámetros de entrada
    parser.add_argument("--text", type=str, required=True, 
                        help="El texto que quieres traducir (obligatorio).")
    
    parser.add_argument("--model", type=str, default="facebook/nllb-200-distilled-600M", 
                        help="Nombre del modelo en Hugging Face (por defecto: nllb-200-distilled-600M).")
    
    parser.add_argument("--origen", type=str, default="eng_Latn", 
                        help="Código del idioma de origen (ej: eng_Latn, spa_Latn).")
    
    parser.add_argument("--destino", type=str, default="spa_Latn", 
                        help="Código del idioma de destino (ej: spa_Latn, fra_Latn).")

    # Leer los argumentos de la terminal
    args = parser.parse_args()

    # --- Ejecución del proceso ---
    print(f"Cargando el modelo: {args.model}...")
    
    traduccion = translate_nllb(
        text=args.text, 
        model_name=args.model, 
        source_lang=args.origen, 
        target_lang=args.destino
    )

    print("\n" + "="*40)
    print(f"ORIGEN ({args.origen}): {args.text}")
    print(f"DESTINO ({args.destino}): {traduccion}")
    print("="*40)
