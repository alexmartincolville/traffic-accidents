WITH accident_severity AS (
    SELECT accident_index
         , accident_severity
    FROM dwh.fact_accident_vehicle
)
SELECT 1 AS id
     , accident_severity
     , COALESCE(ROUND((COUNT(*) * 1.0 / (SELECT COUNT(*) FROM accident_severity)) * 100, 2), 0) AS percentage
FROM accident_severity
GROUP BY accident_severity
ORDER BY percentage;