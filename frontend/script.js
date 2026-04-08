document.getElementById('wineForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const resDiv = document.getElementById('resultado');
    
    // 1. Coleta os valores dos 11 campos
    const features = [];
    for(let i=1; i<=11; i++) {
        const val = document.getElementById(`f${i}`).value;
        features.push(parseFloat(val));
    }

    // 2. Feedback visual de carregamento
    resDiv.style.display = 'block';
    resDiv.innerHTML = "Processando análise...";
    resDiv.className = ""; 

    try {
        // 3. Chamada para a API Flask (certifique-se que o app.py está rodando)
        const response = await fetch('/prever', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ features: features })
        });

        const data = await response.json();

        if (response.ok) {
            // 4. Exibe o resultado de sucesso
            resDiv.className = 'sucesso';
            resDiv.innerHTML = `
                <h3 style="margin:0">Resultado: ${data.status}</h3>
                <p>Nota Sugerida: <strong>${data.nota}</strong></p>
                <small>Confiança do Modelo: ${data.confianca}%</small>
            `;
        } else {
            alert("Erro na API: " + (data.erro || "Falha desconhecida"));
            resDiv.style.display = 'none';
        }
    } catch (error) {
        alert("Não foi possível conectar ao servidor backend (app.py).");
        console.error("Erro de conexão:", error);
        resDiv.style.display = 'none';
    }
});