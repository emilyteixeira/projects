package sisbiblioteca;

import java.util.List;

public class Categorias implements List<Categorias> {
    private String nomeCategoria;

    public Categorias(String nomeCategoria) {
        this.nomeCategoria = nomeCategoria;
    }

    public String getNomeCategoria() {
        return nomeCategoria;
    }

    public void setNomeCategoria(String nomeCategoria) {
        this.nomeCategoria = nomeCategoria;
    }  

    public void adicionarLivro(Livros livro) {
        System.out.println("Livro adicionado: " + livro.getTitulo());
    }

    public void removerLivro(Livros livro) {
        System.out.println("Livro removido: " + livro.getTitulo());
    }
}
