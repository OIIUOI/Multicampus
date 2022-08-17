

SELECT count(*) FROM healthcare;

SELECT max(age), min(age) FROM healthcare;

SELECT max(height), min(height), max(weight), min(weight) FROM healthcare;

SELECT count(*) FROM healthcare WHERE (160 <= height) and (height <= 170);

SELECT * FROM healthcare where is_drinking = 1 ORDER BY waist limit 5;

SELECT count(*) FROM healthcare WHERE (va_left >= 1.5) and (va_right >= 1.5) and (is_drinking = 1);

SELECT count(*) FROM healthcare WHERE blood_pressure < 120;

SELECT AVG(waist) FROM healthcare WHERE blood_pressure >= 140;

SELECT AVG(height), AVG(weight) FROM healthcare WHERE gender = 1;

SELECT id, height, weight FROM healthcare ORDER BY height desc, weight desc limit 1 OFFSET 1;

SELECT count(*) FROM healthcare WHERE weight/(height*height*0.0001) >= 30;

SELECT id, weight/(height*height*0.0001) FROM healthcare WHERE smoking = 3 ORDER BY weight/(height*height*0.0001) DESC LIMIT 5;

SELECT AVG(blood_pressure) FROM healthcare WHERE (gender = 1) and (is_drinking = 1) ORDER BY smoking DESC limit 100;

SELECT AVG(blood_pressure) FROM healthcare WHERE (gender = 0) and (is_drinking = 1) ORDER BY smoking DESC limit 100;

SELECT AVG(blood_pressure) FROM healthcare WHERE weight/(height*height*0.0001) >= 30 ORDER BY blood_pressure DESC LIMIT 10;