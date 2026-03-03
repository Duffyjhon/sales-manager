// Proteção de rota
if (!localStorage.getItem("token")) {
    window.location.href = "login.html";
}
function formatBRL(value) {
  const n = Number(value) || 0;
  return n.toLocaleString("pt-BR", { style: "currency", currency: "BRL" });
}

async function carregarDashboard() {
  const resp = await apiGet("/dashboard/");
  console.log("Dados recebidos:", resp);

  if (!resp.ok) {
    alert((resp.data && resp.data.error) || `Erro ao carregar dashboard (${resp.status})`);
    return;
  }

  const dados = resp.data; // ✅ primeiro define, depois usa
  console.log("DADOS:", dados);

  document.getElementById("total-vendas").innerText = dados.total_vendas ?? 0;
  document.getElementById("total-valor").innerText = formatBRL(dados.total_valor);
  document.getElementById("media-valor").innerText = formatBRL(dados.media_valor);

  const serie = (dados.vendas_por_mes && Object.keys(dados.vendas_por_mes).length)
    ? dados.vendas_por_mes
    : (dados.vendas_por_produto || {});

  gerarGrafico(serie);
}

let chartInstance = null;

function gerarGrafico(vendas) {
  const canvas = document.getElementById("grafico");
  if (!canvas) return;

  const labels = Object.keys(vendas);
  const values = Object.values(vendas);

  // Se não tiver dados, evita criar gráfico vazio
  if (!labels.length) {
    if (chartInstance) chartInstance.destroy();
    chartInstance = null;
    return;
  }

  if (chartInstance) chartInstance.destroy();

  chartInstance = new Chart(canvas, {
    type: "line",
    data: {
      labels,
      datasets: [
        {
          label: "Faturamento (R$)",
          data: values,
          fill: true,
          tension: 0.35,
          pointRadius: 4,
          pointHoverRadius: 6,
          borderWidth: 3
        }
      ]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false, // ✅ deixa o CSS mandar na altura
      plugins: {
        legend: { display: false },
        tooltip: {
          callbacks: {
            label: (ctx) => formatBRL(ctx.parsed.y)
          }
        }
      },
      scales: {
        y: {
          beginAtZero: true,
          ticks: {
            callback: (value) => formatBRL(value)
          }
        },
        x: {
          grid: { display: false }
        }
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