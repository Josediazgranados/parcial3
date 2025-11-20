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

punto2 y 3 
Este proyecto contiene los puntos relacionados con la gramática para
operaciones con matrices y su implementación usando ANTLR4. Todos los
archivos deben estar ubicados dentro de una misma carpeta de trabajo,
incluyendo:

-   Los archivos .g4
-   Los scripts Python
-   La carpeta ejemplos/
-   El entorno virtual venv/
-   El directorio generado por ANTLR (pycache y los archivos
    MatrixLangLexer.py, MatrixLangParser.py, MatrixLangVisitor.py)

PUNTO 2 – GRAMÁTICA PARA PRODUCTO
PUNTO DE MATRICES

Estructura esperada del proyecto:
puntos_project/
│── venv/
│── antlr-4.13.1-complete.jar
│── Punto2/
│   ├── MatrixLang.g4
│   ├── punto2_eval.py
│   ├── run_punto2.py
│   └── ejemplos/
│       └── ejemplo_matrices.mlg
│
└── Punto3/
    ├── MatrixLang.g4
    ├── MatrixLangLexer.py
    ├── MatrixLangParser.py
    ├── MatrixLangVisitor.py
    ├── run_matrix.py
    └── matrices.txt

EJECUCIÓN DEL PUNTO 2:

cd Punto2 python3 run_punto2.py ejemplos/archivo.mlg

PUNTO 3 – IMPLEMENTACIÓN DE LA
GRAMÁTICA EN ANTLR4 

REGENERAR LA GRAMÁTICA:

cd ~/Descargas/puntos_project/Punto3
antlr4 -Dlanguage=Python3 MatrixLang.g4 -visitor

Ejecucion:
python3 run_matrix.py matrices.txt



python3 run_matrix.py matrices.txt
