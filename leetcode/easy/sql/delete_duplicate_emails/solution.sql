-- Table : Person
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | id          | int     |
-- | email       | varchar |
-- +-------------+---------+
-- Write a solution to delete all duplicate emails, keeping only one unique
-- email with the smallest id.

delete from Person
where id not in (
  select * from (
    select min(id)
    from Person
    group by email
  ) as p
);