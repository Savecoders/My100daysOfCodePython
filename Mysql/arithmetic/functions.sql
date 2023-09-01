/*
 la diferencia entre las funciones como SUM() 
 es que van de forma de Columna y las Asignaciones de 
 forma Aritmetica van en forma de Fila
 */
-- SUMA
SELECT
  SUM(4, 3);

-- RESTA
SELECT
  SUBTRACT(4, 3);

-- MULTIPLICACION
SELECT
  MULTIPLY(4, 3);

-- DIVISION
SELECT
  DIVIDE(4, 3);

-- MODULO
SELECT
  MOD(4, 3);

-- alias
SELECT
  SUM(4, 3) AS suma,
  SUBTRACT(4, 3) AS resta,
  MULTIPLY(4, 3) AS multiplicacion,
  DIVIDE(4, 3) AS division,
  MOD(4, 3) AS modulo;