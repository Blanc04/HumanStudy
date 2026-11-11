package webservice;

import java.util.List;

public class EmpController implements Servlet {

	@Override
	public String doGet() {
		
		EmpService empService = new EmpServiceImpl();
		List list = empService.getEmp();
		
//		String html = "<div>ename : SCOTT</div>";
		Jsp jsp = new Jsp();
		String html = jsp.view(list);
		
		return html;
	}

	@Override
	public String doPost() {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public String doPut() {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public String deDelete() {
		// TODO Auto-generated method stub
		return null;
	}

}
