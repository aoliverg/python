def universal(etiqueta):
    if etiqueta.startswith("N"): etiqueta_universal="NOUN"
    elif etiqueta.startswith("V"): etiqueta_universal="VERB"
    elif etiqueta.startswith("A"): etiqueta_universal="ADJ"
    elif etiqueta.startswith("R"): etiqueta_universal="ADV"
    else: etiqueta_universal="X"
    return(etiqueta_universal)
    

tag="NCMS"
tag_u=universal(tag)
print(tag,tag_u)


