package var_02;

import java.util.HashMap;
import java.util.Map;

public class Map_09 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		HashMap<K,V> map = new HashMap();
		
		map.put("k1", "v1");
		map.put("k2", 2);
		map.put("k3", false);
		// 같은 key는 있으면 만들고 없으면 덮어쓰기
		map.put("k2", 3);
		
		System.out.println(map.get("k1"));
		
		String s = (String)map.get("k1");
		
		//없으면 null
		System.out.println(map.get("k100"));
		
		Map<String, Integer> map2 = new HashMap<String, Integer>();
//		Map<String, Integer> map2 = new HashMap();
		map2.put("k1", 1);
//		map2.put("k2", "1");
		int a = map2.get("k1");
		
		// 멜론 차트 1~3가지를 저장해서 관리할 거임
		// 한 곡당 가수명, 제목으로 저장
		// 모든 곡의 정보를 출력까지
		
		Map<String, String> song = new HashMap<String, String>();
		
		// final
		int x = 10;
		x = 20;
		
		final int y = 25;
		y = 200;
	}

}
