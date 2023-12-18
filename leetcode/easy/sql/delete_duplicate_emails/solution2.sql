-- Table : Person
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | id          | int     |
-- | email       | varchar |
-- +-------------+---------+
-- Write a solution to delete all duplicate emails, keeping only one unique
-- email with the smallest id.

delete p1
from Person as p1
inner join Person as p2
on p1.email = p2.email
where p1.id > p2.id;