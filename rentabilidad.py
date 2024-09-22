import sqlite3
import pandas as pd
import matplotlib.pyplot as plt 

conn = sqlite3.connect('../northwind.db')

#OBTENIENDO LOS 10 PRODUCTOS MAS RENTABLES
query = '''
      SELECT ProductName, SUM(Price * Quantity) AS Revenue
      FROM OrderDetails od 
      JOIN Products p ON p.ProductID = od.ProductID
      GROUP BY od.ProductID
      ORDER BY Revenue DESC 
      LIMIT 10
'''

#este metodo permite leer directamente una consulta y nos da la respuesta y ya cierra las conexiones permer valor la conulta segundo la conxion
top_products= pd.read_sql_query(query,conn)

# Crea un gráfico de barras utilizando el DataFrame 'top_products'
# x: columna que se usará para el eje x (nombres de los productos)
# y: columna que se usará para el eje y (ingresos)
# kind: tipo de gráfico, en este caso, un gráfico de barras
# figsize: tamaño de la figura (ancho, alto)
# legend: si se debe mostrar la leyenda, se establece en False para no mostrarla
top_products.plot(x='ProductName',y='Revenue',kind='bar',figsize = (10,5), legend = False)

# Establece el título del gráfico
plt.title('10 Productos más rentables')

# Establece la etiqueta del eje x
plt.xlabel('Products')

# Establece la etiqueta del eje y
plt.ylabel('Revenue')

# Rota las etiquetas del eje x 90 grados para que se vean mejor
plt.xticks(rotation=90)

# Muestra el gráfico en pantalla
#plt.show()


#OBTENIENDO LOS 10 EMPLEADOS MAS EFECTIVOS

query2 = ''' 
         SELECT FirstName || " " || LastName as Employee, COUNT(*) as Total 
         FROM Orders o
         JOIN Employees e
         ON e.EmployeeID = o.EmployeeID
         GROUP BY o.EmployeeID
         ORDER BY Total 
         LIMIT 3
'''
top_products= pd.read_sql_query(query2,conn)

top_products.plot(x='Employee',y='Total',kind='bar',figsize = (10,5), legend = False)

# Establece el título del gráfico
plt.title('10 Empleados mas efectivos')

# Establece la etiqueta del eje x
plt.xlabel('Empleados')

# Establece la etiqueta del eje y
plt.ylabel('Total vendido')

# Rota las etiquetas del eje x 90 grados para que se vean mejor
plt.xticks(rotation=45)

# Muestra el gráfico en pantalla
plt.show()

