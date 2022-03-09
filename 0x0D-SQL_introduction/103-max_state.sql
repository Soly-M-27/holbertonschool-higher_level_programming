-- Write a script that displays the max temperature
-- of each state (ordered by State name)
SELECT state, max(value) AS max_temp
FROM temperature
GROUP BY state
ORDER BY state
LIMIT 3;