create or replace PROCEDURE delete_test_objects
AS
    v_rec all_objects%ROWTYPE ;
    v_cur SYS_REFCURSOR ;

BEGIN
    OPEN v_cur FOR
        SELECT *
        FROM all_objects 
        WHERE owner LIKE 'ADMIN' 
          AND ( object_name LIKE 'TEST%' 
             OR object_name LIKE 'TMP%' ) ;

    LOOP    
        FETCH v_cur INTO v_rec ;
        EXIT WHEN v_cur%NOTFOUND ;
            EXECUTE IMMEDIATE 'DROP ' || v_rec.object_type || ' ' || v_rec.object_name ;

    END LOOP ;
    COMMIT ;

    INSERT INTO event_log 
        VALUES (event_log_sq.NEXTVAL, SYSDATE, 'JOB', NULL, NULL, NULL, 'TEST OBJECTS HAVE BEEN DELETED') ;

    COMMIT ;

    CLOSE v_cur ;

END ;