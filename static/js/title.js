let button = d3.select("#submit");

// TODO
let baseURL = "API address";


let genre = "";
let rating = "";
let profit = "";

// Select the form
let form = d3.select("#form");

// Create event handlers for clicking the button or pressing the enter key
button.on("click", runEnter);
form.on("submit",runEnter);

// Create the function to run for both events
function runEnter() {
    prediction(document.getElementById("input_title").value)
    var tableBody = document.getElementById("table-body");
    var td1 = document.createElement("td");
    var td2 = document.createElement("td");
    var td3 = document.createElement("td");  
    var td4 = document.createElement("td");    
    var row = document.createElement("tr");

    td1.innerHTML = document.getElementById("input_title").value;
    td2.innerHTML = genre;
    td3.innerHTML = rating;
    td4.innerHTML = profit;

    row.appendChild(td1).className="d-inline-block text-truncate";
    row.appendChild(td2);
    row.appendChild(td3);
    row.appendChild(td4);
    tableBody.appendChild(row);
    document.getElementById("input_title").value = "";
    
}
function prediction(title){
    let url = baseURL+title
    // TODO   
    // d3.json(url, function(response) {
        genre = "Prediction";
        rating = "B";
        profit = "$0";
        
        // let genre = response.genre;
        // let rating = response.rating;
        // let profit = response.profit;
    // })
}



