-- 테이블 만들기
CREATE TABLE healthcare (
id PRIMARY KEY,
sido INTEGER NOT NULL,
gender INTEGER NOT NULL,
age INTEGER NOT NULL,
height INTEGER NOT NULL,
weight INTEGER NOT NULL,
waist REAL NOT NULL,
va_left REAL NOT NULL,
va_right REAL NOT NULL,
blood_pressure INTEGER NOT NULL,
smoking INTEGER NOT NULL,
is_drinking BOOLEAN NOT NULL
);

-- csv import 하기
.mode csv 
.import health.csv healthcare

-- 모든 데이터 출력
SELECT COUNT(*) FROM healthcare;

-- 나이 그룹이 10 미만
select count(*) from healthcare where (age <10);


-- 성별이 1
select count(*) from healthcare where (gender = 1);

-- 흡연 수치(smoking)가 3이면서 음주(is_drinking)가 1인 사람
select count(*) from healthcare where (smoking = 3) and (is_drinking=1);

-- 양쪽 시력이(va_left, va_right) 모두 2.0이상인 사람
select count(*) from healthcare where (va_left >= 2) and (va_right >= 2);

-- 시도(sido)를 모두 중복 없이 출력
select distinct sido from healthcare;