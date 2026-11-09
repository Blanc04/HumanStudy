package var_02;

public class While_07 {

	public static void main(String[] args) {

		// while 기본형
		int i = 3;
		while(i < 10) {
			System.out.println(i);
			i++;
		}
		
		i = 3;
		do {
			System.out.println(i);
			i++;
		}while(i < 10);
		
		System.out.println("-----------------");
		// 짝수 출력
		i = 0;
		while(i < 10) {
			i++;
			if(i % 2 != 0) {// 홀수만 검증
				continue;
			}
			System.out.println(i);
		}
		
	}

}
