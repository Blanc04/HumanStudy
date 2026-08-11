-- 주석
/*
범위 주석
*/
-- 데이터베이스를 생성하고, 이후 사용할 데이터베이스를 human으로 지정
create database human;
use human;

-- *는 테이블의 모든 컬럼을 조회
select * from emp;
select * from dept;
select * from salgrade;

-- 필요한 컬럼만 골라서 조회할 수 있음
select empno from emp;
select empno, ename from emp;
-- SELECT / FROM은 줄을 나눠 작성해도 실행 결과는 같음
select
empno,
ename
from
emp;
select job from emp;

-- 중복 결과를 하나만 보여줌
select distinct job from emp;

-- as를 사용하면 조회 결과의 컬럼 이름에 별칭을 붙일 수 있음
-- 공백이 들어간 별칭은 따옴표로 감싸서 표현
select job as 직업 from emp;
select job as "직업 이름" from emp;
-- AS는 생략 가능
select job 직업 from emp;

-- 조회하는 컬럼에 바로 산술 연산을 적용할 수 있음
select sal, sal*12 from emp;
-- 테이블 조회 없이 계산 결과만 확인하는 것도 가능
select 100*12;
-- NULL이 산술 연산에 포함되면 결과도 NULL이 됨
select sal, comm, sal + comm from emp;
-- select ename+sal from emp;

-- WHERE는 조회할 행의 조건을 지정
select *
from emp
where deptno = 20;

-- AND는 두 조건을 모두 만족해야 함
select *
from emp
where deptno = 20 and job='CLERK';
-- OR는 둘 중 하나만 만족해도 됨
select * from emp
where deptno = 20 or job='CLERK';
-- AND가 OR보다 먼저 계산되므로 조건이 복잡하면 괄호로 우선순위를 명확히 하는 것이 좋음
select * from emp
where deptno = 30 or deptno = 20 and job = 'CLERK';

-- 비교 연산자
select * from emp
where sal = 3000;
select * from emp
where sal != 3000;
select * from emp
where sal <> 3000;
-- NOT으로 조건의 결과를 반대로 만들 수도 있음
select * from emp
where not (sal = 3000);
select * from emp
where sal >= 2000 and sal < 3000;

-- between A and B
-- A 이상 and B이하
select * from emp
where sal between 2000 and 3000;

-- 괄호를 사용하면 여러 조건의 계산 순서를 직접 지정할 수 있음
select * from emp
where job='CLECK' or (sal > 2000 and DEPTNO=10)

-- 컬럼이 같고 or로 연결되어 있는 경우
-- in으로 간편하게 표현 가능
select * from emp
where deptno in (20, 30, 10)
-- NOT IN은 괄호 안의 값에 해당하지 않는 행만 조회
select * from emp
where deptno not in (20, 30);

-- LIKE는 문자열의 특정 패턴을 찾을 때 사용
-- %: 모든 글자를 뜻함
select * from emp
where ename like 'S%';
select * from emp
where ename like '%N';
select * from emp
where ename like '%AM%';
-- _는 정확히 한 글자를 뜻함
select * from emp
where ename like '_L%';

-- 문제
-- 이름이 5글자인 사람만 출력
select * from emp
where ename like '_____%';

-- LOWER / UPPER는 문자열을 각각 소문자 / 대문자로 변환
select 'Human';
select lower('Human');
select upper('Human');

-- 문제
-- 'Am'을 이용해서 am이 이름 중간에 들어가는 사람만 출력
-- mariaDB는 like에서 대소문자 구분 원래 안함
select * from emp
where lower(ename) like lower('%Am%');

-- 문제
-- 부서 10 또는 20의 사원 중 이름에 A가 들어가는 사원만 출력
-- 부서 조건을 괄호로 묶은 뒤 이름 조건과 AND로 연결
select * from emp
where (deptno = 10 or deptno = 20) and lower(ename) like lower('%A%');

