-- SINGLE ROW
SELECT *
FROM business_sales
WHERE customer_id = (SELECT customer_id -- this subquery returns single value
                     FROM customer
                     WHERE last_name = 'JOHNSON'
                     ) ;

-- MULTI-ROW 
SELECT *
FROM business_sales
WHERE customer_id IN (SELECT customer_id -- this subquery returns multiple values
                      FROM business_customer
                      WHERE service_plan = 'ELITE'
                      ) ;

-- CORRELATED
-- Who overdrafted?
SELECT *
FROM business_customer bc
WHERE deposit < (SELECT SUM(total_price)
                 FROM business_sales bs
                 WHERE bs.customer_id = bc.customer_id);


-- NESTED (subquery in another subquery)
SELECT *
FROM business_customer 
WHERE customer_id IN (SELECT customer_id
                      FROM business_sales
                      WHERE item_id = (SELECT item_id
                                       FROM business_item
                                       WHERE item_name = 'FOOTWEAR'
                                       )
                      );

-- EXISTS/NOT
SELECT *
FROM business_customer bc
WHERE NOT EXISTS (SELECT *
                  FROM business_sales bs
                  WHERE bs.customer_id = bc.customer_id
                  ) ;
                  
-- ALL/ANY
SELECT *
FROM business_sales 
WHERE total_price > ALL (SELECT AVG(total_price)
                         FROM business_sales);
