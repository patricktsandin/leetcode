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
where not exists(
    select 1
    from Orders as o
    where o.customerId = c.id
)
