import hashlib

def generar_clave(clave: str):
    return hashlib.sha256(clave.encode()).hexdigest()

def validar_clave(clave_ingresada, clave_guardada):
    return generar_clave(clave_ingresada) == clave_guardada
