import random as rd

# Criptografia
def mdc(n1, n2):
    while (n2 != 0):
        r = n1 % n2
        n1 = n2
        n2 = r
    return n1

def gera_chave_publica(n):
    while True:
        e = rd.randrange(2, n)
        if (mdc(n, e) == 1):
            return e

def gera_chave_privada(totiente, e):
    d = 0
    while ((d * e) % totiente != 1):
        d += 1
    return d

def cifrar(mensagem, e, n):
    msg_cifrada = ""
    for letra in mensagem:
        k = (ord(letra) ** e) % n
        msg_cifrada += chr(k)
    return msg_cifrada


def decifrar(mensagem, n, d):
    msg_decifrada = ""
    for letra in mensagem:
        k = (ord(letra) ** d % n)
        msg_decifrada += chr(k)
    return msg_decifrada


def rsa(mensagem):
    p = 17
    q = 19
    n = p * q
    y = p - 1
    x = q - 1
    totiente = x * y
    e = gera_chave_publica(totiente)
    d = gera_chave_privada(totiente, e)
    mensagem = cifrar(mensagem, e, n)
    lista = (mensagem, d, n)

    return lista
