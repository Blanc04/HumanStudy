-- 주석
/*
범위 주석
*/

create database human;
use human;

select * from emp;
select * from dept;
select * from salgrade;

select empno from emp;
select empno, ename from emp;

select
	empno,
	ename
from
	emp;

select job from emp;
-- 중복 결과를 하나만 보여줌
select distinct job from emp;

select job as 직업 from emp;
select job as "직업 이름" from emp;
select job 직업 from emp;

select sal, sal*12 from emp;

select 100*12;

select sal, comm, sal + comm from emp;
-- select ename+sal from emp;

select * 
from emp
where deptno = 20;

select * 
from emp
where deptno = 20 and job='CLERK';

select * from emp
where deptno = 20 or job='CLERK';

select * from emp
where deptno = 30 or deptno = 20 and job = 'CLERK';

select * from emp
where sal = 3000;

select * from emp
where sal != 3000;

select * from emp
where sal <> 3000;

select * from emp
where not (sal = 3000);

select * from emp
where sal >= 2000 and sal < 3000;

-- between A and B
-- A 이상 and B이하
select * from emp
where sal between 2000 and 3000;

select * from emp
where job='CLECK' or (sal > 2000 and DEPTNO=10)

-- 컬럼이 같고 or로 연결되어 있는 경우
-- in으로 간편하게 표현 가능
select * from emp
where deptno in (20, 30, 10)

select * from emp
where deptno not in (20, 30);

-- %: 모든 글자를 뜻함
select * from emp
where ename like 'S%';

select * from emp
where ename like '%N';

select * from emp
where ename like '%AM%';

select * from emp
where ename like '_L%';

-- 문제
-- 이름이 5글자인 사람만 출력
select * from emp
where ename like '_____%';

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
select * from emp
where (deptno = 10 or deptno = 20) and lower(ename) like lower('%A%');

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

select * from emp
where sal > 1000
order by deptno desc, job, empno;

-- limit
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




