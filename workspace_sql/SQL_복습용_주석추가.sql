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
