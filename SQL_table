WITH table_1 AS (
        SELECT 
            tc.topic as topic,
            date_format(c.comm_created_dttm, '%d.%m.%Y') as created,
            c.comm_contact_id,
            COUNT(*) as request,
            row_number() OVER(partition by tc.topic, c.comm_contact_id) as repeated
        FROM test.topic_comm tc
        JOIN test.comm c ON tc.comm_id =  c.comm_id
        GROUP BY tc.topic, c.comm_contact_id, date_format(c.comm_created_dttm, '%d.%m.%Y'))
SELECT 
    topic,
    created,
    SUM(IF(repeated = 1, 1, 0)) as total_initial,
    SUM(
        CASE
            WHEN request > 1 AND repeated > 1 THEN request
            WHEN request > 1 THEN request - 1
            WHEN repeated > 1 THEN 1
            ELSE 0
        END
    ) AS total_repeated,
    SUM(request) as total_requests
FROM table_1
GROUP BY topic, created 
ORDER BY topic 
