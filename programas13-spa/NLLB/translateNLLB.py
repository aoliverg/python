from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

def translate_nllb(text, model_name, source_lang, target_lang):
    """
    Translates text using the NLLB model.
    """
    # 1. Carga del tokenizador y del modelo
    # NLLB utiliza las clases Auto para facilitar la carga
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    # 2. Preparar la entrada y especificar el idioma de origen
    inputs = tokenizer(text, return_tensors="pt", padding=True)

    # 3. Generar la traducción especificando el código del idioma de destino
    # forced_bos_token_id le dice al modelo en qué idioma debe traducir
    forced_bos_token_id = tokenizer.convert_tokens_to_ids(target_lang)
    translated_tokens = model.generate(
        **inputs, 
        forced_bos_token_id=forced_bos_token_id
    )

    # 4. Decodificar la salida
    result = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)
    return result

if __name__ == "__main__":
    # Configuración del modelo
    model_id = "facebook/nllb-200-distilled-600M"
    
    # Códigos de idioma: 
    # Español: spa_Latn | Inglés: eng_Latn | Catalán: cat_Latn
    src_code = "eng_Latn" 
    tgt_code = "spa_Latn"
    
    input_sentence = "This is a translated sentence using NLLB."

    print(f"Cargando {model_id}...")
    
    translation = translate_nllb(input_sentence, model_id, src_code, tgt_code)

    print("-" * 30)
    print(f"Origen ({src_code}): {input_sentence}")
    print(f"Destino ({tgt_code}): {translation}")
    print("-" * 30)
