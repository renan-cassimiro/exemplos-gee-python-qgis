#Importa o pacote do Earth Engine
import ee

#Autenticar-se no Earth Engine. Não precisa chamar sempre
#ee.Authenticate()

#Inicializa o Earth Engine
ee.Initialize()

#Cria uma lista
lista = ee.List([])

#Roda 50 vezes o bloco de codigo das duas linhas subsequentes
for i in range(50):
    #Cria uma imagem aleatória
    imgRand = ee.Image.random(i)
    #Adiciona a imagem aleatória a lista
    lista = lista.add(imgRand)
  
#Ao final, são 50 imagens aleatórias na lista
#Cria uma colecao a partir da lista de imagem
imgCol = ee.ImageCollection(lista)

#Adiciona uma imagem com os valores mediana de toda a coleção ao QGIS
Map.addLayer(imgCol.median(), {}, "Mediana")
#Adiciona uma imagem com os valores mínimos de toda a coleção ao QGIS
Map.addLayer(imgCol.min(), {}, "Minimo")
#Adiciona uma imagem com os valores máximos de toda a coleção ao QGIS
Map.addLayer(imgCol.max(), {}, "Maximo")

