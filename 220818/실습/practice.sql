-- id PRIMARY KEY,
-- sido INTEGER NOT NULL,
-- gender INTEGER NOT NULL,
-- age INTEGER NOT NULL,
-- height INTEGER NOT NULL,
-- weight INTEGER NOT NULL,
-- waist REAL NOT NULL,
-- va_left REAL NOT NULL,
-- va_right REAL NOT NULL,
-- blood_pressure INTEGER NOT NULL,
-- smoking INTEGER NOT NULL,
-- is_drinking BOOLEAN NOT NULL

SELECT smoking, count(*) FROM healthcare WHERE smoking LIKE '_' GROUP BY smoking;

SELECT is_drinking, count(*) FROM healthcare WHERE is_drinking LIKE '_' GROUP BY is_drinking;

SELECT count(*) FROM healthcare GROUP BY is_drinking HAVING blood_pressure >= 200;

SELECT sido, count(*) FROM healthcare GROUP BY sido HAVING 