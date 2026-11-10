package melon_02;

public class MelonExam {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Melon melon = new Melon();
		
		Song s1 = new Song("With", "SSSSSSSS");
		boolean result = melon.addSong(s1);
		if(result) {
			System.out.println("s1이 정상적으로 추가되었습니다.");
		} else {
			System.out.println("추가되지 않았습니다. 관리자 콜!");
		}
		
		Song s2 = new Song("꿈 꾸던 어른이 되었나요?", "머무르");
		melon.addSong(s2);
		
		melon.showList(10);
	}

}
