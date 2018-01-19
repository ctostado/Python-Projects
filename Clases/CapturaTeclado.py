# Ejercicio para la introduccion por teclado

class CapturaTeclado:

    # Constantes para selección de tipo
    CARACTER = 0
    ENTERO = 2
    FLOTANTE = 3

    def __init__(self):
        print("Se ha creado un objeto de tipo teclado")

    def entradaTecado(self,tipoEntrada, mensajeMostrado):

        if tipoEntrada == self.ENTERO:

            while (True):

                try:
                    capturaTeclado = int(input(mensajeMostrado))
                except ValueError:
                    print("Formato de entrada invalido! Ingresa un número entero...")
                except Exception as e:  # Obtener el identificador del error
                    print(type(e).__name__)  # Escribe el tipo de error
                else:
                    return capturaTeclado
                    break

        elif tipoEntrada == self.FLOTANTE:

            while (True):

                try:
                    capturaTeclado = float(input(mensajeMostrado))
                except ValueError:
                    print("Formato de entrada invalido! Ingresa un número Flotante")
                except Exception as e:  # Obtener el identificador del error
                    print(type(e).__name__)  # Escribe el tipo de error
                else:
                    return capturaTeclado
                    break

        elif tipoEntrada == self.CARACTER:

            while (True):

                try:
                    capturaTeclado = input(mensajeMostrado)
                except ValueError:
                    print("Formato de entrada invalido! Ingresa lo solicitado")
                except Exception as e:  # Obtener el identificador del error
                    print(type(e).__name__)  # Escribe el tipo de error
                else:
                    return capturaTeclado
                    break

    pass
