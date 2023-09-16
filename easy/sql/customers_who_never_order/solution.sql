-- Table: Customers
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | id          | int     |
-- | name        | varchar |
-- +-------------+---------+
--
-- Table: Orders
-- +-------------+------+
-- | Column Name | Type |
-- +-------------+------+
-- | id          | int  |
-- | customerId  | int  |
-- +-------------+------+
--
-- Write a solution to find all customers who never order anything.

select name as Customers
from Customers as c
left join Orders as o
on c.id = o.customerId
group by c.id
having count(o.id) = 0;
