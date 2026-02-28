// frontend/js/auth.js
document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("login-form");
  if (!form) return;

  form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const username = document.getElementById("username").value.trim();
    const password = document.getElementById("password").value;

    const res = await apiPost("/auth/login", { username, password });

    if (!res.ok) {
      // seu backend usa {error: "..."}
      alert((res.data && res.data.error) || "Usuário ou senha incorretos");
      return;
    }

    // seu backend retorna {token: "..."}
    const token = res.data && (res.data.token || res.data.access_token);
    if (!token) {
      alert("Login ok, mas não recebi o token. Verifique a rota /auth/login.");
      return;
    }

    localStorage.setItem("token", token);

    // no Render e local funciona assim:
    window.location.href = "/dashboard.html";
  });
});