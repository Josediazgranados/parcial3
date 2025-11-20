CREATE TABLE productos (codigo INT, nombre STRING, precio INT);

INSERT INTO productos (codigo, nombre, precio) VALUES (101, "Laptop", 3500);

INSERT INTO productos (codigo, nombre, precio) VALUES (102, "Mouse", 40);

SELECT nombre, precio FROM productos WHERE codigo = 101;

UPDATE productos SET precio = 3000 WHERE codigo = 101;

DELETE FROM productos WHERE codigo = 102;
