def portafogli(utente, somma):
    banca={}
    if utente not in banca:
        banca[utente]=0
  
    banca = {  utente: banca[utente]+somma}
    return banca

print(portafogli('Mario', 100))
print(portafogli('Luca', 400))
