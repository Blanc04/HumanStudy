package interface_06;

public class Fan implements RemoteControl {

	@Override
	public void powerOn() {
		System.out.println("선풍기 켜기");
	}

	@Override
	public void powerOff() {
		System.out.println("선풍기 끄기");
	}

}
