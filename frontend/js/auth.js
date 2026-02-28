document.getElementById("login-form").addEventListener("submit", async (e) => {
    e.preventDefault();

    const username = document.getElementById("username").value.trim();
    const password = document.getElementById("password").value;

    // envia para backend
    const res = await apiPost("/auth/login", {
        username,
        password
    });

    // se backend retornou erro
    if (res.error || !res.token) {
        alert(res.error || "Usuário ou senha incorretos");
        return;
    }

    // salva token
    localStorage.setItem("token", res.token);

    // redireciona
    window.location.href = "dashboard.html";
});