# Database 02

## Update

|     | 구문     | 예시                                         |
| --- | ------ | ------------------------------------------ |
| C   | INSERT | INSERT INTO 테이블이름 (컬럼 1,..) VALUES (값1,..) |
| R   | SELECT | SELECT * FROM * 테이블이름 WHERE 조건;            |
| U   |        |                                            |
| D   |        |                                            |

## WHERE

.mode csv 모드를 csv로

.import users.csv users

## LIKE

like phone = '%-5114-%'

## ORDER BY

ascending 오름차순 asc

descending 내림차순 dscd

select * from users order by age limit 10;

select * from users order by age , last_name limit 10;

select last_name, first_name balance from users order by balance desc limit 10;
