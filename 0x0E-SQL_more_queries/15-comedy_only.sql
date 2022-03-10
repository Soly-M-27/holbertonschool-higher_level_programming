-- Write a script that lists all Comedy shows in the
-- database hbtn_0d_tvshows
SELECT tv_shows.title AS title
FROM tv_genres
WHERE tv_genres.name = "Comedy"
ORDER BY tv_show.title;