package webservice;

public class ServletExam {

	public static void main(String[] args) {
		
		Servlet s = new EmpController();
		
		String html = s.doGet();
		
		System.out.println(html);
	}

}
