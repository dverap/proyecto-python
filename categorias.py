class Categoria:
    secuencia=0
    def __init__(self,categoria):
        Categoria.secuencia +=1
        self.codigo=Categoria.secuencia
        self.descripcion=categoria
    def mostrar(self):
        print("{} - {}".format(self.codigo,self.descripcion))
        
    def datos(self):
        return [self.codigo,self.descripcion]
    def registro(self):
        return {"codigo":self.codigo,"descripcion":self.descripcion}

# listaCategorias = []        
# cat = Categoria("Lacteos")
# #cat.mostrar() 
# #Categoria.secuencia=2
# #print(cat.datos())       
# cat2 = Categoria("Bebidas")
# #cat2.mostrar()        
# #print(cat2.datos())       
# # listaCategorias.append(cat.datos())        
# # listaCategorias.append(cat2.datos())
# cat3 = Categoria("Legumbres")
# listaCategorias.append(cat.registro())        
# listaCategorias.append(cat2.registro())
# listaCategorias.append(cat3.registro())
# print(listaCategorias)
        