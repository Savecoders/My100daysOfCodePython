/*
 Podemos usar
 GROUP BY
 en múltiples campos,
 el orden en el que escribimos los campos afectan en como se agrupan los datos
 */
SELECT
  certification,
  release_year,
  COUNT(title) AS title_count
FROM
  films
GROUP BY
  certification,
  release_year;

-- GROUP BY CON ORDER BY
SELECT
  certification,
  release_year,
  COUNT(title) AS title_count
FROM
  films
GROUP BY
  certification,
  release_year
ORDER BY
  certification,
  release_year;

-- Orden de ejecución
-- 1 FROM
-- 2 WHERE
-- 3 GROUP BY
-- 4 HAVING
-- 5 SELECT
-- 6 DISTINCT
-- 7 ORDER BY
-- ---------
-- EXAMPLE:
-- ---------
SELECT
  certification,
  COUNT(title) AS title_count
FROM
  films
GROUP BY
  certification
ORDER BY
  titie_count DESC;

LIMIT
  3 -- orden de ejecucion del ejemplo anterior
  -- 1 FROM
  -- 2 WHERE
  -- 3 GROUP BY
  -- 4 SELECT
  -- 5 ORDER BY
  -- 6 LIMIT