-- NULL은 일반 비교 연산자가 아니라 IS NULL / IS NOT NULL로 검사
select * from emp
where comm < 100:
select * from emp
where comm is null:
select * from emp
where comm is not null:

-- order by
-- ORDER BY는 조회 결과의 정렬 기준을 지정
select * from emp
order by sal;
-- asc: 오름차순
select * from emp
order by sal asc;
select * from emp
order by sal dest;
select * from emp
order by sal deptno;
-- order by에 여러 컬럼이 적혀있는 경우
-- 왼쪽부터 적용되고 동일한 값이 있는 경우 다름 조건이 적용됨
select * from emp
order by deptno desc, job;
select * from emp
order by deptno desc, job, empno;

-- WHERE로 먼저 행을 거른 뒤 ORDER BY로 결과를 정렬
select * from emp
where sal > 1000
order by deptno desc, job, empno;

-- limit
-- 정렬된 결과 중 앞에서 지정한 개수만 조회
select *
from emp
where sal > 1000
order by deptno desc, job, empno
limit 3;
-- limit offset, rows
-- offset만큼 건너뛰고 rows만큼 보여줌
select *
from emp
where sal > 1000
order by deptno desc, job, empno
limit 5, 3;

-- 문제
select * from emp
where
(deptno = 20 or deptno = 30)
and sal between 2000 and 3000
order by sal asc, ename desc;

-- 집계 함수: 여러 행의 값을 하나의 결과로 계산
-- COUNT(컬럼)은 해당 컬럼의 NULL을 제외하고 개수를 셈
select count(ename) from emp;
select count(mgr) from emp;
select count(comm) from emp; --null은 개수에서 제외
-- COUNT(*)는 행 자체의 개수를 세기 때문에 NULL 여부와 관계없이 전체 행을 셈
select count(*) from emp;
-- MAX / MIN / SUM / AVG는 각각 최댓값 / 최솟값 / 합계 / 평균
select max(sal) from emp;
select min(sal) from emp;
select sum(sal) from emp;
select avg(sal) from emp;
select count(*), ename from emp;

-- LENGTH는 문자열의 길이를 구함
select length(ename), ename from emp;
select * from emp
where length(ename) = 4;

-- 대상의 몇 번째부터 몇 개를 잘라오기
-- SUBSTRING과 SUBSTR은 여기서는 같은 용도로 사용
select substring(ename, 2, 3), ename from emp;
select substr(ename, 2, 3), ename from emp;

-- 전부 교체
select replace(ename, "A", "에이"), ename from emp;

-- 대상의 자리수를 맞춰주고 남으면 채워줌
-- LPAD는 왼쪽, RPAD는 오른쪽을 지정 문자로 채움
select lpad(ename, 10, '#') from emp;
select lpad(ename, 3, '#') from emp;
select rpad(ename, 10, '#') from emp;
select rpad(ename, 3, '#') from emp;

-- TRIM은 문자열 양 끝의 공백을 제거
select trim('  a b  c   ');
-- CONCAT은 문자열을 이어 붙임
select concat(ename, job) from emp;
select concat(ename, ' ', job) from emp;
-- 오라클에서 합치기 ename || job으로 사용가능
-- CONCAT_WS는 첫 번째 인자를 구분자로 사용해서 나머지 값을 연결
select concat_ws('-', ename, job, empno) from emp;

-- 반올림
select round(3.14);
-- 두 번째 인자는 소수점 아래 몇 자리까지 남길지 지정
select round(3.145, 2);
-- 올림
select ceil(3.14);
select ceil(-3.14);
-- 내림
select floor(3.14);
select floor(-3.14);
-- 버림
select truncate(-3.14, 1);
-- 나머지
select mod(10, 3);

-- 현재 날짜와 시간을 가져오는 함수
select now();
select sysdate();
-- 날짜 출력 양식 지정
select DATE_FORMAT(now(), '%Y년 %m월 %d일 %H시 %i분 %s초');
-- 문자를 날짜 형으로 변화
select str_to_date('2026-08-07', '%Y-%m-%d');

