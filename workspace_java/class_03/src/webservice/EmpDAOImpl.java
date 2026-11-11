package webservice;

import java.util.ArrayList;
import java.util.List;

public class EmpDAOImpl implements EmpDAO {

	@Override
	public List selectEmp() {
		
		List list = new ArrayList();
		list.add(1111);
		list.add(2222);
		list.add(3333);
		list.add(4444);
		list.add(5555);
		
		return list;
	}

}
