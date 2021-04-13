function init() {
    dataBar = [{
        // values
        x: [5, 6, 7, 8],
        // labels
        y: ["A", "B", "C", "D"],
        // texthover
        text: ['A', 'B', 'C', 'D'],
        type: "bar",
        orientation: "h",
        marker: {
            color: 'rgb(142,124,195)'
        }
    }];
    layoutBar = {
        title: "<b>Best movies</b>"
    }

    Plotly.newPlot("bar", dataBar, layoutBar);
    bubbleData = [{
        x: [1, 2, 3, 4],
        y: [10, 11, 12, 13],
        mode: 'markers',
        text: ['A', 'B', 'C', 'D'],
        marker: {
            color: ['rgb(93, 164, 214)', 'rgb(255, 144, 14)', 'rgb(44, 160, 101)', 'rgb(255, 65, 54)'],
            // opacity: [1, 0.8, 0.6, 0.4],
            size: [40, 60, 80, 100]
        }
    }];

    var layoutBubble = {
        title: '<b>most famues actor/actres </b>',
        // xaxis: { title: "OTU Ids" },
        yaxis: { title: "Actor/Actres Name " }
        // showlegend: false,
        // height: 600,
        // width: 600
    };
    Plotly.newPlot("bubble", bubbleData, layoutBubble)

    var data = [{
        values: [19, 26, 55],
        labels: ['Residential', 'Non-Residential', 'Utility'],
        type: 'pie'
      }];
      
      var layout = {
        height: 400,
        width: 500
      };
      
      Plotly.newPlot('pie', data, layout);
      

}
init();
