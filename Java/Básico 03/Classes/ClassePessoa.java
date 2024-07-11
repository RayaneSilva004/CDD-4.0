package JavaPoo;

public class ClassePessoa {
    String nome;
    boolean comendo = false;
    boolean dormindo = false;
    boolean andando = false;
    String acao = ""; 

    public ClassePessoa(String nome) {
        this.nome = nome;
    }

    public void setAcao(String acao) {
        this.acao = acao;
    }

    public void comer() {
        if (acao.isEmpty()) {
            if (dormindo) {
                System.out.printf("%s não pode comer enquanto está dormindo \n", nome);
            } else if (andando) {
                System.out.printf("%s não pode comer enquanto está andando \n", nome);
            } else if (comendo) {
                System.out.printf("%s já está comendo \n", nome);
            } 
            else {
                System.out.printf("%s está comendo \n", nome);
                comendo = true;
                acao = "comendo";
            }
        }
    }

    public void pararDeComer() {
        if (acao.equals("comendo")) {
            System.out.printf("%s parou de comer \n", nome);
            comendo = false;
            acao = "";
        } else {
            System.out.printf("%s não está comendo \n", nome);
        }
    }

    public void dormir() {
        if (acao.isEmpty()) {
            if (comendo) {
                System.out.printf("%s não pode dormir enquanto está comendo \n", nome);
            } else if (andando) {
                System.out.printf("%s não pode dormir enquanto está andando \n", nome);
            } else if (dormindo) {
                System.out.printf("%s já está dormindo \n", nome);
            } else {
                System.out.printf("%s está dormindo \n", nome);
                dormindo = true;
                acao = "dormindo";
            }
        } else {
            System.out.printf("%s não pode dormir, pois está %s \n", nome, acao);
        }
    }

    public void pararDeDormir() {
        if (acao.equals("dormindo")) {
            System.out.printf("%s acordou \n", nome);
            dormindo = false;
            acao = "";
        } else {
            System.out.printf("%s não está dormindo \n", nome);
        }
    }

    public void andar() {
        if (acao.isEmpty()) {
            if (comendo) {
                System.out.printf("%s não pode andar enquanto está comendo \n", nome);
            } else if (dormindo) {
                System.out.printf("%s não pode andar enquanto está dormindo \n", nome);
            } else if (andando) {
                System.out.printf("%s já está andando \n", nome);
            } else {
                System.out.printf("%s está andando \n", nome);
                andando = true;
                acao = "andando";
            }
        } else {
            System.out.printf("%s não pode andar, pois está %s \n", nome, acao);
        }
    }

    public void pararDeAndar() {
        if (acao.equals("andando")) {
            System.out.printf("%s parou de andar \n", nome);
            andando = false;
            acao = "";
        } else {
            System.out.printf("%s não está andando \n", nome);
        }
    }

}
