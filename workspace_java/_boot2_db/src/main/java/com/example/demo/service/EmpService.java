package com.example.demo.service;

import java.util.List;
import java.util.Map;

import com.example.demo.dto.EmpDTO;

public interface EmpService {

	List<EmpDTO> getEmpList();
	EmpDTO getEmpno(int empno);
}
