package game_04;

public class Champ {
	
	void attack() {
		System.out.println("기본 공격 합니다.");
	}
	
	void move() {
		System.out.println("이동합니다.");
	}
	
	void skill(String key) {
		if(key.equals("R")) {
			System.out.println("궁극기를 사용합니다.");
		} else if (key.equals("F")) {
			System.out.println("점멸을 사용합니다.");
		}
	}
	
	void recall() {
		System.out.println("귀환합니다.");
	}
	
}
