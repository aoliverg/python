from PyPDF2 import PdfReader, PdfWriter

def insertar_pdf_en_medio(original, para_insertar, posicion_insercion):
    """Inserta todo el contenido de un PDF dentro de otro en una posición específica."""
    reader_orig = PdfReader(original)
    reader_ins = PdfReader(para_insertar)
    writer = PdfWriter()

    # 1. Copiamos las páginas del original hasta la posición de inserción
    for i in range(posicion_insercion):
        writer.add_page(reader_orig.pages[i])

    # 2. Insertamos TODAS las páginas del segundo PDF
    for page in reader_ins.pages:
        writer.add_page(page)

    # 3. Copiamos el resto de páginas del original
    for i in range(posicion_insercion, len(reader_orig.pages)):
        writer.add_page(reader_orig.pages[i])

    with open("pdf_combinado.pdf", "wb") as f:
        writer.write(f)
    print("¡PDF insertado correctamente!")

def sustituir_pagina(original, para_sustituir, num_pagina_a_cambiar):
    """Sustituye una página concreta del original por la primera página de otro PDF."""
    reader_orig = PdfReader(original)
    reader_sub = PdfReader(para_sustituir)
    writer = PdfWriter()

    for i in range(len(reader_orig.pages)):
        if i == num_pagina_a_cambiar:
            # En lugar de la página original, ponemos la primera del nuevo archivo
            writer.add_page(reader_sub.pages[0])
        else:
            writer.add_page(reader_orig.pages[i])

    with open("pdf_sustituido.pdf", "wb") as f:
        writer.write(f)
    print(f"¡Página {num_pagina_a_cambiar} sustituida con éxito!")

# --- EJEMPLOS DE USO ---
# insertar_pdf_en_medio("trabajo_final.pdf", "anexos.pdf", 5)
# sustituir_pagina("factura_vieja.pdf", "correccion.pdf", 0)
