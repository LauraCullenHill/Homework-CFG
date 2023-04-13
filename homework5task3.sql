-- Change the maximum mark of the cyber security exam to 100

USE foundation_assessment_i;

UPDATE exams
SET Max_Mark = 100 WHERE Exam_Name = 'Cyber Security';

SELECT * FROM exams;

-- Write a query to list the lowest-achieving student across the exams.
-- Output their full name along with their total score.

-- Write a query to list the lowest-achieving student across the exams.
-- Output their full name along with their total score.

USE foundation_assessment_i;

SELECT FORENAME, SURNAME, Mark 
FROM students s
JOIN
result r
ON
s.Student_ID =
r.Student_ID
group by results.Student_ID
ORDER BY sum(result.Mark)
LIMIT 1;


USE foundation_assessment_i;

SELECT s.Student_ID, s.Forename, s.Surname, sum(results.Mark) as Total
FROM results
JOIN students
WHERE r.Student_ID = s.Student_ID
GROUP BY r.Student_ID
ORDER BY Total
LIMIT 1;



-- All students who failed an exam (received a mark of less than 40) have now
-- chosen to leave this program. Remove them from the students table.

USE foundation_assessment_i;

SELECT FORENAME, SURNAME, Mark 
FROM students s
JOIN
result r
ON
s.Student_ID =
r.Student_ID
group by results.Student_ID
ORDER BY sum(result.Mark)
LIMIT 1;


USE foundation_assessment_i;

DELETE s
FROM students s
INNER JOIN
result r
ON
s.Student_ID =
r.Student_ID
WHERE r.Mark < 40;




DELETE FROM Students where Student_ID in
(
	SELECT sid FROM
	(
	SELECT DISTINCT students.Student_ID AS sid
	FROM results 
	JOIN students
	WHERE 
	resuls.Student_ID = students.Student_ID
	AND
	mark < 40
    ) as s
);





SELECT authors.author_name, SUM(books.num_sold) AS total_books_sold
FROM authors
INNER JOIN books ON authors.author_id = books.author_id
GROUP BY authors.author_name
ORDER BY total_books_sold DESC
LIMIT 3;













	
