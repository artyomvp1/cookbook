-- 1. SCALLER
SELECT *
FROM business_sales 
WHERE customer_id IN (SELECT customer_id
                      FROM business_customer
                      WHERE service_plan = 'ELITE') 
;

SELECT *
FROM business_sales
WHERE item_id IN (SELECT item_id
                  FROM business_item
                  WHERE price = (SELECT MIN(price)
                                 FROM business_item 
                                 )
                 )
;

SELECT customer_id, SUM(total_price)
FROM business_sales 
GROUP BY customer_id
HAVING SUM(total_price) > 3000;



-- 2. CORRELATED
SELECT *
FROM business_customer bc
WHERE EXISTS (SELECT *
              FROM business_sales bs
              WHERE bs.customer_id = bc.customer_id
              )

