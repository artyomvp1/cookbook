/*
The query helps to compare LPN_DETAIL packed qty vs
ORDER_LINE_ITEM packed qty, which may be useful when
comparing the units in large orders.
*/
WITH x AS (SELECT item_id, order_qty, orig_order_qty, units_pakd
           FROM order_line_item oli
           WHERE order_id = (SELECT order_id FROM orders WHERE tc_order_Id = '0756637081') -- minor order
          ),

    y AS (SELECT item_id, SUM(initial_qty) AS initial_qty, SUM(size_value) AS size_value
          FROM lpn_detail ld
          WHERE lpn_id IN (SELECT lpn_id 
                           FROM lpn 
                           WHERE tc_order_id IN (SELECT major_order_ctrl_nbr
                                                 FROM orders
                                                 WHERE tc_order_id = '0756637081') -- minor order
                          )
          GROUP BY item_id
          )

SELECT x.order_qty, x.orig_order_qty, x.units_pakd,
       COALESCE(x.item_id,y.item_id) AS item_id,
       y.initial_qty, y.size_value
FROM x
FULL OUTER JOIN y ON y.item_id = x.item_id
;
