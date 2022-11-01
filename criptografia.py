import random as rd

lista_primo_q = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
               53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107,
               109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167,
               173, 179, 181, 191, 193, 197, 199]

lista_primo_p = [211, 223, 227, 229,
               233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283,
               293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359,
               367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431,
               433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491,
               499]
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
    p = rd.choice(lista_primo_p)
    print(p)
    q = rd.choice(lista_primo_q)
    print(q)
    n = p * q
    y = p - 1
    x = q - 1
    totiente = x * y
    e = gera_chave_publica(totiente)
    d = gera_chave_privada(totiente, e)
    mensagem = cifrar(mensagem, e, n)
    lista = (mensagem, d, n)

    return lista
