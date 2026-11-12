package com.example.demo.service;

import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.example.demo.dao.EmpDAO;
import com.example.demo.dto.EmpDTO;

@Service
public class EmpServiceImpl implements EmpService {

	@Autowired
	EmpDAO empDAO;
	
	@Override
	public List<EmpDTO> getEmpList() {
		List<EmpDTO> result = empDAO.selectAllEmp();
		
		return result;
	}

	@Override
	public EmpDTO getEmpno(int empno) {
		EmpDTO empDTO = empDAO.selectEmpno(empno);
		return empDTO;
	}

}
