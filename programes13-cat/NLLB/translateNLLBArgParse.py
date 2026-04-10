
import argparse
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

def translate_nllb(text, model_name, source_lang, target_lang):
    """
    Tradueix text utilitzant el model NLLB.
    """
    # 1. Carregar el tokenitzador i el model
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    # 2. Preparar l'entrada
    inputs = tokenizer(text, return_tensors="pt", padding=True)

    # 3. Generar la traducció especificant el codi de l'idioma de destí
    forced_bos_token_id = tokenizer.convert_tokens_to_ids(target_lang)
    translated_tokens = model.generate(
        **inputs, 
        forced_bos_token_id=forced_bos_token_id
    )

    # 4. Descodificar el resultat
    result = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)
    return result

if __name__ == "__main__":
    # --- Configuració de l'argparse ---
    parser = argparse.ArgumentParser(description="Eina de traducció basada en el model NLLB de Facebook.")

    # Definició dels paràmetres d'entrada
    parser.add_argument("--text", type=str, required=True, 
                        help="El text que vols traduir (obligatori).")
    
    parser.add_argument("--model", type=str, default="facebook/nllb-200-distilled-600M", 
                        help="Nom del model a Hugging Face (per defecte: nllb-200-distilled-600M).")
    
    parser.add_argument("--origen", type=str, default="eng_Latn", 
                        help="Codi de l'idioma d'origen (ex: eng_Latn, spa_Latn).")
    
    parser.add_argument("--desti", type=str, default="cat_Latn", 
                        help="Codi de l'idioma de destí (ex: cat_Latn, fra_Latn).")

    # Llegir els arguments de la terminal
    args = parser.parse_args()

    # --- Execució del procés ---
    print(f"Carregant el model: {args.model}...")
    
    traduccio = translate_nllb(
        text=args.text, 
        model_name=args.model, 
        source_lang=args.origen, 
        target_lang=args.desti
    )

    print("\n" + "="*40)
    print(f"ORIGEN ({args.origen}): {args.text}")
    print(f"DESTÍ  ({args.desti}): {traduccio}")
    print("="*40)
