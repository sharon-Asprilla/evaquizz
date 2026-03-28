import datetime

def tiempo_restante(fecha_inicio, duracion_minutos):
    fin = fecha_inicio + datetime.timedelta(minutes=duracion_minutos)
    return (fin - datetime.datetime.now()).seconds // 60
