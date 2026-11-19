package com.example.demo.controller;

import java.util.List;
import java.util.Map;

import org.apache.ibatis.session.SqlSession;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

import com.example.demo.dto.EmpDTO;
import com.example.demo.service.EmpService;

import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpSession;

@Controller
public class EmpController {

	private static final Logger logger = LoggerFactory.getLogger(EmpController.class);
	
	@Autowired
	EmpService empService;
	
	@Autowired
	SqlSession sqlSession;
	
	@ResponseBody
	@RequestMapping(value="/", method=RequestMethod.GET)
	public String hello() {
		EmpDTO dto = new EmpDTO();
		System.out.println(dto);
		return "hello";
	}
	
	// 사원 목록 조회
	// 리스트라는 주소를 매핑으로 추가해 전달인자를 model로 받고 List DB 안에 있는 변수를 직원 서비스 안의 직원 리스트 불러오기로 지정
	// model이라는 전달인자에 list라는 속성을 추가하고 그 결과를 반환
	@GetMapping("/list")
	public String list(Model model) {
		System.out.println("/list 실행");
		
//		List<EmpDTO> list = empService.getEmpList();
		List<EmpDTO> list = sqlSession.selectList("mapper.emp.selectEmp");
		System.out.println("/list: list: "+ list);
		
		model.addAttribute("list", list);
		return "result";
	}
//	@GetMapping("/list")
//	public String list(Model model) {
//		List<EmpDTO> list = empService.getEmpList();
//		model.addAttribute("list", list);
//		return "result";
//	}


	@RequestMapping("/getEmpno")
	public String getEmpno(Model model,
		@RequestParam(value="empno", required=false)
		int empno
	) {
		System.out.println("/getEmpno 실행");
		
		System.out.println("empno: "+ empno);
		EmpDTO empDTO = empService.getEmpno(empno);

		model.addAttribute("empDTO", empDTO);
		
		return "result";
	}

}





