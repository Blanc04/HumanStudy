<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt" %>
<%@ taglib prefix="fn" uri="http://java.sun.com/jsp/jstl/functions" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>결과 페이지</title>
</head>
<body>
<table border=1>
	<thead>
		<tr>
			<th>empno</th>
			<th>ename</th>
			<th>job</th>
			<th>sal</th>
			<th>mgr</th>
			<th>hiredate</th>
			<th>comm</th>
			<th>deptno</th>
		</tr>
	</thead>
	<tbody>
		<c:if test="${not empty list }">
			<c:forEach var="dto" items="${list}">
			<tr>
				<td>${dto.empno }</td>
				<td>
					<a href="getEmpno?empno=${dto.empno }">${dto.ename }</a>
				</td>
				<td>${dto.job }</td>
				<td>${dto.sal }</td>
				<td>${dto.mgr }</td>
				<td>${dto.hiredate }</td>
				<td>${dto.comm }</td>
				<td>${dto.deptno }</td>
			</tr>
			</c:forEach>
		</c:if>
		<c:if test="${empty list }">
			<tr>
				<td>${empDTO.empno }</td>
				<td>${empDTO.ename }</td>
				<td>${empDTO.job }</td>
				<td>${empDTO.sal }</td>
				<td>${empDTO.mgr }</td>
				<td>${empDTO.hiredate }</td>
				<td>${empDTO.comm }</td>
				<td>${empDTO.deptno }</td>
			</tr>
		</c:if>
	</tbody>
</table>
</body>
</html>