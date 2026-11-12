package com.example.demo.dao;

import java.util.List;
import java.util.Map;

import org.apache.ibatis.session.SqlSession;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import com.example.demo.dto.EmpDTO;

@Repository
public class EmpDAOImpl implements EmpDAO {

	@Autowired
	SqlSession sqlSession;
	
	@Override
	public List<EmpDTO> selectAllEmp() {
		List<EmpDTO> resultList = null;
		
		resultList = sqlSession.selectList("mapper.emp.selectEmp");
		System.out.println("selectAllEmp: resultList: "+ resultList);
		
		return resultList;
	}

	@Override
	public EmpDTO selectEmpno(int empno) {
		EmpDTO empDTO = null;
		
		empDTO = sqlSession.selectOne("mapper.emp.selectEmpno", empno);
		System.out.println("selectEmpno: empDTO: "+ empDTO);
		
		return empDTO;
	}

}

