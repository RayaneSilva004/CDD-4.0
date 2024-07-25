package Heranca;

public class Faculdade {
	public static void main(String[] args) {
		Aluno a1 = new Aluno("João",22);
		Professor p1 = new Professor("Tauã", 60);
		p1.salario=1200.00;
		System.out.println(p1.salario);
	}

}
