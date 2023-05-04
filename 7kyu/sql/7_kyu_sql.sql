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

