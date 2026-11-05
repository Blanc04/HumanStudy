package var_02;

public class Op_02 {

	public static void main(String[] args) {

		int x = 10;
		
		x++;
		System.out.println("x: " + x);
		
		++x;
		System.out.println("x: " + x);
		
		x = 10;
		int y = ++x;
		System.out.println("y: " + y);
		
		x = 10;
		y = x++;
		System.out.println("y: " + y);
		System.out.println("x: " + x);
		
		x = 10;
		y = x++ + ++x;
		System.out.println("y: " + y);
		
		x = 10;
		y = x++ * --x / ++x - x--;
		
		// 소수점은 근사치로 저장됨
		// 그나마 같은 타입이면 수월함
		
		String s1 = "s1";
		String s2 = "s1";
		// 문자열 비교는 무조건 equals()로 함
		System.out.println(s1.equals(s2));
		
		// 삼항 연산자
		int score = 75;
		String grade = (score > 90) ? "A학점" : "B학점";
		System.out.println(grade);
		
		String upgrade = (score >= 90) ? "A" : (score >= 80) ? "B" : "C";
		System.out.println(upgrade);
	}
}
