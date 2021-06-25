WITH vehicle_age AS (
    SELECT accident_index
         , age_of_vehicle
    FROM fact_accident_vehicle
)
SELECT 1 AS id
     , COALESCE(age_of_vehicle, -1) AS age_of_vehicle
     , COALESCE(ROUND((COUNT(*) * 1.0 / (SELECT COUNT(*) FROM vehicle_age)) * 100, 2), 0) AS percentage
FROM vehicle_age
GROUP BY age_of_vehicle
ORDER BY percentage DESC;