package game_04;

public class LOL_Exam {

	public static void main(String[] args) {
		
		VI 롤노잼 = new VI();
		롤노잼.move();
		롤노잼.skill("R");

		
		Jax jax = new Jax();
		jax.move();
		
		Champ champ1 = 롤노잼;
		Champ champ2 = jax;
		
		champ1.move();
		champ2.move();
		
		Auto auto = new Auto();
		auto.run(롤노잼);
		auto.run(jax);
		
//		VI vi2 = (VI)champ1;
//		vi2.징크스랑놀기();
	}

}
