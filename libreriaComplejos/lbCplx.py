import math
def sum_cplx(a,b):
    """calcula la suma entre dos numeros complejos
    (tupla,tupla) -> tupla
    """
    real = a[0] + b[0]
    img = a[1] + b[1]
    return (real,img)
def prod_cplx(a,b):
    """calcula la multiplicacion de dos numeros complejos
    (tupla,tupla) -> tupla
    """
    real = a[0]*b[0] - a[1]*b[1]
    img = a[0]*b[1] + a[1]*b[0]
    return (real,img)
def diff_cplx(a,b):
    """calcula la resta entre dos numeros complejos
    (tupla,tupla) -> tupla
    """
    real = a[0] - b[0]
    img = a[1] - b[1]
    return (real,img)
def div_cplx(a,b):
    """calcula la division entre dos numeros complejos
    (tupla,tupla) -> tupla
    """
    real = (a[0]*b[0] + b[1]*a[1])/((b[0])**2 + (b[1])**2)
    img = (b[0]*a[1] - a[0]*b[1])/((b[0])**2 + (b[1])**2)
    return (real,img)
def modulo(a):
    """calcula el modulo de un numero complejo
    tupla -> natural
    """
    result = math.sqrt(a[0]**2 + a[1]**2)
    return result
def conju(a):
    """retorna el conjugado de un numero complejo
    tupla -> tupla
    """
    return (a[0],a[1]*(-1))
def faseCplx(a):
    """retorna la fase de un numero complejo
    tupla -> int
    """
    fase = math.atan(a[1]/a[0])
    return fase
def crt_plr(a):
    """pasar de representacion cartesiana a polar
    tupla -> tupla
    """
    modul = modulo(a)
    fase = faseCplx(a)
    cuad = iden_cuad(a)
    if cuad == 2:
        fase = math.pi - abs(fase)
    elif cuad == 3:
        fase = math.pi + abs(fase)
    elif cuad == 4:
        fase = (2*math.pi) - abs(fase)
    return (modul,fase)
def iden_cuad(a):
    """identifica el cuadrante a partir de una coordenada polar
    tupla -> int
    """
    if a[0] >= 0 and a[1] >= 0:
        return 1
    if a[0] <= 0 and a[1] >= 0:
        return 2
    if a[0] <= 0 and a[1] <= 0:
        return 3
    if a[0] >= 0 and a[1] <= 0:
        return 4
def plr_crt(a):
    """pasar de representacion polar a cartesiana
    tupla -> tupla
    """
    real = a[0] * math.cos(a[1])
    img = a[0] * math.sin(a[1])
    return (real,img)
