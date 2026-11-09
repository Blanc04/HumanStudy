package var_02;

import java.util.ArrayList;
import java.util.List;

public class List_08 {

	public static void main(String[] args) {
		// 선언
		ArrayList list = new ArrayList();
		
		// 추가
		list.add(1);
		list.add("글씨");
		list.add(true);
		
		// 꺼내기
		System.out.println(list.get(0));
		System.out.println(list.get(1));
		System.out.println(list.get(2));
		
		// 크기
		System.out.println(list.size());
		
		// 반복문으로 list의 모든 내용을 출력	
		for(int i=0; i<list.size(); i++) {
			System.out.println(list.get(i));
		}
		
		for(Object obj : list) {
			System.out.println(obj);
		}
		
		int a = (int)list.get(0);
		
		ArrayList<String> list2 = new ArrayList<String>();
		list2.add("문자");
//		list2.add(1);
		
		String b = (String)list.get(1);
		String c = list2.get(0);
		
		List list3 = new ArrayList();
	}

}