-- IFNULL(값, 대체값): 값이 NULL이면 두 번째 값을 사용
select ifnull(comm, 0), comm from emp;
select sal * 12 + comm from emp;
-- NULL인 comm을 0으로 바꾸면 연봉 계산 결과가 NULL이 되는 것을 막을 수 있음
select sal * 12 + ifnull(comm, 0) from emp;

-- 문제
-- ename의 앞 두 글자만 출력
select substr(ename, 1, 2), ename from emp;
-- ename의 앞 두 글자만 원본 그대로 출력하고 4개의 *를 붙여서 출력
-- SM****
select rpad(substr(ename, 1, 2), 6, '*') from emp;
-- ename의 앞 두 글자만 원본 그대로 출력하고 나머지 이름 만큼의 * 출력
select rpad(substr(ename, 1, 2), length(ename), '*') from emp;

-- case 문
-- CASE는 조건에 따라 서로 다른 값을 반환할 때 사용
select * from emp;
-- 특정 컬럼의 값과 WHEN 값을 직접 비교하는 방식
select
job, sal,
case job
when 'CLERK' then sal * 1.05
when 'SALESMAN' then sal * 1.03
else sal
end as upsal
from emp;
-- WHEN 뒤에 조건식을 직접 작성하는 방식
select
job, sal,
case
when job = 'CLERK' then sal * 1.05
when job = 'SALESMAN' then sal * 1.03
else sal
end as upsal
from emp;
-- NULL 여부도 CASE 조건으로 처리 가능
select
sal, comm,
case
when comm is null then 0
else comm
end
from emp;

-- GROUP BY는 같은 값을 가진 행을 그룹으로 묶어서 집계할 때 사용
select deptno from emp
group by by deptno;
select
deptno, count(*), sum(sal)
from emp
group by deptno;
-- 여러 컬럼을 적으면 컬럼 값의 조합을 기준으로 그룹이 만들어짐
select deptno, job, count(*)
from emp
group by deptno, job;

-- WHERE는 그룹을 만들기 전에 행을 먼저 필터링
select deptno, job
from emp
where deptno = 10
group by deptno, job;
select deptno, job
from emp
where deptno = 10
group by deptno, job
order by job;
select avg(sal) from emp;
/*
select
avg(sal)
from emp
where sal >= avg(sal);
*/

-- HAVING은 GROUP BY로 만든 그룹의 집계 결과에 조건을 걸 때 사용
select
avg(sal) as avg_sal, deptno, job
from emp
group by deptno, job
having avg(sal) >= 2000;
select
avg(sal) as avg_sal, deptno, job
from emp
group by deptno, job
having deptno = 10;
-- where 조건을 having에 적을 수 있지만
-- 통상 group by와 관련된 것만 적기
-- 직업 별로 연봉 1000 이상인 사람이 3명 이상인 경우만 출력
select
job, count(*)
from emp
where sal >= 1000
-- and cnt >=3
-- and count(*) >= 3
group by job
having count(*) >= 3

-- SQL 작성 순서와 실제 처리 순서를 비교하기 위한 표시
/* 5 */ select job, 1 as num
/* 1 */ from emp
/* 2 */ where sal > 1000
/* 3 */ group by job
/* 4 */ having count(*) >= 3
/* 6 */ order by job desc, num

-- UNION은 두 SELECT 결과를 합치면서 중복 행을 제거
select * from emp where deptno = 10
union
select * from emp where deptno = 10;
-- UNION ALL은 중복도 그대로 유지
select * from emp where deptno = 10
union all
select * from emp where deptno = 10;
-- UNION으로 합칠 SELECT들은 결과 컬럼 개수와 위치가 서로 맞아야 함
select sal from emp
union
select ename from emp;

select * from emp
where sal > 1250;

-- 'WAND'의 연복만 출력
select sal
from emp
where ename = 'WAND';

-- 서브쿼리의 결과를 바깥쪽 WHERE 조건에 사용할 수 있음
select * from emp
where sal > (select sal
from emp
where ename = "WAND");
-- 평균 급여보다 많이 받는 사원 조회
select * from emp
where sal > (select avg(sal) from emp);

