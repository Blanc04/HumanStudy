package melon_02;

public class Song {
	// 필드
	// 제목, 가수, 앨범명, 순위, 좋아요 수, 앨범 아트
	String title;			// 제목
	String singer;			// 가수명
	String album;			// 앨범명
	private int rank;		// 순위
	long like;				// 좋아요 수
	String albumArtUrl;		// 앨범 아트 이미지 경로
	boolean useYN;			// 사용 여부
	
	
	// 생성자
	// 제목, 가수
	public Song(String title, String singer){
		this.title = title;
		this.singer = singer;
		
		this.album = title;
		this.rank = -1;
		this.like = 0;
		this.albumArtUrl = "기본이미지";
		this.useYN = true;
	}
	
	// 메소드
	// 재생, 다운로드, 좋아요 수정
	public void play() {
		System.out.println(this.title + "을 재생합니다.");
	}
	
	String download() {
		return this.title + "다운로드 주소";
	}
	
	/**
	 * 좋아요 숫자를 변경
	 * - 좋아요를 눌렀을 때 1 증가
	 * - 좋아요를 뗐을 때 1 감소
	 * 
	 * @param boolean
	 * 		true : 좋아요 눌렀을 때
	 * 		false : 좋아요 뺐을 때
	 * @return long 좋아요 수
	 */
	
	long updateLike(boolean action) {
		if(action) {
			this.like++;
		} else {
			this.like--;
		}
		
		return this.like;
	}
}
