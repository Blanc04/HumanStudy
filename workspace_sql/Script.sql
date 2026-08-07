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
where comm < 100:

select * from emp
where comm is null:

select * from emp
where comm is not null:

-- order by
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

select count(ename) from emp;
select count(mgr) from emp;
select count(comm) from emp; --null은 개수에서 제외
select count(*) from emp;
select max(sal) from emp;
select min(sal) from emp;
select sum(sal) from emp;
select avg(sal) from emp;
select count(*), ename from emp;

select length(ename), ename from emp;
select * from emp
where length(ename) = 4;

-- 대상의 몇 번째부터 몇 개를 잘라오기
select substring(ename, 2, 3), ename from emp;
select substr(ename, 2, 3), ename from emp;

-- 전부 교체
select replace(ename, "A", "에이"), ename from emp;

-- 대상의 자리수를 맞춰주고 남으면 채워줌
select lpad(ename, 10, '#') from emp;
select lpad(ename, 3, '#') from emp;

select rpad(ename, 10, '#') from emp;
select rpad(ename, 3, '#') from emp;

select trim('  a b  c   ');

select concat(ename, job) from emp;
select concat(ename, ' ', job) from emp;
-- 오라클에서 합치기 ename || job으로 사용가능
select concat_ws('-', ename, job, empno) from emp;

-- 반올림
select round(3.14);
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

select now();
select sysdate();

-- 날짜 출력 양식 지정
select DATE_FORMAT(now(), '%Y년 %m월 %d일 %H시 %i분 %s초');

-- 문자를 날짜 형으로 변화
select str_to_date('2026-08-07', '%Y-%m-%d');

select ifnull(comm, 0), comm from emp;

select sal * 12 + comm from emp;
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
select * from emp;

select 
	job, sal,
	case job
		when 'CLERK' then sal * 1.05
		when 'SALESMAN' then sal * 1.03
		else sal
	end as upsal
from emp;

select 
	job, sal,
	case
		when job = 'CLERK' then sal * 1.05
		when job = 'SALESMAN' then sal * 1.03
		else sal
	end as upsal
from emp;

select
	sal, comm,
	case
		when comm is null then 0
		else comm
	end
from emp;

select deptno from emp
group by by deptno;

select
	deptno, count(*), sum(sal)
from emp
group by deptno;

select deptno, job, count(*)
from emp
group by deptno, job;

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

/* 5 */ select job, 1 as num
/* 1 */ from emp
/* 2 */ where sal > 1000
/* 3 */ group by job
/* 4 */ having count(*) >= 3
/* 6 */ order by job desc, num

select * from emp where deptno = 10
union
select * from emp where deptno = 10;

select * from emp where deptno = 10
union all
select * from emp where deptno = 10;

select sal from emp
union
select ename from emp;

select * from emp
where sal > 1250;

-- 'WAND'의 연복만 출력
select sal
from emp
where ename = 'WAND';

select * from emp
where sal > (select sal 
			 from emp
			 where ename = "WAND");

select * from emp
where sal > (select avg(sal) from emp);

-- 부서 별 최고 연봉자
-- 1. 부서 별 최고 연봉
select deptno, max(sal) 
from emp
group by deptno;

select ename, sal
from emp
-- where sal = 2850 or sal = 3000 or sal = 5000;
where sal in (2850, 3000, 5000);

select ename, sal
from emp
-- where sal = 2850 or sal = 3000 or sal = 5000;
where sal in (select max(sal)
			  from emp
			  group by deptno);

select * from dept;

select *
from emp, dept
where emp.deptno = dept.deptno;

select *
from emp e, dept d
where e.deptno = d.deptno;

/*
select ename, dname, deptno
from emp e, dept d
where e.deptno = d.deptno;
*/

select 리얼허거덩거거덩거허얼리.ename, d.name, 리얼허거덩거거덩거허얼리.deptno
from emp 리얼허거덩거거덩거허얼리, dept d
where 리얼허거덩거거덩거허얼리.deptno = d.deptno;

select * from salgrade;

-- 스미스의 연봉 등급은? 정답: 1
-- 이름, 월급, 등급, losal, hisal

select e.ename, e.sal, s.grade, losal, hisal
from emp e, salgrade s
where (e.sal between s.losal and hisal) and ename='SMITH';

select ename from emp;

where empno = (select
					mgr
				from emp
				where ename = 'SMITH');

-- mgr이 null인 것은 빠짐
select e2.ename, e2.ename
from emp e1, emp e2
where e1.mgr = e2.empno
and e1.ename = 'SMITH';

-- 문제
-- 모든 사람의 이름, 급혀, 부서명, 급여 등급, 등급 내림차순
select ename, sal, job, grade
from emp e, dept d, salgrade s
where e.deptno = d.deptno
and e.sal between s.LOSAL and s.HISAL
order by grade desc, sal desc;

select ename, ename from emp;
select ename, emp.* from emp;
select ename, e.* from emp e;

select e.deptno
from emp e join dept d on(e.deptno = d.deptno);

select deptno
from emp e join dept d using(deptno);

select e1.empno, e1.ename, e2.empno, e2.ename
from emp e1
	join emp e2 on e1.mgr = e2.empno;

select e1.empno, e1.ename, e2.empno, e2.ename
from emp e1
	left outer join emp e2 on e1.mgr = e2.empno;

select e1.empno, e1.ename, e2.empno, e2.ename
from emp e1
	right outer join emp e2 on e1.mgr = e2.empno;

select * from dept;

-- 문제
-- deptno, dname, empno, ename
-- 모든 부서가 다 나오게
-- 부서번호 오름차순, 이름 오름차순
select deptno, dname, empno, ename
from dept d
	left outer join emp e using(deptno)
order by deptno, ename;

select sal from emp where ename = 'SCOTT';

select 
	sal, 
	ename, 
	(select grade
		from salgrade
		where 3000 between losal and hisal) as grade
from emp where ename = 'SCOTT';
