GRAFICA OJIVA

import matplotlib.pyplot as plt
print("Setup terminado")

plt.figure (figsize = (12, 6)) # (Ancho, largo) del grafico 
marcas_clase = [ "pan", "Carnes", "Quesos", "Vegetales", " Salsas", "Condimentos " , ""]
frecuencia =[275, 250, 790, 470, 510, 500, 330,0] 
frecuencia =[0, 1, 3, 4, 5, 6,0] 

#Ajuste a las listas para generar el poligono de frecuencias

datos_x = [0] + marcas_clase
datos_y = [0] + frecuencia 



#Poligono de frecuencias  con:
# - Estilo de lineas punteado(linestyle = ":"). https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html
# - marcador con forma circular(marker ="v"). https://matplotlib.org/stable/api/markers_api.html
# - 

plt.plot (datos_x, datos_y,
        linewidth = 6, color = "b", linestyle = ":",  
        marker ="v", markersize = 15, markeredgecolor = "b", markerfacecolor = "y")

plt.xticks( marcas_clase,  fontsize = 15, rotation = 45 )
plt.xlabel("Marcas de clase", fontsize = 25) 
plt.ylabel("Frecuencia acumulada", fontsize = 25)
plt.title("Ojiva", fontsize = 40)
plt.grid(True)
plt.show()