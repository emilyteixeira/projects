package sisbiblioteca;

import java.util.Date;

public class Funcionarios {
    private String nomeFunc;
    private String cargo;
    private Date dataContratacao;

    public Funcionarios(String nomeFunc, String cargo, Date dataContratacao) {
        this.nomeFunc = nomeFunc;
        this.cargo = cargo;
        this.dataContratacao = dataContratacao;
    }

    public String getNomeFunc() {
        return nomeFunc;
    }

    public String getCargo() {
        return cargo;
    }

    public Date getDataContratacao() {
        return dataContratacao;
    }

    public void setNomeFunc(String nomeFunc) {
        this.nomeFunc = nomeFunc;
    }

    public void setCargo(String cargo) {
        this.cargo = cargo;
    }

    public void setDataContratacao(Date dataContratacao) {
        this.dataContratacao = dataContratacao;
    }

    public void registrarEmprestimo(Emprestimos emprestimo) {
        System.out.println("Empréstimo registrado: " + emprestimo.getLivro().getTitulo());
    }

    public void realizarDevolucao(Emprestimos emprestimo) {
        System.out.println("Devolução realizada: " + emprestimo.getLivro().getTitulo());
    }
}
