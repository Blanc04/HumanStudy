package string_09;

public class StringExam {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String s = "영일이삼사오육칠팔구삼사";
		
		char c = s.charAt(3);
		System.out.println(c);
		
		System.out.println(s.length());
		
		int i = s.indexOf("삼사");
		System.out.println(i);
		
		int i2 = s.lastIndexOf("삼사");
		System.out.println(i2);
		
		// indexOf를 사용하지 않고 구현하기
		String email = "d16udonne04@gmail.com";
		// [@]하나, [.]하나 이상 있으면 "이메일 맞음" 하나라도 ㅇ벗으면 "이메일 아님"
		for(i=0;i<email.length();i++) {
			email.charAt(i);
		}
		// indexOf("대상")의 결과가 -1이 아니면 찾음.
		if(email.indexOf("@") != -1 && email.indexOf(".") != -1) {
			System.out.println("이메일 맞음");
		} else {
			System.out.println("이메일 아님");
		}
		
		String s2 = s.replace("삼사", "34");
		System.out.println(s);
		System.out.println(s2);
		
		s2 = s.substring(5, 8);
		System.out.println(s2);
		
		s2 = s.substring(5);
		System.out.println(s2);
		
		String[] s3 = s.split("삼");
		for(String a : s3) {
			System.out.println(a);
		}
		
		double r = Math.random();
		System.out.println(r);
	}

}
