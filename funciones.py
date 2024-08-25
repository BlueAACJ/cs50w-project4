# Funcion para limpiar el formato en el html 

def limpiarlinea(linea):
    CODES = [
        # fomato sucio / codigo html equivalente 
        ("Ã±","&#241;"),
        ("Ãº","&#225;"),
        ("Ã©","&#233;"),
        ("Ã¡","&#225;"),
        ("Ã³","&#243;"),
        ("Ã¼","&#252;"),
        ("Ã“","&#211;"),

        ("â€™","&#39;"),
        ("â€˜","&#34;"),
        ("Â»","&#34;"),
        ("Â«","&#34;"),
        ("Â","&#94;"),
        ("â€³","&#34;"),
        ("â€²","&#39;"),
        ("â€“","&#45;"),
        ("Ã","&#237;"),
    ] 

    # i &#237; Cambio de ultima porque genera muchos problemas 
    # https://ascii.cl/es/codigos-html.htm

    for anterior,siguiente in CODES:
        linea = linea.replace(anterior, siguiente)
    
    # retornamos el texto limpio 
    return linea
