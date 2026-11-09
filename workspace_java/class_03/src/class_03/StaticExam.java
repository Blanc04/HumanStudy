package class_03;

public class StaticExam {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
//		Static_03 s1 = new Static_03();
//		Static_03 s2 = new Static_03();
//		
//		s1.PI = 3.1;
//		System.out.println(s1.getPI());
//		System.out.println(s2.getPI());
		
		System.out.println(Static_03.PI);
		System.out.println(Static_03.getPI());
		
		System.out.println(Math.PI);
		System.out.println(Math.random());
		
//		StaticExam se = new StaticExam();
//		se.test();
		test();
	}
	
	void test() {
		System.out.println("테스트");
	}

}
