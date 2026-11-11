package interface_06;

public interface RemoteControl {
	public static final int 보증기간 = 3;
	// 인터페이스
	// 모든 필드는 public static final (상수)
	// 그래서 생략 가능
	String company = "휴먼전자";
	
	public abstract void powerOn();
	// 모든 메소드는 public abstract(추상)
	// 그래서 생략 가능
	void powerOff();
	
	default void mic(String text) {
		System.out.println(text + "를 들었습니다.");
	}
}
