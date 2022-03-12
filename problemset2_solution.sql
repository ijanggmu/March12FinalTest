SELECT
    dpt.Name AS Department,
    e1.Name AS Employee,
    e1.Salary AS Salary
FROM Employee AS e1
INNER JOIN Department dpt
ON e1.DepartmentID = dpt.Id
WHERE 3 > (
           SELECT COUNT(DISTINCT Salary)
           FROM Employee AS e2
           WHERE e2.Salary > e1.Salary
           AND e1.DepartmentID = e2.DepartmentID
          )
ORDER BY
Department ASC,
Salary DESC;