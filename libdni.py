def calculaLetra(numeroDNI):
  lista = 'TRWAGMYFPDXBNJZSQVHLCKE'
  return (lista[numero%23])
numero = int(input("Escribe tu numero de DNI: "))
print('Tu letra del DNI es: ', calculaLetra(numero))