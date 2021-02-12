from langdetect import detect

lang = detect("Metges de família que han de visitar nens perquè els serveis de pediatria del CAP estan desbordats i urgències hospitalàries amb el doble d'activitat. Com cada tardor, el virus respiratori sincicial (VRS), causant de la bronquiolitis, ja fa setmanes que circula i ja ha assolit els nivells d'epidèmia, de manera que ha tensionat els serveis de pediatria dels CAP i els hospitals, com passa també cada temporada.")
print("Lengua texto 1",lang)

lang = detect("Телеканал ссылается на заявку на исследование в Научно-техническую организацию НАТО, к которой получил доступ.Недавние учения на восточной границе НАТО, присутствие в Прибалтике и война на Украине продемонстрировали успешность российской стратегии радиоэлектронной борьбы (РЭБ). И потенциал радиоэлектронных атак (например, подавления), и радиоэлектронное обеспечение (например, обнаружение целей) показывают, что существующая инфраструктура тактической связи НАТО уязвима перед средствами РЭБ и столкнется с серьезными угрозами, - говорится в документе, передает RT.")
print("Lengua texto 2",lang)
