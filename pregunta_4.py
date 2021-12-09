
"""
Created on Wed Dec  8 00:22:29 2021

@author: EVER JHONNY
"""
import numpy as np

def Entrenamiento(a, b):

        num_inputs = 0

        while num_inputs < len(y):
            print('-------------------- ')
            # generando pesos aleatorios en el rango [-1,1]
            pesos = np.array(np.random.uniform(-1, 1, x.shape))
            for a, peso, b in zip(x, pesos, y):

                # Realiza la suma  de entradas con pesos               
                y_generado = np.dot(a, peso)
               
                # Función sigmoide
                y_generado = 0 if y_generado < 0 else 1

                if y_generado == b:
                    num_inputs += 1
                else:
                    num_inputs = 0
               
                print('entrada: ', a, 'pesos:', peso, 'esperado: ',
                      b, 'obtenido: ',   y_generado)


x = np.array([[0,0,1],[0,1,1],[1,0,1],[1,1,1]])
y = np.array([[0],[0],[0],[1]])
perceptron = Entrenamiento(x, y)
