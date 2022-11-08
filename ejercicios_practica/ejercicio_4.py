# Matplotlib [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de matplotlib
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    print("Line Plot: Figura con múltiples gráficos")

    # NOTA: aproveche los ejemplos "line_plot" y "scatter_plot" de clase

    # Se desea graficar cuatro funciones en una misma figura
    # en cuatros gráficos (axes) distintos. Para el siguiente
    # intervalor de valores de "X":
    x = np.linspace(0, 10, 40)

    # Realizar tres gráficos que representen
    # y1 = x^2 (X al cuadrado)
    # y2 = x^3 (X al cubo)
    # y3 = x^4 (X a la cuarta)
    # y4 = raiz_cuadrada(X)

    # Implementación:
    y1 = x**2
    y2 = x**3
    y3 = x**4
    y4 = np.sqrt(x)

    # Alumnos: Esos cuatro gráficos deben estar colocados
    # en la diposición de 2 filas y 2 columna:
    # ------
    #  graf1 | graf2
    # ------
    #  graf3 | graf4
    # Utilizar add_subplot para lograr este efecto
    # de "2 filas" "2 columna" de gráficos

    # Se debe colocar en la leyenda la función que representa
    # cada gráfico

    # Cada gráfico realizarlo con un color distinto
    # a su elección

    # Colocar una grilla a elección

    # Crear acá su gráfico
    
    fig = plt.figure() 

    ax1 = fig.add_subplot(2, 2, 1)
    ax2 = fig.add_subplot(2, 2, 2) 
    ax3 = fig.add_subplot(2, 2, 3) 
    ax4 = fig.add_subplot(2, 2, 4)
    
    ax1.plot(x,y1, color="tab:red")
    ax2.plot(x,y2, color="tab:cyan")
    ax3.plot(x,y3, color="tab:olive")
    ax4.plot(x,y4, color="tab:purple")
    ax1.set_title("Cellar spiders population")
    ax2.set_title("Jumping spiders population")
    ax3.set_title("Wolf spiders population")
    ax4.set_title("Black widow spider population") 
    ax1.set_xlabel("Time")
    ax1.set_ylabel("Growth")
    ax2.set_xlabel("Time")
    ax2.set_ylabel("Growth")
    ax3.set_xlabel("Time")
    ax3.set_ylabel("Growth")
    ax4.set_xlabel("Time")
    ax4.set_ylabel("Growth")
    ax1.grid(ls="dashed")
    ax2.grid(ls="dashdot")
    ax3.grid(ls="solid")
    ax4.grid(ls="dotted")
    plt.show()

    print("terminamos")
