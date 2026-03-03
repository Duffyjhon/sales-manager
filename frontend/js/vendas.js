// =======================
// PROTEÇÃO
// =======================
if (!localStorage.getItem("token")) {
    window.location.href = "login.html";
}

let todasVendas = [];

// =======================
// FUNÇÕES DE FORMATAÇÃO (NOVO)
// =======================
function formatBRL(value) {
    const n = Number(value) || 0;
    return n.toLocaleString("pt-BR", {
        style: "currency",
        currency: "BRL"
    });
}

function formatDateBR(dateString) {
    if (!dateString) return "";

    const d = new Date(dateString);
    if (isNaN(d.getTime())) return "";

    return d.toLocaleDateString("pt-BR");
}

// =======================
// TEMA ESCURO
// =======================
document.addEventListener("DOMContentLoaded", () => {
    const toggle = document.getElementById("tema-toggle");

    if (localStorage.getItem("tema") === "dark") {
        document.body.classList.add("dark");
        toggle.checked = true;
    }

    toggle.addEventListener("change", e => {
        if (e.target.checked) {
            document.body.classList.add("dark");
            localStorage.setItem("tema", "dark");
        } else {
            document.body.classList.remove("dark");
            localStorage.setItem("tema", "light");
        }
    });

    carregarVendas();

    // 🔥 Agora sim! Busca funcionando
    document.getElementById("busca").addEventListener("input", atualizarLista);
    document.getElementById("filtro-produto").addEventListener("change", atualizarLista);
});

// =======================
// REGISTRAR VENDA
// =======================
document.getElementById("venda-form").addEventListener("submit", async (e) => {
  e.preventDefault();

  const cliente = document.getElementById("cliente").value.trim();
  const produto = document.getElementById("produto").value.trim();
  const valor = parseFloat(document.getElementById("valor").value);
  const data_venda = document.getElementById("data_venda")?.value; // "YYYY-MM-DD" ou ""

  const payload = { cliente, produto, valor };

  if (data_venda) {
    payload.data_venda = data_venda;
  }

  const result = await apiPost("/vendas/", payload);

  if (!result.ok) {
    alert((result.data && result.data.error) || `Erro ao registrar venda (${result.status})`);
    return;
  }

  alert("Venda registrada!");
  e.target.reset();
  carregarVendas();
});

// =======================
// CARREGAR LISTA
// =======================
async function carregarVendas() {
  const resp = await apiGet("/vendas/");
  if (!resp.ok) {
    alert((resp.data && resp.data.error) || `Erro ao carregar vendas (${resp.status})`);
    todasVendas = [];
    return;
  }
  todasVendas = resp.data || [];
  preencherFiltroProdutos();
  atualizarLista();
}

// =======================
// LISTAR VENDAS
// =======================
function atualizarLista() {
    const area = document.getElementById("lista-vendas");
    area.innerHTML = "";

    const busca = document.getElementById("busca").value.toLowerCase();
    const filtroProduto = document.getElementById("filtro-produto").value;

    let filtradas = todasVendas.filter(v =>
        v.cliente.toLowerCase().includes(busca)
    );

    if (filtroProduto) {
        filtradas = filtradas.filter(v => v.produto === filtroProduto);
    }

    filtradas.forEach(v => {
        const item = document.createElement("div");
        item.classList.add("venda-item");

        item.innerHTML = `
            <strong>${v.cliente}</strong><br>
            Produto: ${v.produto}<br>
            Valor: ${formatBRL(v.valor)}<br>
            Data: ${formatDateBR(v.data_venda)}
            <br>
            <button class="btn-delete" onclick="deletarVenda(${v.id})">Excluir</button>
        `;

        area.appendChild(item);
    });
}

// =======================
// DELETAR VENDA
// =======================
async function deletarVenda(id) {
    if (!confirm("Tem certeza que deseja excluir esta venda?")) return;

    const result = await apiDelete(`/vendas/${id}`);

    if (result.error) {
        alert("Erro: " + result.error);
        return;
    }

    alert("Venda excluída!");
    carregarVendas();
}

// =======================
// SELECT DE PRODUTOS
// =======================
function preencherFiltroProdutos() {
    const select = document.getElementById("filtro-produto");

    const produtos = [...new Set(todasVendas.map(v => v.produto))];
    select.innerHTML = `<option value="">Todos os produtos</option>`;

    produtos.forEach(p => {
        select.innerHTML += `<option value="${p}">${p}</option>`;
    });
}

// =======================
// EXPORTAÇÕES
// =======================
document.getElementById("exportar-excel").addEventListener("click", exportarExcel);
document.getElementById("exportar-pdf").addEventListener("click", exportarPDF);

function baixarArquivo(url, nomeArquivo) {
    fetch(url, {
        headers: {
            "Authorization": "Bearer " + localStorage.getItem("token")
        }
    })
        .then(r => r.blob())
        .then(blob => {
            const link = document.createElement("a");
            link.href = URL.createObjectURL(blob);
            link.download = nomeArquivo;
            link.click();
        });
}

function dataHoje() {
    return new Date().toISOString().split("T")[0];
}

function exportarExcel() {
    baixarArquivo("/vendas/export/excel", `vendas_${dataHoje()}.xlsx`);
}

function exportarPDF() {
    baixarArquivo("/vendas/export/pdf", `vendas_${dataHoje()}.pdf`);
}

// =======================
// VOLTAR / LOGOUT
// =======================
document.getElementById("logout").addEventListener("click", () => {
    localStorage.removeItem("token");
    window.location.href = "login.html";
});

document.getElementById("voltar-dashboard").addEventListener("click", () => {
    window.location.href = "dashboard.html";
});