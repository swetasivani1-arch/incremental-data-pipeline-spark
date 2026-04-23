-- Keep latest record per customer
SELECT *
FROM (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY ingesttime DESC) AS rn
    FROM customer_bronze
) t
WHERE rn = 1;
