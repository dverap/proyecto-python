from categorias import Categoria


class Articulo:
  secuencia=2             
  articulos = [ {"codigo":1,"descripcion":"Coca Cola","categoria":2,"precio":1.5,"stock":100},
              {"codigo":2,"descripcion":"Vita Leche","categoria":1,"precio":1,"stock":50},
             ]

  def __init__(self,descrip,codCategoria,precio,stock):
    Articulo.secuencia +=1
    self.codigo=Articulo.secuencia
    self.descripcion=descrip
    self.categoria=codCategoria
    self.precio=precio
    self.stock=stock
  
    
  def mostrar(self):
    print("{} - {} - {} - {} - {} ".format(self.codigo,self.descripcion,self.categoria,self.precio,self.stock))

  def registro(self):
    return {"codigo":self.codigo,"descripcion":self.descripcion,"categoria":self.categoria,"precio":self.precio,"stock":self.stock}
#print(Articulo.articulos)

# art = Articulo("Pepsi",2,1.5,100)
# #art.mostrar()
# articulo = art.registro()
# #print(articulo)
# Articulo.articulos.append(articulo)
# print(Articulo.articulos)