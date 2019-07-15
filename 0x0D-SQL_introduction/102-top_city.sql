-- Import in hbtn_0c_0 database this table dump
-- Loads table
SOURCE temperatures.sql;
-- Displays avg temp in July and August
SELECT city, AVG(value) as avg_temp FROM temperatures WHERE month=7 OR month=8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
