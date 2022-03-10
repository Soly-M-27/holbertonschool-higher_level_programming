-- Write a script that lists all shows, and all genres
-- linked to that show, from the database hbtn_0d_tvshows
SELECT tv_shows.title AS title, tv_genres.name AS name
FROM tv_genres
INNER JOIN tv_shows ON tv_shows.title = tv_genres.name
ORDER BY title
ORDER BY name ASC;