-- 부서 별 최고 연봉자
-- 1. 부서 별 최고 연봉
select deptno, max(sal)
from emp
group by deptno;
-- IN을 사용하면 여러 값 중 하나와 일치하는지 검사 가능
select ename, sal
from emp
-- where sal = 2850 or sal = 3000 or sal = 5000;
where sal in (2850, 3000, 5000);
-- 위 값을 직접 적는 대신 서브쿼리가 돌려준 여러 결과를 IN에 사용할 수 있음
select ename, sal
from emp
-- where sal = 2850 or sal = 3000 or sal = 5000;
where sal in (select max(sal)
from emp
group by deptno);

select * from dept;

-- 여러 테이블을 FROM에 적고 WHERE에서 연결 조건을 작성하는 기존 JOIN 방식
select *
from emp, dept
where emp.deptno = dept.deptno;
-- 테이블 별칭을 사용하면 긴 테이블 이름을 짧게 적을 수 있음
select *
from emp e, dept d
where e.deptno = d.deptno;
/*
select ename, dname, deptno
from emp e, dept d
where e.deptno = d.deptno;
*/
-- 별칭은 꼭 e, d 같은 짧은 문자일 필요는 없음
select 리얼허거덩거거덩거허얼리.ename, d.name, 리얼허거덩거거덩거허얼리.deptno
from emp 리얼허거덩거거덩거허얼리, dept d
where 리얼허거덩거거덩거허얼리.deptno = d.deptno;

select * from salgrade;

-- 스미스의 연봉 등급은? 정답: 1
-- 이름, 월급, 등급, losal, hisal
-- 급여가 등급의 최저~최고 급여 범위 안에 들어가는 행과 연결
select e.ename, e.sal, s.grade, losal, hisal
from emp e, salgrade s
where (e.sal between s.losal and hisal) and ename='SMITH';

select ename from emp;
-- 사원의 MGR 값은 그 사원의 관리자 EMPNO를 뜻하므로 서브쿼리로 관리자를 찾을 수 있음
where empno = (select
mgr
from emp
where ename = 'SMITH');

-- mgr이 null인 것은 빠짐
-- 같은 EMP 테이블을 두 번 사용해서 사원(e1)과 관리자(e2)를 연결하는 SELF JOIN
select e2.ename, e2.ename
from emp e1, emp e2
where e1.mgr = e2.empno
and e1.ename = 'SMITH';

-- 문제
-- 모든 사람의 이름, 급혀, 부서명, 급여 등급, 등급 내림차순
-- EMP-DEPT는 부서번호로, EMP-SALGRADE는 급여 범위로 각각 연결
select ename, sal, job, grade
from emp e, dept d, salgrade s
where e.deptno = d.deptno
and e.sal between s.LOSAL and s.HISAL
order by grade desc, sal desc;

-- 테이블명.* 또는 별칭.* 으로 해당 테이블의 모든 컬럼을 선택 가능
select ename, ename from emp;
select ename, emp.* from emp;
select ename, e.* from emp e;

-- ANSI JOIN 문법: JOIN ... ON으로 연결 조건을 작성
select e.deptno
from emp e join dept d on(e.deptno = d.deptno);
-- 두 테이블의 조인 컬럼 이름이 같으면 USING으로 간단히 작성 가능
select deptno
from emp e join dept d using(deptno);

-- INNER JOIN은 양쪽 테이블에서 조인 조건이 일치하는 행만 출력
select e1.empno, e1.ename, e2.empno, e2.ename
from emp e1
join emp e2 on e1.mgr = e2.empno;
-- LEFT OUTER JOIN은 왼쪽 테이블의 행을 전부 유지
select e1.empno, e1.ename, e2.empno, e2.ename
from emp e1
left outer join emp e2 on e1.mgr = e2.empno;
-- RIGHT OUTER JOIN은 오른쪽 테이블의 행을 전부 유지
select e1.empno, e1.ename, e2.empno, e2.ename
from emp e1
right outer join emp e2 on e1.mgr = e2.empno;

