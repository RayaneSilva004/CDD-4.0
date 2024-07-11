package Turmad;

public class OperadoresExemplo6 {

	public static void main(String[] args) {
		String nome = "Tatá";
		int idade = 10;
		double nota = 4.5;
		
		System.out.println(nome);
		System.out.println(idade);
		System.out.println(nota);
		// OU
		System.out.print(nome+" ");
		System.out.print(idade+" ");
		System.out.print(nota+" ");
		// OU
		System.out.println(nome+" "+idade+" "+nota);
		// OU
		System.out.printf("Seu nome é %s, sua idade é  %d e sua nota foi %.2f", nome,idade,nota);
	}

}
