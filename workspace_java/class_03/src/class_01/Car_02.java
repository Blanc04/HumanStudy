package class_01;

public class Car_02 {
	
	// 필드(공용, 전역 변수)
	// 변수 선언만 가능
	// 선언 하면서 동시에 초기화 가능
	String company = "1950년대 미국산 차";
//	String model = "최초의 차";
	String model;
	int maxSpeed = 125;
	int year;
	
	// 초기화 하지 않은 경우
	// 0, false, null로 초기화 됨
	int speed;
	// 필드 영역에서는 실행(행동) 불가
//	speed = 10; // speed의 값을 10으로 바꾸는 행동
	
	boolean power;
	
	//////////
	// 메소드
	
	// 선언
	// 리턴타입 메소드명(전달인자(들)) {}
	void powerOn() {
		power = true;
	}
	void powerOff() {
		power = false;
	}
	
	// 속도를 적어서 주면
	// speed에 반영
	// 단, 최고 속도 이상을 받으면 최고 속도로 보정
	void setSpeed(int s) {
		System.out.println(s);
		
		if (s >= maxSpeed) {
			System.out.println("야!!!!!!!!!!!");
			s = maxSpeed;
			System.out.println(s);
		}
	}
	
	/**
	 * javadoc 주석
	 * 속도, 즉 필드의 speed를 돌려줌
	 * 
	 * @param 없음
	 * @return int
	 * @author d16udonne04@gmail.com
	 */
	int getSpeed() {
		return speed;
	}
	
	int getSpeed(int s) {
		System.out.println();
		System.out.println(s);
		return speed;
	}
	
	// overloading 오버로딩
	// 전달인자 타입의 개수, 순서
	// 메소드 명을 동일하게 할 수 있는 것
	
	// 전달인자 자료형이 정확히 동일한 것 우선순위 높음
	// 그 다음에 자동 형변환으로 들어갈 수 있는 것
	int plus(int x, int y) {
		System.out.println("int plus(int x, int y)");
		return x + y;
	}
	
	int plus(int x) {
		return x + x;
	}
	
	int minus(int x, int y) {
		return x - y;
	}
	
	double plus(double x, double y) {
		System.out.println("int plus(int x, int y)");
		return x + y;
	}
	
	//////////
	// 생성자
	// new 할 때 무조건 실행되는 메소드
	
	// 생성자를 선언하지 않으면
	// 무조건 기본 생성자가 자동 완성됨
	Car_02(){
		System.out.println("생성자 실행");
	}
	
	Car_02(String m, int y, boolean p){
		model = m;
		year = y;
		power = p;
	}
	
	Car_02(String m){
		this(m, 2026, false);
		
//		model = m;
//		year = 2026;
//		power = false;
		
		System.out.println();
	}
	
	void setYear(int year) {
		this.year = year;
	}
	
	
	
}
