import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# --- CONFIGURACIÓN ---
FS = 44100  # Frecuencia de muestreo (estandard de CD)
MIDA_BLOC = 1024  # Cuántas muestras analizamos cada vez
DURADA_FINESTRA = 200  # Cuántos datos mostramos en el gráfico de la onda

# Creamos la figura con dos gráficos (Onda y Espectro)
fig, (ax_ona, ax_freq) = plt.subplots(2, 1, figsize=(10, 7))

# Configuramos el gráfico de la onda
x_ona = np.arange(0, MIDA_BLOC)
line_ona, = ax_ona.plot(x_ona, np.zeros(MIDA_BLOC), color='cyan')
ax_ona.set_ylim(-0.1, 0.1) # Sensibilidad del micrófono
ax_ona.set_title("Señal del Micrófono (Onda)")
ax_ona.axis('off')

# Configuramos el gráfico del espectro
x_freq = np.linspace(0, FS/2, MIDA_BLOC//2)
line_freq, = ax_freq.plot(x_freq, np.zeros(MIDA_BLOC//2), color='magenta')
ax_freq.set_xlim(0, 4000)  # Hasta 4kHz (donde se concentra la voz humana)
ax_freq.set_ylim(0, 1)
ax_freq.set_title("Análisis de Frecuencias (Espectro)")

# Variable para guardar los datos que llegan
datos_audio = np.zeros(MIDA_BLOC)

def audio_callback(indata, frames, time, status):
    """Esta función se ejecuta cada vez que el micrófono tiene datos nuevos."""
    global datos_audio
    # Cogemos solo el primer canal (mono)
    datos_audio = indata[:, 0]

def actualizar_grafico(frame):
    """Actualiza las líneas del gráfico con los datos actuales."""
    # 1. Actualizar Onda
    line_ona.set_ydata(datos_audio)

    # 2. Calcular FFT (Espectro)
    fft_data = np.abs(np.fft.fft(datos_audio))[:MIDA_BLOC//2]
    line_freq.set_ydata(fft_data)

    # 3. Dibujar una barra de volumen en la consola (opcional)
    volumen = np.linalg.norm(datos_audio) * 10
    print(f"Volumen: {'█' * int(volumen)}", end='\r')

    return line_ona, line_freq

# Iniciamos la entrada de sonido
stream = sd.InputStream(channels=1, samplerate=FS, callback=audio_callback, blocksize=MIDA_BLOC)

with stream:
    # Animación de Matplotlib para refrescar la pantalla
    ani = FuncAnimation(fig, actualizar_grafico, interval=30, blit=True)
    plt.tight_layout()
    plt.show()
