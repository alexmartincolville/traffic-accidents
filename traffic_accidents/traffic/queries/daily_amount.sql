SELECT 1 as id
     , day_of_week
     , COUNT(*) AS count
FROM dwh.fact_accident_vehicle
GROUP BY day_of_week
ORDER BY count DESC;