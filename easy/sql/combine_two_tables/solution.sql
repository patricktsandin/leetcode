-- Table: Person
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | personId    | int     |
-- | lastName    | varchar |
-- | firstName   | varchar |
-- +-------------+---------+
--
-- Table: Address
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | addressId   | int     |
-- | personId    | int     |
-- | city        | varchar |
-- | state       | varchar |
-- +-------------+---------+
--
-- Write a solution to report the first name, last name, city, and state of each
-- person in the Person table. If the address of a personId is not present in
-- the Address table, report null instead.
--
-- Return the result table in any order.

select firstName, lastName, city, state
from Person
left join Address
on Address.personId = Person.personId;
