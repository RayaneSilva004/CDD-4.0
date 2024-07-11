package Turmad;

public class OperadorExemplo7 {

	public static void main(String[] args) {
		int a = 3;
		System.out.println(a %2 == 0 ?++a: a++);
		
		int b = 4;
		System.out.println(b%2== 0?"é par" : "é ímpar");
	}

}
