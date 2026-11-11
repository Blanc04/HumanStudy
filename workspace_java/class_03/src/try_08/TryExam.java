package try_08;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;

public class TryExam {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		FileInputStream fis = null;
		
		try {
			fis = new FileInputStream("c:\\test.txt");
			System.out.println("뭔가 함.");
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} finally {
			if(fis != null) {
				try {
					fis.close();
				} catch (IOException e) {
					e.printStackTrace();
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		}
		
		try(
			FileInputStream fis2 = new FileInputStream("c:\\test.txt");
		){
			System.out.println("뭔가 함.");
		} catch (Exception e) {
			e.printStackTrace();
		}
		
		throw new Exception("내가 만든 에러~");
		
	}

}
