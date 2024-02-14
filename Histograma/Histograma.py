plt.figure (figsize = (12, 5)) # (Ancho, largo) del grafico 
frecuencia_relativa = [0.1667, 0.3333, 0.1667, 0.1667, 0.1667]# Datos del eje x
Marca_de_clase =[275, 350, 420, 370, 435 ] #Datos del eje y

#Histograma con:
# - Barras ajustadas al 100% (width = 1)
# - Contorno negro (edgecolor ="k")
plt.bar(Marca_de_clase, frecuencia_relativa,
        width = 10, edgecolor = "k", 
        color = ["#8B0000", "#CD5C5C", "#B22222", "#FFA07A", "#FF0000"])

plt.xticks(Marca_de_clase, fontsize = 15, rotation = 45 )
plt.xlabel("Marca_de_clase", fontsize = 25) #Etiqueta del eje x 
plt.ylabel("Frecuencia-relativa", fontsize = 25)#Etiqueta del eje y
plt.title("Histograma", fontsize = 40)#titulo
plt.grid()# Se activa la cuadricula 
plt.show() # Se muestra el grafico en panta