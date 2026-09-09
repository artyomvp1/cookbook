/*Replace Column1 and Column2*/
CASE
    WHEN column1 IS NULL OR column2 IS NULL THEN 0
    ELSE SIZE(
            FILTER(
                SEQUENCE(
                    LEAST(TO_DATE(column1), TO_DATE(column2)),
                    GREATEST(TO_DATE(column1), TO_DATE(column2)),
                    INTERVAL 1 DAY
                ),
                d -> DAYOFWEEK(d) IN (1, 7)    -- 1=Sunday, 7=Saturday
            )
         )
END AS weekend_days
