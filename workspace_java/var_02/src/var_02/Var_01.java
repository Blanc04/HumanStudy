package var_02;

public class Var_01 {

	public static void main(String[] args) {
		
		// 한 줄 주석
		/*
		  여러 줄 주석
		  범위 주석
		 */
		
		int a;
		a = 10;
		
		// 정수만 가능
		int b = 20;
		
		// syso 입력 후 Ctrl+Space
		System.out.println(a);
		System.out.println(b);
		
		System.out.println(a+", "+b);
		
//		b = 3.5;
//		b = "a";
		
		char c1 = 'A';
		System.out.println("c1: " + c1);
		
		char c2 = 65;
		System.out.println("c2: " + c2);
		
		char c3 = 65 + 3;
		System.out.println("c3: " + c3);
		
		// 명시적 long type
		long l1 = 2200000000L;
		long l2 = 30;
		
		String s1 = "나는 내 이름이 싫다.";
		System.out.println("s1: " + s1);
		
		String s2 = "개놈\"개놈\"개놈";
		System.out.println("s2: " + s2);
		
		String s3 = "개놈\n개놈\n개놈";
		System.out.println("s3: " + s3);
		
		System.out.println("글씨"+3+2);
		System.out.println("글씨"+(3+2));
		System.out.println("글씨"+3*2);
		System.out.println(2+3+"글씨");
		
		float f1 = 3.14f;
		double d1 = 3.14;
		
		boolean stop = true;
		boolean start = false;
		System.out.println("stop: " + stop);
		System.out.println("start: " + start);
		
		// 문제 1
		// 내 나이를 저장하고 출력
		int age = 23;
		System.out.println("문제 1: "+ age);
		
		// 문제 2
		// 운전면허가 있다 없다를 저장하고 출력
		String Drive = "있음";
		String noDrive = "없음";
		System.out.println("문제 2: "+ noDrive);
		
		// 문제 3
		// 1평은 3.3제곱미터
		// 5명은 몇 제곱미터인지 계산해서 저장하고 출력
		double q3num1 = 3.3;
		double q3result = q3num1 * 5;
		System.out.println("문제 3: " + q3num1 * 5 + "제곱미터");
		System.out.println("문제 3: " + q3result + "제곱미터");
		
        // 문제4
        // 두 변수 x, y에 각각 숫자를 넣고
        // 출력 결과 : "3 > 4의 결과는 false 입니다"
		int x = 6;
		int y = 8;
		boolean q4result = x>y;
		System.out.println("문제 4: "+ x + ">" + y+"의 결과는 "+q4result+"입니다");
        
        // 문제5
        // 회식비 78500원
        // 참석인원 3명
        // 인 당 얼마?
		int q5price = 78500;
		int q5people = 3;
        // 5-1 : 원 단위 까지 출력
		System.out.println("문제 5-1: "+q5price/q5people+"원");
		
        // 5-2 : 만원 단위 까지만 출력
		int q5money = q5price/q5people;
		System.out.println("문제 5-2: "+q5money/10000*10000+"원");
		
        // 5-3 : 나머지는 주최자가 낸다. 그럼 주최자가 낼 돈은?
//		int q5andMoney = q5money/1000*1000;
		int q5otherMoney = q5money/10000*10000;
		int otherPeople = q5people-1;
//		System.out.println("문제 5-3: "+(q5price-q5andMoney*otherPeople)+"원");
		System.out.println("문제 5-3: "+(q5price-q5otherMoney*otherPeople)+"원");
        
        // 문제6
        String left = "국밥";
        String right = "돈까스";
        
        String oldLeft = left; 
        left = right;
        right = oldLeft;
        
        System.out.println("left : "+ left); // 돈까스
        System.out.println("right : "+ right); // 국밥
        
        int i1 = 10;
        long i2 = i1;
        i2 = i1; //생략 가능
        
        i1 = (int)i2;
        
        i2 = 2200000000L;
        
        i1 = (int)i2;
        
        System.out.println("i1: "+i1);
        
        float ff1 = 1.23f;
        double ff2 = ff1;
        ff1 = (float)ff2;
        
        int i3 = 2100000000;
        int i4 = i3 * 3;
        System.out.println(i4);
        
        int i5 = 10;
        double i6 = i5;
        
        int i7 = 33;
        int i8 = 10;
        double i9 = i7/i8;
        System.out.println("i9: " + i9);
        
        double d2 = 10 / 4;
        System.out.println("d2: " + d2);
        
        double d3 = 10.0 / 4;
        System.out.println("d3: " + d3);
        
        double d4 = (double)10 / 4;
        
        String s4 = "123";
//        int ii1 = (int)s4; // 지원하지 않음
        
        int ii1 = Integer.parseInt(s4);
        
        int ii2 = 0xF;
        System.out.println(ii2);
	}
	
}
