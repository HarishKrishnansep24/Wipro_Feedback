window.onload = average_graph();

function average_graph() {
    console.log("{{ trainer_list_json }}")
    var trainer_list = JSON.parse('{{ trainer_list_json|safe }}');
    var score_list = JSON.parse('{{ average_score_json|safe }}');

    console.log(trainer_list)

    var nameArr = []

    for (var i = 0; i < trainer_list.length; i++) {
        nameArr.push(trainer_list[i].name)
    }
    console.log(nameArr)
    console.log(score_list);

    var canvas = document.getElementById("graph");
    var data = {
        labels: nameArr,
        datasets: [{
            label: "Sales",
            data: score_list,
            backgroundColor: "rgba(75,192,192,0.4)",
            borderColor: "rgba(75,192,192,1)"
        }]
    };



    // Set the options for the graph
    var options = {
        scales: {
            y: {
                beginAtZero: true,
                ticks: {
                    min: 0,
                    max: 20,
                    stepSize: 1,
                    callback: function (value, index, values) {
                        if (Math.floor(value) === value) {
                            return value;
                        }
                    }
                }
            }
        }
    };

    // Create the bar chart
    var barChart = new Chart(canvas, {
        type: 'bar',  //change the type to bar
        data: data,
        options: options
    });
}