select * from dept;

-- 문제
-- deptno, dname, empno, ename
-- 모든 부서가 다 나오게
-- 부서번호 오름차순, 이름 오름차순
-- DEPT를 왼쪽에 두고 LEFT JOIN하므로 사원이 없는 부서도 결과에 남음
select deptno, dname, empno, ename
from dept d
left outer join emp e using(deptno)
order by deptno, ename;

select sal from emp where ename = 'SCOTT';

-- SELECT 절 안의 서브쿼리는 각 행에서 하나의 값처럼 사용할 수 있음
-- 여기서는 급여 3000이 어느 SALGRADE 범위에 속하는지 조회해 grade 컬럼으로 표시
select
sal,
ename,
(select grade
from salgrade
where 3000 between losal and hisal) as grade
from emp where ename = 'SCOTT';

-- having 없이 서브쿼리로 해결
-- GROUP BY 결과를 다시 바깥 SELECT의 테이블처럼 사용해서 조건을 걸 수도 있음
-- 1. 부서 별 평균 연봉 출력
select avg(sal)
from emp
group by deptno;
-- 2. 부서 별 평균 연봉이 2000 이상인 부서만 출력
-- having 사용
select avg(sal) avg_sal
from emp
-- where avg_sal >= 2000
-- where avg(sal) >= 2000
group by deptno
having avg(sal) >= 2000;

-- 서브쿼리 사용
-- FROM 안에 들어간 서브쿼리를 인라인 뷰(파생 테이블)처럼 사용
-- 안쪽에서 계산한 avg_sal을 바깥 WHERE에서 일반 컬럼처럼 조건 검사
select *
from (
	select avg(sal) avg_sal
	from emp
	group by deptno
) a
where avg_sal >= 2000;

-- DDL
-- DDL(Data Definition Language): 테이블 같은 데이터베이스 구조 자체를 생성/변경/삭제
-- create
-- DESC는 테이블의 컬럼, 자료형, NULL 허용 여부, KEY 등의 구조를 확인
desc emp;

-- CREATE TABLE로 새 테이블의 컬럼과 제약조건을 직접 정의
create table emp2(
	empno int(4) primary key,
	ename varchar(10) not null,
	job varchar(9),
	mgr int(4),
	hiredate date,
	sal decimal(7, 2), -- 총 7자리, 그 중 2자리는 소수점
	comm decimal(7, 2),
	deptno int(2)
);
select * from emp2;
desc emp2;

desc dept;
create table dept2(
	deptno int(2) primary key,
	dname varchar(14),
	lot varchar(13)
);
select * from dept2;

-- 테이블 복사
-- CREATE TABLE ... AS SELECT ... : SELECT 결과를 기반으로 새 테이블 생성
-- 아래 문장은 EMP의 데이터까지 함께 복사
create table emp_copy
as select * from emp;

select * from emp_copy

-- 1 <> 1은 항상 거짓이므로 조회되는 행이 없음
-- 따라서 컬럼 구조만 만들어지고 데이터는 복사되지 않음
create table emp_copy2
as select * from emp where 1 <> 1;

select * from emp_copy2;

-- 1 != 1 역시 항상 거짓이므로 데이터 없이 테이블 형태만 생성
create table dept3
as select * from dept where 1 != 1;

select * from dept3;

-- PRIMARY KEY는 각 행을 유일하게 식별
-- FOREIGN KEY는 다른 테이블의 키를 참조해서 테이블 사이의 관계를 제한
create table emp3 (
	empno int(4),
	ename varchar(10) not null,
	job varchar(9),
	mgr int(4),
	hiredate date,
	sal decimal(7, 2), -- 총 7자리, 그 중 2자리는 소수점
	comm decimal(7, 2),
	deptno int(2), 
	primary key (empno),
	foreign key (deptno) references dept3(deptno)
);

