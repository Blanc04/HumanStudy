package webservice;

import java.util.List;

public class EmpServiceImpl implements EmpService {

	@Override
	public List getEmp() {
		EmpDAO empDAO = new EmpDAOImpl();
		
		List list = empDAO.selectEmp();
		
		return list;
	}

}
