WITH age_bands AS (
    SELECT accident_index
         , age_band_of_driver
    FROM fact_accident_vehicle
    WHERE age_band_of_driver <> 'Data missing or out of range'
)
SELECT 1 AS id
     , age_band_of_driver
     , ROUND((COUNT(*) * 1.0 / (SELECT COUNT(*) FROM age_bands)) * 100, 2) AS percentage
FROM age_bands
GROUP BY age_band_of_driver
ORDER BY percentage;