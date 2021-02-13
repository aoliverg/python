import codecs
import re
entrada=codecs.open("catalog.xml","r",encoding="utf-8")
salida=codecs.open("catalog.txt","w",encoding="utf-8")
artist=""
title=""
year=""
for linia in entrada:
    linia=linia.rstrip().lstrip()
    if linia.startswith("</cd>"):
        if not artist=="" and not title=="" and not year=="":
            cadena=artist+"\t"+title+"\t"+year
            print(cadena)
            salida.write(cadena+"\n")
    else:
        m_title = re.search('<title>(.+?)</title>', linia)
        if m_title:
            title = m_title.group(1)
        m_artist = re.search('<artist>(.+?)</artist>', linia)
        if m_artist:
            artist = m_artist.group(1)
        m_year = re.search('<year>(.+?)</year>', linia)
        if m_year:
            year = m_year.group(1)
   
