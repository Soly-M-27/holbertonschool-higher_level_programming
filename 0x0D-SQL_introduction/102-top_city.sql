-- Write a script that displays the top 3 of cities
-- temperature during July and August ordered by temperature (descending)
Select city, avg(value) AS avg_temp FROM temperatures ORDER BY avg_temp DESC LIMIT 3;
