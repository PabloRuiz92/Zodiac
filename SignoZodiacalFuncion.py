
diccionario_aspecto = {
    "CAPRICORNIO": "C:\cosas\Downloads\pildoras\phyton\ejercicios\isaac\Zodiac\imagenes\Collectible_Capricorn_appearance.png",
    "ACUARIO": "imagenes\Collectible_Aquarius_appearance.png",
    "PISCIS": "imagenes\Collectible_Pisces_appearance.png",    
    "ARIES": "imagenes\Collectible_Aries_appearance.png",
    "TAURO": "imagenes\Collectible_Taurus_appearance.png",
    "GEMINIS": "imagenes\Collectible_Gemini_appaerance2.png",
    "CANCER": "imagenes\Collectible_Cancer_appearance.png",
    "LEO": "imagenes\Collectible_Leo_appearance.png",
    "VIRGO": "imagenes\Collectible_Virgo_appearance.png",    
    "LIBRA": "imagenes\Collectible_Libra_appearance.png",
    "ESCORPIO": "imagenes\Collectible_Scorpio_appearance.png",
    "SAGITARIO": "imagenes\Collectible_Sagittarius_appearance.png"
}

diccionario_signo = {
    "CAPRICORNIO": "imagenes\Collectible_Capricorn_icon.png",
    "ACUARIO": "imagenes\Collectible_Aquarius_icon.png",
    "PISCIS": "imagenes\Collectible_Pisces_icon.png",    
    "ARIES": "imagenes\Collectible_Aries_icon.png",
    "TAURO": "imagenes\Collectible_Taurus_icon.png",
    "GEMINIS": "imagenes\Collectible_Gemini_icon.png",
    "CANCER": "imagenes\Collectible_Cancer_icon.png",
    "LEO": "imagenes\Collectible_Leo_icon.png",
    "VIRGO": "imagenes\Collectible_Virgo_icon.png",    
    "LIBRA": "imagenes\Collectible_Libra_icon.png",
    "ESCORPIO": "imagenes\Collectible_Scorpio_icon.png",
    "SAGITARIO": "imagenes\Collectible_Sagittarius_icon.png"
}

def Signo_zodiacal(mes, dia):
    signoZodiacal=""
    if int(mes)==1:
        if 1<=int(dia) and int(dia)<=19:
            signoZodiacal="CAPRICORNIO"
        else:
            signoZodiacal="ACUARIO"
    if int(mes)==2:
        if 1<=int(dia) and int(dia)<=18:
            signoZodiacal="ACUARIO"
        else:
            signoZodiacal="PISCIS"
    if int(mes)==3:
        if 1<=int(dia) and int(dia)<=20:
            signoZodiacal="PISCIS"
        else:
            signoZodiacal="ARIES"
    if int(mes)==4:
        if 1<=int(dia) and int(dia)<=19:
            signoZodiacal="ARIES"
        else:
            signoZodiacal="TAURO"
    if int(mes)==5:
        if 1<=int(dia) and int(dia)<=20:
            signoZodiacal="TAURO"
        else:
            signoZodiacal="GEMINIS"
    if int(mes)==6:
        if 1<=int(dia) and int(dia)<=20:
            signoZodiacal="GEMINIS"
        else:
            signoZodiacal="CANCER"
    if int(mes)==7:
        if 1<=int(dia) and int(dia)<=22:
            signoZodiacal="CANCER"
        else:
            signoZodiacal="LEO"
    if int(mes)==8:
        if 1<=int(dia) and int(dia)<=22:
            signoZodiacal="LEO"
        else:
            signoZodiacal="VIRGO"
    if int(mes)==9:
        if 1<=int(dia) and int(dia)<=22:
            signoZodiacal="VIRGO"
        else:
            signoZodiacal="LIBRA"   
    if int(mes)==10:
        if 1<=int(dia) and int(dia)<=22:
            signoZodiacal="LIBRA"
        else:
            signoZodiacal="ESCORPIO"
    if int(mes)==11:
        if 1<=int(dia) and int(dia)<=21:
            signoZodiacal="ESCORPIO"
        else:
            signoZodiacal="SAGITARIO"
    if int(mes)==12:
        if 1<=int(dia) and int(dia)<=21:
            signoZodiacal="SAGITARIO"
        else:
            signoZodiacal="CAPRICORNIO"

    return signoZodiacal