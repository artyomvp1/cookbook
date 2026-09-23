
-- yyyy-MM-dd from one column + HH:mm:ss from other column
SELECT CURRENT_DATE AS today,
       carrierresettime,
       CAST(CONCAT(CURRENT_DATE, ' ', DATE_FORMAT(carrierresettime, 'HH:mm:ss')) AS TIMESTAMP) AS carrier_reset_today
FROM non_published_analytics.na_sc_analytics.ship_via_critical_pull_times_raw
LIMIT 10 ;
