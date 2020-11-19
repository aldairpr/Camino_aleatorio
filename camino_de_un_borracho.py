from bokeh.plotting import figure, show, output_file
from borracho import BorrachoTradicional
from campo import Campo
from coordenada import Coordenada
import numpy as np

def simulacion_caminata(borracho, pasos, tipo_de_borracho):
    """Simular caminata y obtener las coordenadas."""
    origen = Coordenada(0, 0)
    
    campo = Campo()
    campo.anadir_borracho(borracho, origen)
    
    coord_x = []
    coord_y = []
    
    coord_x.append(origen.x)
    coord_y.append(origen.y)
    
    for _ in range(pasos):
        campo.mover_borracho(borracho)
        coord_x.append(campo.obtener_coordenada(borracho).x)
        coord_y.append(campo.obtener_coordenada(borracho).y)
        ultima_coordenada = campo.obtener_coordenada(borracho)
    
    #Distancia del punto inicial al final
    distancia = origen.distancia(ultima_coordenada)
    
    return coord_x, coord_y, distancia

def graficar(x, y, distancia): 
    distancia_inicio_a_fin = np.round(distancia, 2)
    
    # Salida estática HTML
    output_file("recorrido.html")
    
    grafica = figure(title="Camino aleatorio", x_axis_label='X (m)', y_axis_label='Y (m)')
    #size: Tamano del circulo.
    #alpha: Intensidad del color.
    grafica.circle(x[0], y[0], color='red', size=10, alpha=0.7, legend = 'Inicio')  
    grafica.line(x, y, color = 'green', legend = 'Recorrido del borracho')
    grafica.circle(x[len(x)-1], y[len(y)-1], color='black', size=10, alpha=0.5, legend = 'Final')
    grafica.line([x[0], x[len(x)-1]], [y[0], y[len(y)-1]], color = 'purple', line_dash = "4 4", legend = f'Se alejo {distancia_inicio_a_fin} metros del punto de origen')

    show(grafica)

def main(pasos, tipo_de_borracho):
    borracho = tipo_de_borracho(nombre="XX")    
    coord_x, coord_y, distancia = simulacion_caminata(borracho, pasos, tipo_de_borracho)
    graficar(coord_x, coord_y, distancia)


if __name__=="__main__":
    pasos_que_dara = 2000
    
    main(pasos_que_dara, BorrachoTradicional)