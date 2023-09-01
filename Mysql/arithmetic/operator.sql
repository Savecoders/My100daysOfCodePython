-- Los operadores mas usados son los mas basicos en la informatica `+` `-` `*` y `/` 
-- como son operadores basicos ya podemos esperar los resultados como el siguiente ejemplo:
-- suma
SELECT
  (4 + 3);

-- resta
SELECT
  (4 - 3);

-- multiplicacion
SELECT
  (4 * 3);

-- division
SELECT
  (4 / 3);

/*
 Similar algunos lenguajes de programación,
 SQL asume que solo quieres el valor entero de una división,
 es por eso que (4 / 3) como output da 1.
 */
SELECT
  (4 / 3.0);

-- alias  
SELECT
  (4 / 3.0) AS division;