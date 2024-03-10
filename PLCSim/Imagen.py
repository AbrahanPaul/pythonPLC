import os
from skimage import io


filename = os.path.join('tito.jpg')
tito = io.imread(filename)

print("Dimensiones de la imagen: (filas, columnas, canales) ", tito.shape)
io.imshow(tito)
io.show()

