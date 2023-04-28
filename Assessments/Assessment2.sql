# 4.1 

CREATE DATABASE foundation_assessment_ii;

USE foundation_assessment_ii;
CREATE TABLE movie_info (
	movie_ID INT NOT NULL,
	movie_name VARCHAR(100) NOT NULL,
	movie_length TIME NOT NULL,
	age_rating VARCHAR(100) NOT NULL
);

CREATE TABLE screens (
	screen_ID VARCHAR(100) NOT NULL,
	four_k BOOLEAN NOT NULL
);

CREATE TABLE showings (
	showing_ID INT NOT NULL,
	movie_ID INT NOT NULL,
    screen_ID INT NOT NULL,
    start_time TIME NOT NULL,
    available_seats INT NOT NULL
);

#INSERTED DATA

#4.2

SELECT movie_name, start_time FROM movie_info
INNER JOIN showings ON movie_info.movie_ID = showings.movie_ID
WHERE start_time > '12:00:00'
ORDER BY start_time;


#4.3

SELECT movie_name, sum(movie_name) FROM movie_info
ORDER BY sum(movie_name),
SHOW 1; #show top 1 only;
