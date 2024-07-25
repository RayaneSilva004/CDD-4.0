package Encapsulamento;

public class Pet {
	private String nome;
	private String signo;
	private String raca;
	private boolean vacinado;
	private String nomeDono;
	private String padrinho;
	
	public String getNome() {
		return nome;
	}
	public void setNome(String nome) {
		this.nome = nome;
	}
	public String getSigno() {
		return signo;
	}
	public void setSigno(String signo) {
		this.signo = signo;
	}
	public String getRaca() {
		return raca;
	}
	public void setRaca(String raca) {
		this.raca = raca;
	}
	public boolean isVacinado() {
		return vacinado;
	}
	public void setVacinado(boolean vacinado) {
		this.vacinado = vacinado;
	}
	public String getNomeDono() {
		return nomeDono;
	}
	public void setNomeDono(String nomeDono) {
		this.nomeDono = nomeDono;
	}
	public String getPadrinho() {
		return padrinho;
	}
	public void setPadrinho(String padrinho) {
		this.padrinho = padrinho;
	}
	
}
