SELECT accident."Accident_Index"
     , accident."Date"
     , accident."Day_of_Week"
     , accident."Accident_Severity"
     , accident."Road_Type"
     , accident."Speed_limit"
     , vehicle."make"
     , vehicle."Age_Band_of_Driver"
     , vehicle."Driver_Home_Area_Type"
     , vehicle."Age_of_Vehicle"
     , vehicle."Journey_Purpose_of_Driver"
FROM input_accident_information AS accident
         LEFT JOIN input_vehicle_information AS vehicle
                   ON accident."Accident_Index" = vehicle."Accident_Index"
WHERE accident."Date"::date >= ((SELECT MAX("Date") FROM input_accident_information)::date - INTERVAL '2 YEAR')
  AND vehicle."Accident_Index" IS NOT NULL
ORDER BY accident."Date"
;