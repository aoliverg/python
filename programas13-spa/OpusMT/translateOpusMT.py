from transformers import MarianMTModel, MarianTokenizer

def translate_text(text, model_name):
    """
    Translates a given string using a specific Opus-MT model.
    """
    # 1. Load the tokenizer and the model from Hugging Face
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)

    # 2. Tokenize the input text
    # The 'pt' return_tensors means we are using PyTorch
    inputs = tokenizer(text, return_tensors="pt", padding=True)

    # 3. Generate the translated tokens
    translated_tokens = model.generate(**inputs)

    # 4. Decode the tokens back into a human-readable string
    result = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)
    return result

if __name__ == "__main__":
    # Configuration
    model_id = "Helsinki-NLP/opus-mt-en-es"
    input_sentence = "This is a translation test using OpusMT"

    print("Cargando el modelo y realizando la traducción...")
    
    # Execution
    translation = translate_text(input_sentence, model_id)

    # Output
    print("-" * 30)
    print(f"Texto original:   {input_sentence}")
    print(f"Texto traducido:  {translation}")
    print("-" * 30)
