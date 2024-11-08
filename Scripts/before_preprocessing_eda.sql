/* count */
select count(*) from pallet;
select count(*) from pallet where TransactionType = 'Allot';
select count(*) from pallet where TransactionType = 'Return';

/* MIN */
select min(QTY) as min from pallet where TransactionType = 'Allot' ;
select min(abs(QTY)) as min from pallet where TransactionType = 'Return' ;

/* MAX */
select max(QTY) as max from pallet where TransactionType = 'Allot' ;
select max(abs(QTY)) as max from pallet where TransactionType = 'Return' ;

/* MEAN */
select avg(QTY) as Mean from pallet where TransactionType = 'Allot' ;
select avg(abs(QTY)) as Mean from pallet where TransactionType = 'Return' ;

/*  MEDIAN */
SELECT QTY AS median_QTY
FROM (
    SELECT QTY, ROW_NUMBER() OVER (ORDER BY QTY) AS row_num,
           COUNT(*) OVER () AS total_count
    FROM pallet where TransactionType = 'Allot'
) AS median
WHERE row_num = (total_count + 1) / 2 OR row_num = (total_count + 2) / 2;   

SELECT abs(QTY) AS median_QTY
FROM (
    SELECT QTY, ROW_NUMBER() OVER (ORDER BY QTY) AS row_num,
           COUNT(*) OVER () AS total_count
    FROM pallet where TransactionType = 'Return'
) AS median
WHERE row_num = (total_count + 1) / 2 OR row_num = (total_count + 2) / 2;

/* Mode */
SELECT QTY AS mode_QTY
FROM (
    SELECT QTY, COUNT(*) AS frequency
    FROM pallet
    where TransactionType = 'Allot'
    GROUP BY QTY
    ORDER BY frequency DESC
    LIMIT 1
) AS mode;

SELECT abs(QTY) AS mode_QTY
FROM (
    SELECT QTY, COUNT(*) AS frequency
    FROM pallet
     where TransactionType = 'Return'
    GROUP BY QTY
    ORDER BY frequency DESC
    LIMIT 1
) AS mode;

/*  VARIANCE */
SELECT VARIANCE(QTY) AS allot_variance
FROM pallet where TransactionType = 'Allot';

SELECT VARIANCE(QTY) AS return_variance
FROM pallet where TransactionType = 'Return';

/* Standard Deviation */
SELECT STDDEV(QTY) AS allot_std
FROM pallet where TransactionType = 'Allot';

SELECT STDDEV(QTY) AS return_std
FROM pallet where TransactionType = 'Return';

/*  RANGE */
SELECT MAX(QTY) - MIN(QTY) AS allot_range
FROM pallet where TransactionType = 'Allot';

SELECT MAX(QTY) - MIN(QTY) AS return_range
FROM pallet where TransactionType = 'Return';

/* SKEWNESS */
SELECT
    (
        SUM(POWER(QTY - (SELECT AVG(QTY) FROM pallet where TransactionType = 'Allot'), 3)) / 
        (COUNT(*) * POWER((SELECT STDDEV(QTY) FROM pallet where TransactionType = 'Allot'), 3))
    ) AS allot_skewness FROM pallet where TransactionType = 'Allot' ;
  SELECT
    (
        SUM(POWER(QTY - (SELECT AVG(QTY) FROM pallet where TransactionType = 'Return'), 3)) / 
        (COUNT(*) * POWER((SELECT STDDEV(QTY) FROM pallet where TransactionType = 'Return'), 3))
    ) AS return_skewness FROM pallet where TransactionType = 'Return';

  /* KURTOSIS */
  
  SELECT  (
        (SUM(POWER(QTY - (SELECT AVG(QTY) FROM pallet where TransactionType = 'Allot'), 4)) / 
        (COUNT(*) * POWER((SELECT STDDEV(QTY) FROM pallet where TransactionType = 'Allot'), 4))) - 3
    ) AS allot_kurtosis  FROM pallet where TransactionType = 'Allot';

  SELECT  (
        (SUM(POWER(QTY - (SELECT AVG(QTY) FROM pallet where TransactionType = 'Return'), 4)) / 
        (COUNT(*) * POWER((SELECT STDDEV(QTY) FROM pallet where TransactionType = 'Return'), 4))) - 3
    ) AS return_kurtosis  FROM pallet where TransactionType = 'Return';
