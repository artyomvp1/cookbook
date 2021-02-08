CREATE OR REPLACE PROCEDURE delete_test_objects
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
            IF v_rec.object_type LIKE 'TABLE' THEN
                EXECUTE IMMEDIATE 'DROP TABLE ' || v_rec.object_name ;
                
            ELSIF v_rec.object_type LIKE 'PROCEDURE' THEN
                EXECUTE IMMEDIATE 'DROP PROCEDURE ' || v_rec.object_name ;
                
            ELSIF v_rec.object_type LIKE 'FUNCTION' THEN
                EXECUTE IMMEDIATE 'DROP FUNCTION ' || v_rec.object_name ;
                
            ELSIF v_rec.object_type LIKE 'TRIGGER' THEN
                EXECUTE IMMEDIATE 'DROP TRIGGER ' || v_rec.object_name ;
                
            END IF ;
            
    END LOOP ;
    COMMIT ;
    
    INSERT INTO event_log 
        VALUES (event_log_sq.NEXTVAL, SYSDATE, 'JOB', NULL, NULL, NULL, 'TEST OBJECTS HAVE BEEN DELETED') ;
        
    COMMIT ;
        
    CLOSE v_cur ;
    
END ;