-- 테이블 삭제
-- DROP TABLE은 테이블의 데이터뿐 아니라 테이블 구조 자체도 삭제
drop table dept3;

create table dept3(
	deptno int(2) primary key,
	ename varchar(14),
	loc varchar(13)
);

-- alter
-- ALTER TABLE은 이미 만들어진 테이블의 구조를 변경
-- ADD: 새 컬럼 추가 / DEFAULT: 값을 생략했을 때 사용할 기본값
alter table emp3
add gender varchar(10) not null default '남';
select * from emp3;

-- CHANGE는 컬럼 이름과 정의를 함께 변경할 때 사용
alter table emp3
change gender gender2 varchar(10);
select * from emp3;

-- RENAME COLUMN은 컬럼 이름만 변경
alter table emp3
rename column gender2 to gender3;
select * from emp3;

-- DROP COLUMN은 테이블에서 해당 컬럼을 제거
alter table emp3
drop column gender;
select * from emp3;

-- RENAME TO는 테이블 자체의 이름을 변경
alter table emp3
rename to emp4;
select * from emp4;

drop table emp4;
drop table dept3;

select * from emp_copy;
-- TRUNCATE는 테이블 구조는 남겨두고 내부 행을 전부 비움
truncate table emp_copy;

select * from dept2;
drop table dept2;

select * from emp2;
drop table emp2;

create table dept2(
	deptno int(2) primary key,
	ename varchar(14),
	loc varchar(13)
);

-- DEFAULT를 지정한 컬럼은 INSERT에서 값을 생략하면 기본값이 사용됨
create table emp2(
	empno int(4),
	ename varchar(10) not null,
	job varchar(9) default 'CLERK',
	mgr int(4),
	hiredate date default now(),
	sal decimal(7, 2), -- 총 7자리, 그 중 2자리는 소수점
	comm decimal(7, 2),
	deptno int(2),
	primary key (empno),
	foreign key (deptno) references dept2(deptno)
);
select * from emp2;

-- INSERT INTO ... VALUES는 새 행을 추가
-- 컬럼 목록을 생략하면 테이블에 정의된 컬럼 순서대로 값을 전부 맞춰 넣어야 함
insert into dept2
values (
	10,
	'휴먼',
	'천안'
);

insert into emp2
values (
	1000, 
	'변에이딘', 
	'MANAGER', 
	2000, 
	'2026-08-09',
	4000,
	100,
	10
);
select * from emp2;

-- INSERT에 컬럼 목록을 적으면 지정한 컬럼에만 값을 넣을 수 있음
-- 생략된 컬럼은 DEFAULT가 있으면 기본값, 없으면 NULL이 사용됨
insert into emp2 (empno, ename, sal, comm, deptno)
values (1001, '강사', 4100, 150, 10);

-- ename은 not null 제한
-- insert에 누락하면 null이 들어감
-- 그래서 에러 발생
/*
insert into emp2 (empno, sal, comm, deptno)
values (1001, 4100, 150, 10);
*/

-- primary key
-- unique + not null
/*
insert into emp2 (empno, ename, sal, comm, deptno)
values (1001, '강사', 4100, 150, 10);
*/

-- dept 테이블에 deptno 20값이 없어서 에러
/*
insert into emp2 (empno, ename, sal, comm, deptno)
values (1002, '강사', 4100, 150, 20);
*/

-- VALUES 뒤에 괄호를 여러 개 적으면 한 번의 INSERT로 여러 행을 추가
insert into emp2 (empno, ename, sal, comm, deptno)
values
(1002, '강사2', 4100, 150, 10),
(1003, '강사3', 4100, 150, 10),
(1004, '강사4', 4100, 150, 10);

select * from emp2;

-- update
-- UPDATE는 기존 행의 값을 수정
-- 아래처럼 WHERE가 없으면 EMP2의 모든 행이 수정됨
update emp2
set
	sal = 1000,
	comm = 200;

