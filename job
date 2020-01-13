BEGIN
    DBMS_SCHEDULER.CREATE_JOB (job_name             => 'deleting_job',
                               job_type             => 'STORED_PROCEDURE', -- PLSQL_BLOCK
                               job_action           => 'delete_all_test', -- BEGIN ... ; END ;
                               start_date           => SYSTIMESTAMP,
                               repeat_interval      => 'freq=daily; interval=1;', --hourly
                               end_date             => NULL,
                               enabled              => TRUE,
                               comments             => 'Testing dayly job') ;
END ;
