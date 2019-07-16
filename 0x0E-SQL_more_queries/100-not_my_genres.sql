-- A script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
SELECT DISTINCT tv_shows.title
FROM tv_show_genres
LEFT JOIN tv_shows
ON tv_show_genres.show_id=tv_shows.id
LEFT JOIN tv_genres
ON tv_show_genres.genre_id=tv_genres.id
WHERE tv_genres.name NOT IN
(
SELECT tv_genres.name
FROM tv_show_genres
LEFT JOIN tv_shows
ON tv_show_genres.show_id=tv_shows.id
LEFT JOIN tv_genres
ON tv_show_genres.genre_id=tv_genres.id
WHERE tv_genres.name='Comedy'
)
ORDER BY tv_shows.title;