-- 기존 컬럼 값을 계산식에 다시 사용해서 값을 갱신할 수도 있음
-- WHERE가 있으므로 empno가 1002인 행만 대상
update emp2
set
	sal = sal * 1.1,
	comm = comm * 1.2
where empno = 1002;
select * from emp2;

select * from dept2;
update dept2
set deptno = 20
where deptno = 10;

-- DELETE는 행을 삭제하며 WHERE로 삭제 대상을 지정
delete from emp2
where empno = 1002;
select * from emp2;

-- ROLLBACK은 아직 COMMIT하지 않은 트랜잭션 변경사항을 되돌림
rollback;
select * from emp2;
select * from dept2;

-- COMMIT은 현재까지의 트랜잭션 변경사항을 확정
-- COMMIT된 변경은 그 이전 상태로 ROLLBACK할 수 없음
commit;
rollback;
delete from emp2
where empno = 1013;
select * from emp2;
rollback;
select * from emp2;

-- JOIN은 연속해서 여러 테이블을 연결할 수도 있음
-- LEFT OUTER JOIN이므로 왼쪽 EMP(e)의 행은 조건이 맞지 않아도 유지됨
select *
from emp e
	left outer join emp e2 on(e.mgr = e.empno)
	left outer join dept d on(e.deptno = d.deptno)
order by e.ename desc;

select * from emp
where deptno = 10;

-- index
-- INDEX는 특정 컬럼 검색/정렬에 사용할 수 있는 별도의 탐색 구조
-- 아래 인덱스는 empno를 내림차순 기준으로 정의
create index idx_emp_empno_desc
on emp(empno desc);

select * from emp
order by empno desc;

-- deptno 조건 검색용 인덱스 생성
create index idx_emp_deptno
on emp(deptno);

select * from emp
where deptno = 10;

-- FORCE INDEX는 옵티마이저에게 지정한 인덱스를 사용하도록 강하게 지시
select *
from emp force index (idx_emp_deptno)
where deptno = 10
order by deptno;

-- mariadb 한글 한 글자는 3byte
-- LENGTH는 문자 개수가 아니라 문자열이 차지하는 바이트 수를 반환
select length('한글');
select length('ab');

-- 현재 가장 큰 번호에 1을 더해서 다음 번호를 직접 계산하는 방식
select max(empno)+1 from emp;

-- AUTO_INCREMENT를 사용하면 새 행이 들어올 때 번호를 자동 증가시킬 수 있음
create table emp_auto (
	empno int auto_increment,
	ename varchar(50),
	
	primary key(empno)
);

insert into emp_auto (ename)
values ('에이딘');

select * from emp_auto;

insert into emp_auto (ename)
values ('에이딘2');
select * from emp)_auto;

-- 무한 대댓글
-- 아래 UNION ALL 예시는 관리자 없는 최상위 행(level 1)과 특정 관리자의 직속 부하(level 2)를 직접 합침
-- 단계가 더 깊어질 수 있는 구조는 WITH RECURSIVE로 반복 탐색할 수 있음
select
	empno, ename, mgr, 1 as level
from emp
where mgr is null
union all
select
	empno, ename, mgr, 2 as level
from emp
where mgr = 7839;

-- WITH RECURSIVE: 이전 단계의 결과를 다시 참조하면서 계층 구조를 반복 조회
-- emp_recu가 재귀 CTE의 이름
with recursive emp_recu as (
	select
		empno, ename, mgr,
		lpad(ename, length(ename), ' '),
		1 as level,
	 	cast(ename as char(200)) as sort_key
	from emp
	-- Anchor(시작) 쿼리: 관리자가 없는 최상위 사원부터 시작
	where mgr is null
	union all
	-- Recursive(반복) 쿼리: 직전 단계의 사원을 관리자로 가진 다음 사원을 계속 연결
	select
		e.empno, e.ename, e.mgr,
		lpad(e.ename, (er.level*2)+length(e.ename), ' '),
		-- 부모 level에 1을 더해서 현재 깊이를 계산
		er.level+1 as level,
		-- 부모의 sort_key 뒤에 현재 이름을 붙여 계층 순서를 유지할 정렬용 키 생성
		concat(er.sort_key, '-', cast(e.ename as char(200))) as sort_key
	from emp e
		join emp_recu er on (e.mgr = er.empno)
)
select * from emp_recu
order by sort_key;

