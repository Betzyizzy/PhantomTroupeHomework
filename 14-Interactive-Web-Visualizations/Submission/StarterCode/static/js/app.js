$(document).ready(function() {
    getData();
    $("#selDataset").on("change", function() {
        getData();
    });
});

function getData() {
    let url = "samples.json";
    $.ajax({
        type: "GET",
        url: url,
        contentType: "application/json",
        dataType: "json",
        success: function(data) {
            Dropdown(data);
            BarChart(data);
            BubbleChart(data);
            Table(data);
        
        },
        error: function(data) {
            console.log("Error");
        },
        complete: function(data) {
            console.log("Request finished");
        }
    });
}


function Dropdown(data) {
    let names = data.names;

    for (let i = 0; i < names.length; i++) {
        let name = names[i];
        let html_option = `<option value="${name}">${name}</option>`;
        $("#selDataset").append(html_option);
    }
}


function Table(data) {
    let id = parseInt($("#selDataset").val());
    let currentData = data.metadata.filter(x => x.id === id)[0];

    $("#sample-metadata").empty();

    let items = Object.entries(currentData).map(([key, value]) => `${key}: ${value}`);
    for (let i = 0; i < items.length; i++) {
        let item = items[i];
        let text = `<p>${item.charAt(0).toUpperCase() + item.slice(1)}<p>`;
        $("#sample-metadata").append(text);
    }
}



function BarChart(data){
    let id = $("#selDataset").val();
    let currentData = data.samples.filter(x => x.id === id)[0];
    
    let trace = {
        x: currentData.sample_values.slice(0, 10).reverse(),
        y: currentData.otu_ids.map(x => `OTU ID: ${x}`).slice(0, 10).reverse(),
        text: currentData.otu_labels.slice(0, 10).reverse(),
        name: "Bacteria Count",
        type: "bar",
        marker: {
            color: 'rgb(158,202,225)',
            opacity: 0.6,

        },
        orientation: 'h',
        text: currentData.otu_labels,
    };

    let traces = [trace];

    let layout = {
        title: 'Bacteria Count',
        xaxis: {
            title: 'Count'
        },
        margin: {
            l: 90,
            r: 30,
            b: 0,
            t: 30,
            pad: 0
          }
    };
    
    Plotly.newPlot('bar', traces, layout);


}


function BubbleChart(data){
    let id = $("#selDataset").val();
    let currentData = data.samples.filter(x => x.id === id)[0];

    let trace = {
        x: currentData.otu_ids,
        y: currentData.sample_values,
        mode: 'markers',
        text: currentData.otu_labels,
        marker: {
            color: [10, 50, 100, 150, 200, 175],
            colorscale: [[0, 'rgb(255,192,203)'], [1, 'rgb(176,224,230)']],
            cmin: 0,
            cmax: 200,
            size: [600, 1200, 800, 400, 1500, 2000],
            sizemode: 'area',
            showscale: true,
            colorbar: {
              thickness: 10,
              y: 0.5,
              ypad: 0,
              title: 'Tree Density',
              titleside: 'bottom',
              outlinewidth: 1,
              outlinecolor: 'black',
              tickfont: {
                family: 'Lato',
                size: 14,
                color: 'blue'
              }
            }
          }
        };
        
    
    traces = [trace];

    let layout = {
        showlegend: false,
        xaxis: {
            title: 'OTU ID'
        },
        margin: {
            l: 80,
            r: 80,
            b: 0,
            t: 10,
            pad: 0
          }
      };

    Plotly.newPlot("bubble", traces, layout);



}

