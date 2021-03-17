CREATE OR REPLACE PROCEDURE test_procedure (c_id IN NUMBER,
                                            v_cur OUT SYS_REFCURSOR) -- OUT
AS

BEGIN
    OPEN v_cur FOR
        SELECT *
        FROM sales 
        WHERE customer_id = c_id ;
END ;
/

CREATE OR REPLACE PROCEDURE tmp_procedure (c_id IN NUMBER)
AS
    v_rec sales%ROWTYPE ;
    v_cur SYS_REFCURSOR ;
BEGIN
    test_procedure(c_id, v_cur) ; -- Calling procedure
    LOOP
        FETCH v_cur INTO v_rec ;
        EXIT WHEN v_cur%NOTFOUND ;
            DBMS_OUTPUT.PUT_LINE(v_rec.sales_date) ;
    END LOOP ;
    CLOSE v_cur ;
END ;
/
