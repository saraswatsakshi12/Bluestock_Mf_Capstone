-- 1. Top 5 funds by AUM

SELECT 
scheme_name,
aum_crore
FROM fact_aum
ORDER BY aum_crore DESC
LIMIT 5;



-- 2. Average NAV per month

SELECT
strftime('%Y-%m', date) AS month,
AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY month;



-- 3. SIP vs Lumpsum transactions

SELECT
transaction_type,
COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY transaction_type;



-- 4. Total investment by state

SELECT
state,
SUM(amount) AS total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_amount DESC;



-- 5. Funds with expense ratio < 1%

SELECT
scheme_name,
expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;



-- 6. Highest 5 year returns

SELECT
scheme_name,
return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 5;



-- 7. Average transaction amount

SELECT
AVG(amount) AS avg_transaction
FROM fact_transactions;



-- 8. Number of schemes by category

SELECT
category,
COUNT(*) 
FROM dim_fund
GROUP BY category;



-- 9. High risk funds

SELECT
scheme_name,
risk_grade
FROM dim_fund
WHERE risk_grade='High';



-- 10. NAV range

SELECT
MAX(nav) AS max_nav,
MIN(nav) AS min_nav
FROM fact_nav;