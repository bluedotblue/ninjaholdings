#Total number of customers who signed up in 2024.
#SELECT COUNT(c.id) AS total_customer_signups_2024 
#FROM nh_db.customers c
#WHERE c.signup_date BETWEEN "2024-01-01" AND "2024-12-31";

#Top 5 customers by total transaction amount.
#SELECT c.id, c.name, ROUND(SUM(t.amount), 2) AS total_transaction_amount
#FROM nh_db.customers c
#LEFT JOIN nh_db.transactions t ON c.id = t.customer_id
#GROUP BY c.id
#HAVING total_transaction_amount IS NOT NULL
#ORDER BY total_transaction_amount DESC
#LIMIT 5;

#Average transaction amount by state.
SELECT c.state, ROUND(AVG(t.amount),2) AS avg_amount
FROM nh_db.customers c
LEFT JOIN nh_db.transactions t ON c.id = t.customer_id
GROUP BY c.state;





