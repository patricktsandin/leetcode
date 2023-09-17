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
where id in (
  select id
  from (
    select
      id,
      min(id) over(partition by email) as min_id
    from Person
  ) as p
  where id > min_id
);