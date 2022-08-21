-- 3
SELECT * FROM albums ORDER BY title DESC LIMIT 5;

-- 4
SELECT count(*) as "고객 수" FROM customers;

-- 5
SELECT FirstName as 이름, LastName as 성 FROM customers 
WHERE Country = 'USA' ORDER BY FirstName DESC limit 5;

-- 6
SELECT count(*) as 송장수 FROM invoices WHERE BillingPostalCode not NULL;

-- 7
SELECT * FROM invoices WHERE BillingState not NULL 
ORDER BY InvoiceDate DESC limit 5;

-- 8
SELECT count(*) FROM invoices WHERE InvoiceDate 
BETWEEN "2013-01-01" AND "2013-12-31";

-- 9
SELECT CustomerId AS 고객ID, FirstName AS 이름, 
LastName AS 성 FROM customers
WHERE FirstName LIKE 'L%' ORDER BY CustomerId;

-- 10
SELECT Country AS 나라, count(*) AS "고객 수"
FROM customers GROUP BY Country 
ORDER BY count(*) DESC LIMIT 5;

-- 11
SELECT ArtistId, count(*) FROM albums GROUP BY ArtistId
ORDER BY count(*) DESC limit 1;

-- 12
SELECT ArtistId, count(*) FROM albums GROUP BY ArtistId
HAVING count(*) > 9 ORDER BY count(*) DESC

-- 13
SELECT country, state, count(*) AS "고객 수" FROM customers
WHERE state LIKE '%' GROUP BY country, State
ORDER BY count(*) DESC, country DESC LIMIT 5;

-- 14
SELECT 
  CustomerId,
  CASE
    WHEN Fax is NULL THEN "X"
    WHEN Fax not NULL THEN "O"
  END AS "Fax 유/무"
 FROM customers ORDER BY CustomerId LIMIT 5;

-- 15
SELECT LastName, FirstName, 
strftime('%Y','now') - substr(BirthDate,1,4) + 1 as 나이
FROM employees ORDER BY EmployeeId;

-- 16
SELECT name FROM artists WHERE artistID = (
SELECT ArtistId FROM albums
GROUP BY ArtistId
ORDER BY count(*) DESC limit 1);

-- 17
select name from genres WHERE GenreId = (
select GenreId FROM tracks GROUP BY GenreId
ORDER BY count(*) LIMIT 1);
