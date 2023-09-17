-- Table: Weather
-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | id            | int     |
-- | recordDate    | date    |
-- | temperature   | int     |
-- +---------------+---------+
--
-- Write a solution to find all dates' Id with higher temperatures compared to its previous dates (yesterday).

select w2.id
from
  Weather as w1,
  Weather as w2
where
  w2.recordDate = date_add(w1.recordDate, interval 1 day)
  and w2.temperature > w1.temperature;
