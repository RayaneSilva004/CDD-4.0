package Encapsulamento;

public class RioMar extends Pet {
	public static void main(String[] args) {
		Pet p1 = new Pet();
		p1.setNome("THAYSA");
		p1.getNome();
		
		p1.setSigno("Capricornio");
		p1.getSigno();
		
		p1.setRaca("Vira-Lata");
		p1.getRaca();
		
		p1.setVacinado(false);
		
		p1.setNomeDono("Rayane");
		p1.getNomeDono();
		
		p1.setPadrinho("Mariana");
		p1.getPadrinho();
		
		String nome= p1.getNome();
		System.out.println(nome);
		String signo= p1.getSigno();
		System.out.println(signo);
		String raca= p1.getRaca();
		System.out.println(raca);
		String padrinho= p1.getPadrinho();
		System.out.println(padrinho);
		
	}

}
