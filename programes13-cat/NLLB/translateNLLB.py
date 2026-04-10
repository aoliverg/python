from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

def translate_nllb(text, model_name, source_lang, target_lang):
    """
    Translates text using the NLLB model.
    """
    # 1. Load the tokenizer and model
    # NLLB uses Auto classes for easier loading
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    # 2. Prepare the input and specify the source language
    inputs = tokenizer(text, return_tensors="pt", padding=True)

    # 3. Generate the translation specifying the target language code
    # forced_bos_token_id tells the model which language to translate into
    forced_bos_token_id = tokenizer.convert_tokens_to_ids(target_lang)
    translated_tokens = model.generate(
        **inputs, 
        forced_bos_token_id=forced_bos_token_id
    )

    # 4. Decode the output
    result = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)
    return result

if __name__ == "__main__":
    # Model configuration
    model_id = "facebook/nllb-200-distilled-600M"
    
    # Language Codes: 
    # Spanish: spa_Latn | English: eng_Latn | Catalan: cat_Latn
    src_code = "eng_Latn" 
    tgt_code = "spa_Latn"
    
    input_sentence = "This is a translated sentence using NLLB."

    print(f"Loading {model_id}...")
    
    translation = translate_nllb(input_sentence, model_id, src_code, tgt_code)

    print("-" * 30)
    print(f"Source ({src_code}): {input_sentence}")
    print(f"Target ({tgt_code}): {translation}")
    print("-" * 30)
