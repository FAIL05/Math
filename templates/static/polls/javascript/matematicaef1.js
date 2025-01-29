const questoes = [
    {
        pergunta: "Qual número vem depois do 5?",
        opcoes: ["3", "4", "6"],
        resposta: "6"
    },
    {
        pergunta: "Quanto é 2 + 2?",
        opcoes: ["3", "4", "5"],
        resposta: "4"
    },
    {
        pergunta: "Se eu tenho 3 maçãs e ganho mais 2, quantas maçãs eu tenho?",
        opcoes: ["4", "5", "6"],
        resposta: "5"
    }
];

let indiceAtual = 0;
let pontuacao = 0;
let tempoRestante = 10;
let intervalo;

function iniciarTemporizador() {
    tempoRestante = 10;
    document.getElementById("tempo").innerText = tempoRestante;
    intervalo = setInterval(() => {
        tempoRestante--;
        document.getElementById("tempo").innerText = tempoRestante;
        if (tempoRestante === 0) {
            clearInterval(intervalo);
            proximaQuestao();
        }
    }, 1000);
}

function mostrarQuestao() {
    clearInterval(intervalo);
    iniciarTemporizador();

    const q = questoes[indiceAtual];
    document.getElementById("pergunta").innerText = q.pergunta;

    let opcoesHtml = "";
    q.opcoes.forEach(opcao => {
        opcoesHtml += `<button onclick="verificarResposta('${opcao}')">${opcao}</button>`;
    });

    document.getElementById("opcoes").innerHTML = opcoesHtml;
}

function verificarResposta(resposta) {
    clearInterval(intervalo);
    const q = questoes[indiceAtual];
    if (resposta === q.resposta) {
        document.getElementById("resultado").innerText = "Correto!";
        pontuacao++;
    } else {
        document.getElementById("resultado").innerText = "Tente novamente!";
    }
}

function proximaQuestao() {
    indiceAtual++;
    if (indiceAtual < questoes.length) {
        document.getElementById("resultado").innerText = "";
        mostrarQuestao();
    } else {
        document.getElementById("quiz-container").innerHTML = `<h2>Fim do quiz!</h2><p>Você acertou ${pontuacao} de ${questoes.length} perguntas.</p>`;
    }
}

mostrarQuestao();
