import pandas as pd
import sqlite3


clientes = pd.read_csv('clientes.txt', sep='\t')
mascotas = pd.read_excel('mascotas.xlsx')
consultas = pd.read_json('consultas.json')
vacunas = pd.read_csv('vacunas.csv')
veterinarios = pd.read_xml('veterinarios.xml')


conn = sqlite3.connect('veterinaria.db')

# Guardar cada DataFrame en una tabla de la base de datos
clientes.to_sql('clientes', conn, if_exists='replace', index=False)
mascotas.to_sql('mascotas', conn, if_exists='replace', index=False)
consultas.to_sql('consultas', conn, if_exists='replace', index=False)
vacunas.to_sql('vacunas', conn, if_exists='replace', index=False)
veterinarios.to_sql('veterinarios', conn, if_exists='replace', index=False)




print("Datos cargados exitosamente")
tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table';", conn)
print("Tablas disponibles:")
print(tables)

print("\nContenido de 'clientes':")
print(pd.read_sql_query("SELECT * FROM clientes;", conn))

print("\nContenido de 'mascotas':")
print(pd.read_sql_query("SELECT * FROM mascotas;", conn))

print("\nContenido de 'consultas':")
print(pd.read_sql_query("SELECT * FROM consultas;", conn))

print("\nContenido de 'vacunas':")
print(pd.read_sql_query("SELECT * FROM vacunas;", conn))

print("\nContenido de 'veterinarios':")
print(pd.read_sql_query("SELECT * FROM veterinarios;", conn))


conn.close()