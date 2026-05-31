import sqlite3
import pandas as pd

db = sqlite3.connect('https://github.com/davidjamesknight/SQLite_databases_for_learning_data_science/blob/main/iris.db?raw=true')
sql = """
    SELECT 
        O.petal_length, 
        O.petal_width, 
        O.sepal_length, 
        O.sepal_width, 
        S.species
    FROM Observation AS O
    JOIN Species AS S ON S.species_id = O.species_id
"""
df = pd.read_sql_query(sql, db)
df.head()