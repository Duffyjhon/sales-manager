// Proteção de rota
if (!localStorage.getItem("token")) {
    window.location.href = "login.html";
}

async function carregarDashboard() {
    const dados = await apiGet("/dashboard/");

    console.log("Dados recebidos:", dados);

    document.getElementById("total-vendas").innerText = dados.total_vendas;
    document.getElementById("total-valor").innerText = "R$ " + dados.total_valor.toFixed(2);
    document.getElementById("media-valor").innerText = "R$ " + dados.media_valor.toFixed(2);

    gerarGrafico(dados.vendas_por_produto);
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
                y: { beginAtZero: true },
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