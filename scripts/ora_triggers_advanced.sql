CREATE OR REPLACE TRIGGER test_trigger
    AFTER UPDATE 
    OF balance
    ON customer
    FOR EACH ROW
    WHEN (NEW.balance > OLD.balance) -- Condition with inserted and old values

DECLARE

BEGIN
    INSERT INTO event_log
        VALUES(event_log_sq.NEXTVAL, SYSDATE, 'ADMIN', 'CUSTOMER', :NEW.balance, :OLD.balance, 'TESTING') ; -- binding :NEW, :OLD
END ;
/
