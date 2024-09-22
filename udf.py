# Importa la biblioteca sqlite3 para trabajar con bases de datos SQLite
import sqlite3  

# Importa la biblioteca pandas (aunque no se utiliza en este código)
import pandas as pd

# Define una función lambda que calcula el cubo de un número
square = lambda n : n * n 

# Imprime el cubo de 2 utilizando la función 'square'
print(square(2))

# Establece una conexión a una base de datos SQLite ('northwind.db')
with sqlite3.connect('../northwind.db') as conn:
    # Crea una función personalizada 'square' dentro de SQLite para usarla en consultas SQL
# La función acepta 1 parámetro y usa la función 'square' definida previamente
     conn.create_function('square', 1, square)

# Crea un cursor que permite ejecutar comandos SQL sobre la base de datos
     cursor = conn.cursor()

# Ejecuta una consulta SQL para seleccionar todas las filas de la tabla 'Products'
     cursor.execute('''SELECT *,square(Price) FROM Products WHERE Price > 0''')

# Almacena todos los resultados de la consulta en la variable 'results'
     results = cursor.fetchall() 

# Convierte los resultados de la consulta (almacenados en 'results') en un DataFrame de panda
     results_df = pd.DataFrame(results) 

# Confirma y guarda todos los cambios realizados en la base de datos desde la última transacción
     #conn.commit()

# Cierra el cursor, liberando los recursos asociados con él
     #cursor.close()
     #conn.close()

# Imprime el resultado de la consulta, que es una lista de todas las filas de la tabla 'Products'
print(results_df)


