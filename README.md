Punto 1: Analizador SQL CRUD con ANTLR4

DESCRIPCIÓN
Este proyecto implementa un analizador léxico, sintáctico y semántico para un subconjunto de SQL centrado en operaciones CRUD:
- CREATE TABLE
- INSERT INTO
- SELECT
- UPDATE
- DELETE

La gramática está construida con ANTLR4 y el análisis semántico se realiza mediante un visitor en Python que valida tablas, columnas y tipos de datos.
EJECUCIÓN
cd ~/Descargas/puntos_project/Punto1
python3 run_punto1.py ejemplo_sql.p1.sql
