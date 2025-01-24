# Write your MySQL query statement below
SELECT 
    s.student_id, 
    s.student_name, 
    su.subject_name, 
    COUNT(e.student_id)attended_exams
FROM Students AS s
CROSS JOIN Subjects As su
LEFT JOIN Examinations AS e 
    ON e.student_id = s.student_id
    AND su.subject_name = e.subject_name
GROUP BY s.student_id, s.student_name, su.subject_name
ORDER BY s.student_id, s.student_name, su.subject_name;