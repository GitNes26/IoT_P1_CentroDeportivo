import ConexionMySQL as mysql
import json

# t = input("Nombre de Tabla: ")
# w=mysql.Mostrar(t)
# print(type(w))
# for x in w:
#     print(type(x), x[1])


# t = input("Nombre de Tabla: ")
# cs= input("Cambiar el campo: ")
# vs= input("Por: ")
# w = input("Donde el campo: ")
# c = input("Sea: ")
# v = input("A...: ")
# mysql.Actualizar(tabla=t, campoSet=cs,valorSet=vs,
# campoWhere=w, condicional=c,valorWhere=v)
# print('campo modificado')

t = input("Nombre de Tabla: ")
c = input("Donde el campo:")
v = input("Tenga el valor:")
mysql.Eliminar(tabla=t, campoWhere=c, valorWhere=v)
print('campo eliminado')