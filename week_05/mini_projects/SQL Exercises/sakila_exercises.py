SELECT * FROM sakila.actor

SELECT * FROM sakila.actor WHERE first_name = "FRED";

#######################
Building one list based on another:

SELECT * FROM
(
SELECT a.first_name, a.last_name, a.actor_id FROM sakila.actor AS a
JOIN sakila.film_actor AS fa
ON fa.actor_id = a.actor_id
JOIN sakila.film AS f
ON f.film_id = fa.film_id
WHERE f.film_id = 128
) AS actor_list

JOIN sakila.film_actor AS fa2
ON fa2.actor_id = actor_list.actor_id
JOIN sakila.film AS f2
ON fa2.film_id = f2.film_id
#######################

5.) Use a join query to select all the films in the category of your choice that was released before 2006

SELECT f.title, f.release_year, c.name FROM sakila.film as f
JOIN sakila.film_category as fc
ON f.film_id = fc.film_id
JOIN sakila.category as c
ON fc.category_id = c.category_id
WHERE f.release_year < 2011
#######################

6.-- Use a join query to select all actors first and last names, the film title, description, total cost and release year, and the category names for each of those films that the actor has appeared in. Sort the results by:
--   -cost
--   -release year
--   - and find the total cost for all movies they have appeared in.

SELECT al.first_name AS "Actor's First Name", al.last_name AS "Actor's Last Name", SUM(al.length) AS "Total length of movies appeared in"
FROM (
SELECT a.first_name, a.last_name, f.title, f.description, f.release_year, f.length, c.name
FROM sakila.actor AS a
JOIN sakila.film_actor AS fa
ON fa.actor_id = a.actor_id
JOIN sakila.film AS f
ON f.film_id = fa.film_id
JOIN sakila.film_category AS fc
ON fc.film_id = f.film_id
JOIN sakila.category AS c
ON c.category_id = fc.category_id
ORDER BY f.length DESC
) AS al
GROUP BY al.first_name, al.last_name
#######################




SELECT * FROM
(
SELECT a.first_name, a.last_name, a.actor_id FROM sakila.actor AS a
JOIN sakila.film_actor AS fa
ON fa.actor_id = a.actor_id
JOIN sakila.film AS f
ON f.film_id = fa.film_id
WHERE f.film_id = 128
) AS actor_list

JOIN sakila.film_actor AS fa2
ON fa2.actor_id = actor_list.actor_id
JOIN sakila.film AS f2
ON fa2.film_id = f2.film_id
