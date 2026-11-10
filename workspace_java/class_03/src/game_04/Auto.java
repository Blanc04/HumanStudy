package game_04;

public class Auto {
	
	void run(Champ champ) {
		champ.attack();
		champ.move();
		champ.skill("F");
		champ.skill("R");
		champ.recall();
		
		if(champ instanceof VI) {
			VI vi = (VI)champ;
			vi.징크스랑놀기();
		}
	}
}
