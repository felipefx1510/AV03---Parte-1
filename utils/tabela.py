import sqlite3

conexao = sqlite3.connect('carros_db.sqlite')

cursor = conexao.cursor()

def CREATE_TABLE():
    cursor.execute("""
               
               CREATE TABLE IF NOT EXISTS carros(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               tipo VARCHAR(255) UNIQUE,
               ano INT(4),
               qtd_portas INT(100),
               potencia INT(100)
               );
            """)

def inserir_dados(tipo, ano, qtd_portas, potencia):
    cursor.execute("""
        INSERT INTO carros(tipo, ano, qtd_portas, potencia) 
                VALUES (?, ?, ?, ?)
    """, (tipo, ano, qtd_portas, potencia))
    conexao.commit()
    
def listar_carros():
    carros = cursor.execute("""
        SELECT * FROM carros
""").fetchall()
    for lista in carros:
        print(f'ID: {lista[0]}, Tipo: {lista[1]}, Ano: {lista[2]}, Portas: {lista[3]}, Potência: {lista[4]} cavalos')
        
def buscar_carros(tipo):
    carros = cursor.execute("SELECT * FROM carros WHERE tipo=?", (tipo,)).fetchall()
    for busca in carros:
        print(f'ID: {busca[0]}, Tipo: {busca[1]}, Ano: {busca[2]}, Portas: {busca[3]}, Potência: {busca[4]} cavalos')