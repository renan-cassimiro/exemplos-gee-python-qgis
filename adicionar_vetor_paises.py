#Importa o pacote do Earth Engine
import ee

#Autenticar-se no Earth Engine. Não precisa chamar sempre
#ee.Authenticate()

#Inicializa o Earth Engine
ee.Initialize()

#Carrega a colecao de vetores LSIB 2017: Large Scale International Boundary Polygons, Detailed
#pelo codigo do dataset: 'USDOS/LSIB_SIMPLE/2017'
paises = ee.FeatureCollection("USDOS/LSIB_SIMPLE/2017")

#Imprime no console a quantidade de vetores
print("Tamanho Inicial da Coleção: ",paises.size().getInfo())

#Filtra a colacao de vetores para manter apenas Brasil
brasil = paises.filterMetadata('country_co', 'equals','BR')

#Imprime no console a quantidade de vetores após filtro
print("Tamanho da coleção depois do filtro: ", brasil.size().getInfo())

#Adiciona camada ao QGIS
Map.addLayer(brasil, {}, "Brasil")


