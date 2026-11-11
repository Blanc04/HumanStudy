package abstract_05;

import java.util.ArrayList;
import java.util.List;

// abstract 클래스
// 부모 전용 클래스이기에 new 불가
// abstract 메소드를 가질 수 있음
public abstract class Student {
	List skills = new ArrayList();
	
	Student() {
		System.out.println("Student 생성자 실행");
	}
	
	void eat() {
		{
			int a = 0;
		}
		System.out.println("우걱 우걱 밥 먹는다.");
	}
	
	// 추상 메소드
	// 실행 블럭이 있으면 안 됨
	// 나는 구현하지 않는다
	// 자식에게 구현을 떠 넘김
//	abstract void study() { }
	abstract void study();
}
