package var_02;

public class Var_01 {

	/**
	 * 
	 * @param args
	 */
	public static void main(String[] args) {
		
		// 한줄 주석
		/*
		  여러줄 주석
		  범위 주석
		 */
		
		
		
		int a;
		a = 10;
		
		int b = 20;
		
		System.out.print(a);
		System.out.println(b);
		
		System.out.println(a +/*", "+*/ b);
		
//		b = 3.5;
//		b = "a";
		
		char c1 = 'A';
		System.out.println("c1: "+ c1);
		
		char c2 = 65;
		System.out.println("c2: "+ c2);
		
		char c3 = 65 + 3;
		System.out.println("c3: "+ c3);
		
		
		long l1 = 2200000000L;
		long l2 = 30;
		
		String s1 = "최민수";
		System.out.println("s1: "+ s1);
		
		String s2 = "최\"민\"수";
		System.out.println("s2: "+ s2);
		
		String s3 = "최\n민수";
		System.out.println("s3: "+ s3);
		
		System.out.println("글씨" + 3);
		System.out.println("글씨" + 3 + 2);
		System.out.println("글씨" + (3 + 2));
		System.out.println("글씨" + 3 * 2);
		
		System.out.println(2 + 3 + "글씨");
		
		
		float f1 = 3.14f;
		double d1 = 3.14;
		
		boolean stop = true;
		boolean start = false;
		
		System.out.println("stop: "+ stop);
		
		
		// 문제1
		// 내 나이를 저장하고 출력하시오
		int age = 20;
		System.out.println(age);
		
		// 문제2
		// 운전면허가 있다 없다를 저장하고 출력하시오
		boolean yn = true;
		
		// 문제3
		// 1평은 3.3제곱미터입니다
		// 5평이 몇 제곱미터인지 계산해서 저장하고 출력하시오
		double py = 3.3;
		double result3 = 5 * py;
		
		// 문제4
		// 두 변수 x, y에 각각 숫자를 넣고
		// 출력 결과 : "3 > 4의 결과는 false 입니다"
		int x = 3;
		int y = 4;
		boolean result4 = x > y;
		System.out.println(x +" > "+ y +"의 결과는"+ result4 +"입니다");
		
		
		// 문제5
		// 회식비 78500원
		// 참석인원 3명
		// 인 당 얼마?
		// 5-1 : 원 단위 까지 출력
		// 5-2 : 만원 단위 까지만 출력
		// 5-3 : 나머지는 주최자가 낸다. 그럼 주최자가 낼 돈은?
		int total = 78500;
		int members = 3;
		int member = total / members; //26,166.66666666
		System.out.println("5-1 : "+ member);
		
		int money1 = (member / 1000) * 1000;
		System.out.println("5-2 : "+ money1);
		
		int money2 = total - (money1 * (members - 1));
		System.out.println("5-3 : "+ money2);
		
		
		// 문제6
		String left = "국밥";
		String right = "돈까스";
		
		String temp = left;
		left = right;
		right = temp;
		
		System.out.println("left : "+ left); // 돈까스
		System.out.println("right : "+ right); // 국밥
		
		
		int i1 = 10;
		long i2 = (long)i1;
		i2 = i1; // 생략 가능
		
		i1 = (int)i2;
		
		i2 = 2200000000L;
		i1 = (int)i2;
		System.out.println("i1:"+ i1);
		
		float ff1 = 1.23f;
		double ff2 = ff1;
		ff1 = (float)ff2;
		
		int i3 = 2100000000;
		int i4 = i3 * 3;
		System.out.println(i4);
		
		int i5 = 10;
		double i6 = i5;
		System.out.println("i6:"+ i6);
		
		int i7 = 33;
		int i8 = 10;
		double i9 = i7 / i8;
		System.out.println("i9 : "+ i9);
		
		double d2 = 10 / 4;
		System.out.println("d2: "+ d2);
		
		double d3 = 10.0 / 4;
		System.out.println("d3: "+ d3);
		
		double d4 = (double)10 / 4;
		
		String s4 = "123";
//		int ii1 = (int)s4; //  지원하지 않음
		
		int ii1 = Integer.parseInt(s4);
		
		int ii2 = 0xFF;
		System.out.println(ii2);
		
	}

}









