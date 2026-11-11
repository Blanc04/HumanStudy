package interface_06;

public class Tv 
extends Display
implements RemoteControl, OTT {

	@Override
	public void powerOn() {
		System.out.println("TV 켜기");
	}

	@Override
	public void powerOff() {
		System.out.println("TV 끄기");
	}

	@Override
	public void netflix() {
		System.out.println("넷플릭스 시청하기");
	}
	
}
