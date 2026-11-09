package var_02;

public class Op_02 {

	public static void main(String[] args) {

		int x = 10;

		x++;
		System.out.println("x:"+ x); // 11
		
		++x;
		System.out.println("x:"+ x); // 12
		
		x = 10;
		int y = ++x;
		System.out.println("y:"+ y); // 11
		
		x = 10;
		y = x++;
		System.out.println("y:"+ y); // 10
		System.out.println("x:"+ x);
		
		x = 10;
		y = x++ + ++x;
		System.out.println(y);
		
		x = 10;
		y = x++ * --x / ++x - x--;
		// x = 10
		//  10 * 10 / 11 - 11;
		System.out.println("x:"+ x +", y:"+ y);

		x = 10;
		y = x++ + (--x / ++x) - x--;
		// x = 10
		// 10 + (9 / 10) - 11;
		System.out.println("x:"+ x +", y:"+ y); //  -1
		
		x = 0;
		System.out.println(x++);
		System.out.println(x++);
		System.out.println(x++);
		
		double a = 7.3;
		int b = 0;
		System.out.println(a / b);
		
		System.out.println(10 % 3); // 1
		
		int c = 149;
		// 기습 문제
		// 10의 자리만 출력하시오
		// 249 / 10 == 14
		// 24 % 10 == 4
		
		float d = 0.1f;
		double e = 0.1;
		boolean f = d == e;
		System.out.println( f );
		// 소수점은 근사치로 저장된다
		// 그나마 같은 타입이면 수월하다
		
		String s1 = "s1";
		String s2 = "s1";
		// 문자열 비교는 무조건 equals()로 한다
		System.out.println( s1.equals(s2) );
		System.out.println( "abcd".equals(s2) );		
		
		// 문제2
		// 빼빼로데이에 RTX5060를 15%할인한다
		// 원래가격은 120만원. 
		// 그렇다면 가격은?
		int rtx5060 = 1200000;
		double sale = 0.15;
		double price = rtx5060 - rtx5060 * sale;
		price = rtx5060 * (1 - sale);
		System.out.println(price);
		
		double v1 = 1000;
		double v2 = 794.0;
		// 문제3
		// v1 / v2의 결과를 소수점 3번째까지 출력하시오 // 1.25944584
		double v3 = v1 / v2;
		double v4 = ((int)(v3 * 1000)) / 1000;
		
		// 삼항 연산자
		int score = 85;
		String grade = (score >= 90) ? "A학점" : "B학점";
		System.out.println(grade);
		
		// 문제4
		// 90이상 : A
		// 80이상 : B
		// 그 외 : C
		String upgrade = (score >= 90) ? "A학점" : (score < 90 && score >= 80) ? "B학점" : "C학점";
	}
}