select * from emp;
/*
문제 1
1981년에 입사한 사원 중에서
급여가 가장 낮은 사원을 조회하시오
*/
-- 서브쿼리에서 1981년 입사자 중 최저 급여를 먼저 구하고
-- 바깥 쿼리에서 같은 조건 + 그 급여와 일치하는 사원을 조회
select * from emp
where hiredate like '1981%' and sal = (select min(sal) from emp where hiredate like '1981%');

/*
문제 2
각 부서 별
급여가 가장 높은 사원 가장 낮은 사원의 차이를 조회하시오
출력 : 부서명, 차이 금액
*/
select job, max(sal) - min(sal)
from emp
group by job;

select deptno, max(sal), min(sal) from emp
group by deptno;
select * from emp
where deptno = 10
order by sal;

-- EMP를 DEPT와 연결해야 부서번호가 아니라 실제 부서명(dname)을 출력 가능
-- 같은 부서 그룹 안에서 최고 급여 - 최저 급여를 계산
select d.dname, max(e.sal) - min(e.sal) as salCalc
from emp e join dept d using(deptno)
group by d.deptno, d.dname;

/*
문제 3
BLAKE보다 높은 연봉을 받는 사람들 출력
*/
-- 안쪽 쿼리로 BLAKE의 급여 한 값을 구하고, 그 값보다 큰 사원만 조회
select ename, sal
from emp
where sal > (
	select sal
	from emp
	where ename = 'BLAKE'
);

/*
문제 4
JONES랑 같은 job을 가진 사람들
*/
-- 안쪽 쿼리로 JONES의 JOB을 구한 뒤 같은 JOB을 가진 사원을 조회
select ename, job
from emp
where job = (
	select job
	from emp
	where ename = 'JONES'
);

/*
문제 5
급여 등급 별 사원 수를 등급 오름차순으로 정렬
단, 모든 등급을 표시한다
*/
-- COUNT(*)가 아니라 COUNT(e.empno)를 사용하면 사원이 없는 등급은 0으로 셀 수 있음
select s.grade, count(e.empno)
-- salgrade의 행은 전부 살려둠
from salgrade s
-- 조건에 맞는 emp가 있으면 붙임
left join emp e
    on e.sal between s.losal and s.hisal
group by s.grade
order by s.grade;

/*
문제 6
이름, 급여, 급여 등급, 부서 이름 조회
단, 급여 등급 3 이상만 조회.
급여 등급 내림차순, 등급이 같은 경우 급여 내림차순, 급여가 같은 경우 이름 내림차순
*/
select ename, sal, s.grade, job
from emp e
join salgrade s
    on sal between s.losal and s.hisal
where s.grade >= 3
order by s.grade desc, sal desc, ename desc;

-- EMP + SALGRADE + DEPT 세 테이블을 각각 급여 범위와 부서번호로 연결
select e.ename, e.sal, s.grade, d.dname
from emp e
join salgrade s
    on e.sal between s.losal and s.hisal
join dept d
    on e.deptno = d.deptno
where s.grade >= 3
order by s.grade desc, e.sal desc, e.ename desc;

/*
문제 7
부서명이 SALES인 사원 중
급여 등급이 2 또는 3인 사원을 급여 내림차순으로 정렬
*/
select e.ename, e.sal, s.grade, d.dname
from emp e
join salgrade s
    on e.sal between s.losal and s.hisal
join dept d
    on e.deptno = d.deptno
-- 부서명은 DEPT에서, 급여 등급은 SALGRADE에서 조건 검사
-- IN (2, 3)은 grade = 2 OR grade = 3과 같은 의미
where d.dname = 'SALES'
  and s.grade in (2, 3)
order by e.sal desc;

select * from emp;