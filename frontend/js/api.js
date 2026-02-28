// frontend/js/api.js
// Base URL vazio = mesma origem (funciona no Render e local)
const API_URL = "";

/**
 * Faz request e retorna um objeto padronizado:
 * { ok: boolean, status: number, data: any, raw?: string }
 */
async function apiRequest(method, endpoint, body = null) {
  const headers = {
    "Content-Type": "application/json",
  };

  const token = localStorage.getItem("token");
  if (token) headers["Authorization"] = "Bearer " + token;

  const options = { method, headers };
  if (body !== null) options.body = JSON.stringify(body);

  let res;
  try {
    res = await fetch(API_URL + endpoint, options);
  } catch (err) {
    return { ok: false, status: 0, data: { error: "Falha de rede" }, raw: String(err) };
  }

  const contentType = res.headers.get("content-type") || "";
  let data = null;
  let raw = "";

  try {
    if (contentType.includes("application/json")) {
      data = await res.json();
    } else {
      raw = await res.text();
      data = raw;
    }
  } catch (e) {
    raw = "Falha ao ler resposta";
    data = { error: raw };
  }

  return { ok: res.ok, status: res.status, data, raw };
}

async function apiGet(endpoint) {
  return apiRequest("GET", endpoint);
}

async function apiPost(endpoint, data) {
  return apiRequest("POST", endpoint, data);
}

async function apiDelete(endpoint) {
  return apiRequest("DELETE", endpoint);
}