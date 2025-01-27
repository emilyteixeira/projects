package sisbiblioteca;

import java.util.ArrayList;
import java.util.List;

public class Clientes {
    private String nomeCliente;
    private String telefone;
    private List<Emprestimos> historicoEmprestimos;

    public Clientes(String nomeCliente, String telefone) {
        this.nomeCliente = nomeCliente;
        this.telefone = telefone;
        this.historicoEmprestimos = new ArrayList<>();
    }

    public String getNomeCliente() {
        return nomeCliente;
    }

    public String getTelefone() {
        return telefone;
    }

    public List<Emprestimos> getHistoricoEmprestimos() {
        return historicoEmprestimos;
    }

    public void setNomeCliente(String nomeCliente) {
        this.nomeCliente = nomeCliente;
    }

    public void setTelefone(String telefone) {
        this.telefone = telefone;
    }

    public void setHistoricoEmprestimos(List<Emprestimos> historicoEmprestimos) {
        this.historicoEmprestimos = historicoEmprestimos;
    }

    public void realizarEmprestimo(Emprestimos emprestimo) {
        this.historicoEmprestimos.add(emprestimo);
    }

    public void devolverLivro(Emprestimos emprestimo) {
        this.historicoEmprestimos.remove(emprestimo);
    }
}
