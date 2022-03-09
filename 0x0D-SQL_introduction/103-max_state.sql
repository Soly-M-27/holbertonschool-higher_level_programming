-- Write a script that displays the max temperature
-- of each state (ordered by State name)
SELECT state, value
FROM temperature
GROUP BY state
ORDER BY max(temperature)
LIMIT 3;
