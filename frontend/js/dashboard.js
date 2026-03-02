// Proteção de rota
if (!localStorage.getItem("token")) {
    window.location.href = "login.html";
}

async function carregarDashboard() {
  const resp = await apiGet("/dashboard/");
  console.log("Dados recebidos:", resp);

function formatBRL(value) {
  const n = Number(value) || 0;
  return n.toLocaleString("pt-BR", { style: "currency", currency: "BRL" });
}
  if (!resp.ok) {
    alert((resp.data && resp.data.error) || `Erro ao carregar dashboard (${resp.status})`);
    return;
  }

  const dados = resp.data;

  document.getElementById("total-vendas").innerText = dados.total_vendas ?? 0;
  document.getElementById("total-valor").innerText = formatBRL(dados.total_valor);
  document.getElementById("media-valor").innerText = formatBRL(dados.media_valor);

  gerarGrafico(dados.vendas_por_produto || {});
}

function gerarGrafico(vendas) {
    const ctx = document.getElementById("grafico");

    new Chart(ctx, {
        type: "bar",
        data: {
            labels: Object.keys(vendas),
            datasets: [{
                label: "Vendas (R$)",
                data: Object.values(vendas),
                borderRadius: 6
            }]
        },
        options: {
            plugins: { legend: false },
            scales: {
               y: {
                  beginAtZero: true,
                  ticks: {
                    callback: (value) => formatBRL(value)
                  }
               },
                x: { grid: { display: false } }
            }
        }
    });
}

// Tema escuro (persistente)
const temaToggle = document.getElementById("tema-toggle");
temaToggle.checked = localStorage.getItem("tema") === "dark";

if (temaToggle.checked) document.body.classList.add("dark");

temaToggle.addEventListener("change", () => {
    const dark = temaToggle.checked;
    document.body.classList.toggle("dark", dark);
    localStorage.setItem("tema", dark ? "dark" : "light");
});

// Logout
document.getElementById("logout").addEventListener("click", () => {
    localStorage.removeItem("token");
    window.location.href = "login.html";
});

carregarDashboard();