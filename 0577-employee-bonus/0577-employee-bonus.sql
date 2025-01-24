# Write your MySQL query statement below
SELECT e.name, b.bonus FROM Bonus AS b
RIGHT OUTER JOIN Employee AS e ON e.empId = b.empId
WHERE b.bonus IS NULL
OR b.bonus < 1000;