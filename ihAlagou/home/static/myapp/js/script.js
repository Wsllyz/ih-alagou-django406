var distancia = '{{ dados|escapejs }}';
var marker;
var cor;
var map = L.map('map').setView([-8.0526073, -34.8845963], 19);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

pegarDistancia();
setInterval(pegarDistancia, 5000);

function pegarDistancia() {
    $.ajax({
        url: "{% url 'distancia_view' %}",
        type: "GET",
        success: function(data) {
            console.log(data);
            distancia = data.dados.feeds[0].field5;
            console.log(distancia);
            atualizar();
        }
    });
}

function atualizar() {
    if (distancia > 25) {
        cor = "{% static 'home/css/src/pontoVermelho.png' %}";
    } else if (distancia > 19) {
        cor = "{% static 'home/css/src/pontoLaranja.png' %}";
    } else if (distancia > 14) {
        cor = "{% static 'home/css/src/pontoAmarelo.png' %}";
    } else if (distancia > 9) {
        cor = "{% static 'home/css/src/pontoCiano.png' %}";
    } else {
        cor = "{% static 'home/css/src/pontoVerde.png' %}";
    }
}

// função com lister no ícone para abrir o card
marker.on('click', function() {
    var cardDiv = document.getElementById('cardDiv');
    if (cardDiv.classList.contains('hidden')) {
        cardDiv.classList.remove('hidden');
        cardDiv.classList.add('visible');
    } else {
        cardDiv.classList.remove('visible');
        cardDiv.classList.add('hidden');
    }
});

function openPopup() {
    document.getElementById("popup").style.display = "block";
}

function closePopup() {
    document.getElementById("popup").style.display = "none";
}