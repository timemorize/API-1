$(document).ready(function () {
    const data1 = {
    labels: listaEntidades,
    datasets: [{
        label: 'Quantdade:',
        data: listaQuantidadeEntidades,
        backgroundColor: [
        'rgba(255, 99, 132, 0.2)',
        'rgba(54, 162, 235, 0.2)',
        'rgba(255, 206, 86, 0.2)',
        'rgba(75, 192, 192, 0.2)',
        'rgba(153, 102, 255, 0.2)',
        'rgba(255, 159, 64, 0.2)'
        ],
        borderColor: [
        'rgba(255, 99, 132, 1)',
        'rgba(54, 162, 235, 1)',
        'rgba(255, 206, 86, 1)',
        'rgba(75, 192, 192, 1)',
        'rgba(153, 102, 255, 1)',
        'rgba(255, 159, 64, 1)'
        ],
        borderWidth: 1
    }]
    };

    const data2 = {
    labels: listaTurmas,
    datasets: [{
        label: 'Quantidade de Alunos por Turma',
        data: listaQuantidadeAlunosTurma,
        backgroundColor: 'rgba(75, 192, 192, 0.2)',
        borderColor: 'rgba(75, 192, 192, 1)',
        borderWidth: 1
    }]
    };

    const config1 = {
    type: 'bar',
    data: data1,
    options: {
        scales: {
        y: {
            beginAtZero: true
        }
        }
    }
    };

    const config2 = {
    type: 'doughnut',
    data: data2,
    options: {
        plugins: {
        legend: {
            position: 'bottom'
        }
        }
    }
    };

    var ctx1 = $('#chart1')[0].getContext('2d');
    new Chart(ctx1, config1);

    var ctx2 = $('#chart2')[0].getContext('2d');
    new Chart(ctx2, config2);
});