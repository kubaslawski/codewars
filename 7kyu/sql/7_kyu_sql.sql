/* REPEAT AND REVERSE */
SELECT REPEAT(name, 3) AS name, REVERSE(characteristics) AS characteristics
FROM monsters

/*  Length based SELECT with LIKE */
SELECT first_name, last_name
FROM NAMES
WHERE first_name LIKE '______%'

/* SQL with LOTR: Elven Wildcards */
SELECT UPPER(SUBSTRING(firstname, 1, 1)) || LOWER(SUBSTRING(firstname, 2))
           || ' ' ||
       UPPER(SUBSTRING(lastname, 1, 1)) || LOWER(SUBSTRING(lastname, 2))
           AS shortlist
FROM elves
WHERE (firstname LIKE '%tegil%' OR lastname LIKE '%astar%');

/* Maths with String Manipulations */
SELECT BIT_LENGTH(name) + LENGTH(race) AS calculation
FROM demographics;

/* SQL Basics: Up and Down */
SELECT CASE
           WHEN (SUM(number1) + SUM(number2)) % 2 = 1 THEN MAX(number1)
           ELSE MIN(number1)
           END AS number1,
       CASE
           WHEN (SUM(number1) + SUM(number2)) % 2 = 0 THEN MIN(number2)
           ELSE MAX(number2)
           END AS number2
FROM numbers

/* Easy SQL: Bit Length */
SELECT id, BIT_LENGTH(name) AS name, birthday, BIT_LENGTH(race) as race
FROM demographics

/* GROCERY STORE: Support Local Products */
SELECT COUNT(*) AS products, country
FROM products
WHERE country IN ('United States of America', 'Canada')
GROUP BY country
ORDER BY products DESC;

