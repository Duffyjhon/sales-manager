const API_URL = "";

// GET (buscar dados)
async function apiGet(endpoint) {
    const resposta = await fetch(API_URL + endpoint, {
        method: "GET",
        headers: {
            "Authorization": "Bearer " + localStorage.getItem("token"),
            "Content-Type": "application/json"
        }
    });

    return resposta.json();
}

// POST (enviar dados)
async function apiPost(endpoint, data) {
    const resposta = await fetch(API_URL + endpoint, {
        method: "POST",
        headers: {
            "Authorization": "Bearer " + localStorage.getItem("token"),
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    });

    return resposta.json();
}
async function apiDelete(endpoint) {
    const resposta = await fetch(API_URL + endpoint, {
        method: "DELETE",
        headers: {
            "Authorization": "Bearer " + localStorage.getItem("token"),
            "Content-Type": "application/json"
        }
    });

    return resposta.json();
}