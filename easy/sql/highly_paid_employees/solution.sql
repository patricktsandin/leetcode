-- Table: Employee
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | id          | int     |
-- | name        | varchar |
-- | salary      | int     |
-- | managerId   | int     |
-- +-------------+---------+
--
-- Write a solution to find the employees who earn more than their managers.

select e.name as Employee
from Employee as e
inner join Employee as m
on e.managerId = m.id
where e.salary > m.salary;