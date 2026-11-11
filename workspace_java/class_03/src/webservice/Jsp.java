package webservice;

import java.util.List;

public class Jsp {
	
	String view(List<Integer> list) {
		StringBuffer sb = new StringBuffer();
		
		for( int empno : list ) {
			sb.append("<div>)" + empno + "</div>\n");
		}
		
		String result = sb.toString();
		return result;
	}
}
