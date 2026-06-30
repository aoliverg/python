import whisper

# 1. Cargamos el modelo.
# El modelo "tiny" o "base" son ideales para ordenadores sin mucha potencia.
print("Cargando el modelo de lenguaje...")
model = whisper.load_model("base")

# 2. Indicamos el archivo de audio que queremos transcribir
# Puede ser un .mp3, .wav o incluso el audio de un vídeo .mp4
archivo_audio = "audio.ogg"

print(f"Transcribiendo el archivo '{archivo_audio}'... Esto puede tardar un poco.")
resultado = model.transcribe(archivo_audio)

# 3. Mostramos el texto final y el idioma detectado
print("\n--- TRANSCRIPCIÓN FINAL ---")
print(f"Idioma detectado: {resultado['language']}")
print(f"Texto: {resultado['text']}")

# Guardamos el resultado en un archivo de texto
with open("transcripcion.txt", "w", encoding="utf-8") as f:
    f.write(resultado['text'])
