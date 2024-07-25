package ÉoFim;

public class TriAtleta implements Corredor, Nadador, Ciclista {
	private boolean descansando;
    private boolean aquecendo;
    private boolean correndo;
    private boolean nadando;
    private boolean pedalando;
    
    public TriAtleta() {
        this.descansando = false;
        this.aquecendo = false;
        this.correndo = false;
        this.nadando = false;
        this.pedalando = false;
    }

    public boolean descansar() {
        if (descansando) {
            System.out.println("O atleta já está descansando");
            return false;
        } else {
            System.out.println("O atleta entrou em descanso");
            descansando = true;
            return true;
        }
    }

    public boolean sairDescanso() {
        if (descansando) {
            System.out.println("Atleta saiu do descanso");
            descansando = false;
            return true;
        } else {
            System.out.println("Atleta não está descansando");
            return false;
        }
    }
    
    public boolean aquecer() {
    	if(aquecendo) {
    		System.out.println("Atleta já aqueceu");
    		return false;
    	}else {
            System.out.println("O atleta está aquecendo");
            aquecendo = true;
            return true;
    }
    }
    
    public boolean correr(){
    	if (!aquecendo) {
            System.out.println("TriAtleta não pode correr, ele não aqueceu ainda");
            return false;
        } else if (descansando) {
            System.out.println("TriAtleta está descansando, ele não pode correr");
            return false;
        } else if (nadando) {
            System.out.println("TriAtleta não pode correr, pois está nadando");
            return false;
        } else if (pedalando) {
            System.out.println("TriAtleta não pode correr, pois está pedalando");
            return false;
        } else if (correndo) {
            System.out.println("TriAtleta já está correndo");
            return false;
        } else {
            System.out.println("TriAtleta começou a correr");
            correndo = true;
            return true;
        }
    }
    
    public boolean pararCorrer() {
    	if(!correndo) {
    		System.out.println("TriAtleta não está corrrendo");
    		return false;
    	}else {
    		System.out.println("TriAtleta parou de correr");
    		correndo = false;
    		return true;
    	}
    }
    public boolean nadar() {
        if (!aquecendo) {
            System.out.println("TriAtleta não pode nadar, ele não aqueceu ainda");
            return false;
        } else if (descansando) {
            System.out.println("TriAtleta está descansando, ele não pode nadar");
            return false;
        } else if (correndo) {
            System.out.println("TriAtleta não pode nadar, pois está correndo");
            return false;
        } else if (pedalando) {
            System.out.println("TriAtleta não pode nadar, pois está pedalando");
            return false;
        } else if (nadando) {
            System.out.println("TriAtleta já está nadando");
            return false;
        } else {
            System.out.println("TriAtleta começou a nadar");
            nadando = true;
            return true;
        }
    }

    public boolean pararNadar() {
        if (!nadando) {
            System.out.println("TriAtleta não está nadando");
            return false;
        } else {
            System.out.println("TriAtleta parou de nadar");
            nadando = false;
            return true;
        }
    }
    public boolean pedalar() {
        if (!aquecendo) {
            System.out.println("TriAtleta não pode pedalar, ele não aqueceu ainda");
            return false;
        } else if (descansando) {
            System.out.println("TriAtleta está descansando, ele não pode pedalar");
            return false;
        } else if (nadando) {
            System.out.println("TriAtleta não pode pedalar, pois está nadando");
            return false;
        } else if (correndo) {
            System.out.println("TriAtleta não pode pedalar, pois está correndo");
            return false;
        } else if (pedalando) {
            System.out.println("TriAtleta já está pedalando");
            return false;
        } else {
            System.out.println("TriAtleta começou a pedalar");
            pedalando = true;
            return true;
        }
    }

    public boolean pararPedalar() {
        if (!pedalando) {
            System.out.println("TriAtleta não está pedalando");
            return false;
        } else {
            System.out.println("TriAtleta parou de pedalar");
            pedalando = false;
            return true;
        }
    }
}
