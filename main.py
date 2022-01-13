from helpers import Helper
from categorias import Categoria
from articulos import Articulo
import os

categorias = [{"codigo":1,"descripcion":"Lacteos"},{"codigo":2,"descripcion":"Bebidas"}]
def buscategoria(cod):
  cat = "Sin categoria"
  for pos in range(0,len(categorias)):
    categoria = categorias[pos]
    if categoria["codigo"] == cod:
       cat = categoria["descripcion"]
       break
  return cat    
helper = Helper()
lista = ["1) Articulos","2) Categorias","3) Salir"]
opcion=""
while opcion != "3":
  os.system("cls")
  opcion = helper.menu(lista,"Menu Inventarios")
  if opcion == "1":
    opc1=""
    while opc1 != "3":
      os.system("cls")
      opc1 = helper.menu(["1) Ingreso","2) Consulta","3) Salir"],"Menu Articulos")
      os.system("cls")
      if opc1 == "1":
        print("Ingreso de Articulos")
        nombre= input("Nombre del Articulo: ")
        categoria= input("Codigo de Categoria: ")
        precio= float(input("Precio del Articulo: "))
        stock= int(input("Stock del Articulo: "))
        art = Articulo(nombre,categoria,precio,stock)
        articulo = art.registro()
        Articulo.articulos.append(articulo)
        input("Datos ingresados satisfactoriamente, presiones una tecla para continuar...")
      elif opc1 == "2":
        print("*"*20,"Consulta de Articulos","*"*20)
        print("Codigo"," "*5,"Descripcion"," "*5,"Categoria","  Precio   ","  Stock")
        for art in Articulo.articulos:
          cod = art["codigo"]
          des=art["descripcion"]
          cat=art["categoria"]
          cat = buscategoria(cat)
          pre = art["precio"]
          sto=art["stock"]
          print(" "*2,cod," "*8,des," "*(15-len(des)),cat," "*5,pre," "*(8-len(str(pre))),sto)
        input("Presione una tecla para continuar...")
          
            
  elif opcion == "2":
    print("Mantenimiento de Articulos")
    
  elif opcion == "3":
    print("Salir")
        
print("Gracias por visitarnos")  
print(Articulo.articulos)

