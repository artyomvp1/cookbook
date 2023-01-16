/* DESCRIPTION:
Syntax: DBMS_XMLGEN.GETXML('SELECT ...')
*/

DECLARE
  v_sql VARCHAR2(1000) := 'SELECT first_name, last_name, deposit 
                           FROM customer
                           ' ;

BEGIN
  FOR i IN (SELECT DBMS_XMLGEN.GETXML(v_sql) AS xml_result 
            FROM DUAL
            )
  LOOP
    DBMS_OUTPUT.PUT_LINE(i.xml_result) ;
  END LOOP ;

END ;
/
