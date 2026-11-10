package override_03;

import melon_02.Song;

public class PhoneExam {

	public static void main(String[] args) {
		Phone phone1 = new Phone("010-6666-6666");
		Phone phone2 = new Phone("010-1166-1166");
		phone1.setPower(true);
		
		// phone1의 벨소리 바꾸기
		Song song = new Song("shit", "shit");
		phone1.ringtone(song);
		
		phone2.setPower(true);
		
		if(phone2.call(phone1.getNumber())) {
			phone1.ring();
			phone1.recieve();
		}
		
		SmartPhone s1 = new SmartPhone("010");
		SmartPhone s2 = new SmartPhone("011");
		
		if(s2.call(s1.getNumber())) {
			s1.ring();
			s1.recieve();
		}
		s1.message(s2.getNumber(), "자니?");
		s1.search("검색");
	}

}
