package interface_06;

public class RemoconExam {
	public static void main(String[] args) {
		Tv tv = new Tv();
		tv.powerOn();
		
		RemoteControl rc = tv;
	}
}
