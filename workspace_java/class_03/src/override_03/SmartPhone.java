package override_03;

// extends 상속
// 단 하나의 클래스만 가능
// private 제외한 모든 요소를 상속 받을 수 있음
public class SmartPhone extends Phone {
	
	SmartPhone(String number) {
		super(number);
		
		System.out.println(this.number);
		ring();
//		System.out.println(this.power);
	}
	
	void openStore() {
		System.out.println("어플 목록이 나옵니다");
	}
	
	String search(String keyword) {
		System.out.println(keyword + "검색 중입니다...");
		
		return keyword + "검색 결과 페이지";
	}
	
	@Override
	void message(String number, String text){
		super.message("1", "text");
		System.out.println("1: " + text);
	}
}
