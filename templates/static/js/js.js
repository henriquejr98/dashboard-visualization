function render_likelihood_endyear(url){
    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){

        const ctx = document.getElementById('likelihood_endyear').getContext('2d');
        const myChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: data.labels,
                datasets: [{
                    label: 'Likelihood',
                    data: data.data,
                    backgroundColor: "#CB1EA8",
                    borderColor: "#bd31c4",
                    borderWidth: 1
                }]
            },
        });
    })
}

function render_relevance_pestle(url){

    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){

        const ctx = document.getElementById('relevance_pestle').getContext('2d');
        const myChart = new Chart(ctx, {
            type: 'radar',
            data: {
                labels: data.labels,
                datasets: [{
                    label: 'Relevance',
                    data: data.data,
                    fill: true,
                    backgroundColor: 'rgba(255, 99, 132, 0.2)',
                    borderColor: "#bd31c4",
                    pointBackgroundColor: "#bd31c4",
                    pointBorderColor: '#fff',
                    pointHoverBackgroundColor: '#fff',
                    pointHoverBorderColor: "#bd31c4"
                  }, {
                    label: 'Intensity',
                    data: data.data2,
                    fill: true,
                    backgroundColor: 'rgba(54, 162, 235, 0.2)',
                    borderColor: "#3518b8",
                    pointBackgroundColor: "#3518b8",
                    pointBorderColor: '#fff',
                    pointHoverBackgroundColor: '#fff',
                    pointHoverBorderColor: "#3518b8"
                  }]
            },
        });
    })
}

function render_relevance_region(url){

    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){

        const ctx = document.getElementById('relevance_region').getContext('2d');
        const myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: data.labels,
                datasets: [{
                    label: 'Relevance',
                    data: data.data,
                    backgroundColor: "#CB1EA8",
                    borderColor: "#bd31c4",
                    borderWidth: 1
                },
                {
                    label: 'Intensity',
                    data: data.data2,
                    borderColor: "#3518b8",
                    type: 'line',
                    order: 1
                }]
            },
        });
    })
}

