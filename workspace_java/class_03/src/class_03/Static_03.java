package class_03;

public class Static_03 {
	// static
	// 생성하지 않고 바로 사용할 수 있는 것
	// 모든 클래스가 공통으로 가지고 있음
	static double PI = 3.14;
	String name;
	
	// 상수 : static final
	static final String 주민번호 = "123456-1";
	
	static final String OK = "E00";
	static final String FILTER_ERROR = "E01";
	static final String COOLER_ERROR = "E02";
	
	static double getPI() {
//		name = "abc";
//		return this.PI;
		return PI;
	}
	
	void setPI(double p) {
		PI = p;
	}
	
	Static_03(){
		PI = 3.14;
	}
}
