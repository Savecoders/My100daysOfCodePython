/*
 GROUP BY
 se usa comúnmente con funciones agregadas 
 para proporcionar estadística de resumen al agrupar en un solo campo,
 en este caso certificación y titulo
 */
SELECT
  certification,
  COUNT(title) AS title_count
FROM
  films
GROUP BY
  certification;

-- HAVING
SELECT
  certification,
  COUNT(title) AS title_count
FROM
  films
GROUP BY
  certification
HAVING
  COUNT(title) > 10;

-- Having es como un Where pero para Group By