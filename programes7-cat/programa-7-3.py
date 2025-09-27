class Paraula:
    '''classe per representar paraules. Les paraules estan composades per una forma, un lema i una etiqueta'''
    def __init__(self,forma,lema,etiqueta):
        self.forma=forma
        self.lema=lema
        self.etiqueta=etiqueta
    def torna_forma(self):
        '''Retorna la forma de la paraula'''
        return(self.forma)
    def torna_lema(self):
        '''Retorna el lem de la paraula'''
        return(self.lema)
    def torna_etiqueta(self):
        '''Retorna l'etiqueta de la paraula'''
        return(self.etiqueta)
    def es_lema(self):
        '''Diu si una determinada forma és un lema'''
        if self.forma==self.lema:
            return(True)
        else:
            return(False)
    def categoria(self):
        '''Retorna el nom de la categoria de la paraula'''
        if self.etiqueta.startswith("N"):return("NOM")
        elif self.etiqueta.startswith("V"):return("VERB")
        elif self.etiqueta.startswith("A"):return("VERB")
        elif self.etiqueta.startswith("R"):return("VERB")
        else: return("CATEGORIA TANCADA")
        

print(help(Paraula))
