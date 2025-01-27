package sisbiblioteca;

import java.util.List;

public class Livros {

    private String titulo;
    private String autor;
    private String isbn;
    private boolean statusDisponibilidade;
    private List<Categorias> categoria;

    public Livros(String titulo, String autor, String isbn, boolean statusDisponibilidade, List<Categorias> categoria) {
        this.titulo = titulo;
        this.autor = autor;
        this.isbn = isbn;
        this.statusDisponibilidade = statusDisponibilidade;
        this.categoria = categoria;
    }

    public String getTitulo() {
        return titulo;
    }

    public String getAutor() {
        return autor;
    }

    public String getIsbn() {
        return isbn;
    }

    public boolean getStatusDisponibilidade() {
        return statusDisponibilidade;
    }

    public List<Categorias> getCategoria() {
        return categoria;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public void setAutor(String autor) {
        this.autor = autor;
    }

    public void setIsbn(String isbn) {
        this.isbn = isbn;
    }

    public void setStatusDisponibilidade(boolean statusDisponibilidade) {
        this.statusDisponibilidade = statusDisponibilidade;
    }

    public void setCategoria(List<Categorias> categoria) {
        this.categoria = categoria;
    }

    public void marcarComoEmprestado() {
        System.out.println("Livro emprestado: " + this.titulo);
    }

    public void marcarComoDisponivel() {
        System.out.println("Livro disponível: " + this.titulo);
    }
}
