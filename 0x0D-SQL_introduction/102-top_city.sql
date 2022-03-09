-- Write a script that displays the top 3 of cities
-- temperature during July and August ordered by temperature (descending)
SELECT city, avg(value) AS avg_temp FROM temperatures WHERE month = 6 || month = 7 GROUP BY city ORDER BY TOP(avg_temp) DESC LIMIT 3;
