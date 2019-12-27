![Iron Hack](https://github.com/rogerzadi/ModeloSupervivencia/blob/master/images/ironhack.png)
# Clusterización de clientes Retail
Este es un modelo que se utiliza para alimentar Crece la cual es un proyecto sobre una plataforma la cual ayuda a generar insights básicos así como basados en machine learning para tiendas. **Este es el apartado de Machine Learning para la plataforma**

### Intro 
Se creo un modelo de clusterización no supervisado, basandonos en las ventas de una tienda se crearon diferentes clusters con diferentes caracteristicas, esto para generar una estrategia de ventas mas solida.

### Modelo Utilizado
- K-Means
- Se utiliza PCA para disminuir dimensiones 

### Modelo

El modelo tiene como entrada:
- Registro de ventas de una tienda

La cual contiene Timestamp, Transacción, Item, Categoria, Precio

Se limpia y transforma los tipos de datos, observamos cuales son las variables categoricas para sacar one-hot-code (dummies) para asi poder manegar estos datos, esto se hace en base a la columna de categorías y a la suma de los Items pertenecientes a cada categoría, atravez de la libreria sklearn utilizamos el metodo K-means el cual se le indica que seran 3 clusters *en el ejemplo se ven 4 clusters pero en la plataforma se utilizan 3* 

el resultado se puede apreciar gráficamente así, sin embargo, los outputs del sistema serían datos los cuales utiliza el Web developer para dibujar sus gráficas:

![Gráfica por día](https://github.com/rogerzadi/Clusterizaci-n_clientes_retail/blob/master/images/cluster_hora.JPG)

