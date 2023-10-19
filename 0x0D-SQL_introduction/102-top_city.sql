-- Import in hbtn_0c_0 database this table dump
-- script that displays the top 3 of cities temperature during July and
-- August ordered by temperature (descending)
SELECT city, AVG(value) AS avg_temp FROM tempretures WHERE month
BETWEEN 7 NAD 8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
