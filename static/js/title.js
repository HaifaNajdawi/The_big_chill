let button = d3.select("#submit");

let baseURL = "https://the-big-chill.herokuapp.com/ML?plot=";


let genre = "";
let rating = "";
let profit = "";

// Select the form
let form = d3.select("#form");

// Create event handlers for clicking the button or pressing the enter key
button.on("click", runEnter);
form.on("submit",runEnter);

function prediction(title){
    let url = baseURL+title  
    // console.log(url)
    // let genres = ""
    d3.json(url, function(response) {
        var genres = ""
        var rating = ""
        // console.log("This is a response: " + response)
        // for (var i = 0; i < response.length; i++){
        //     genres += response[i][0][0];
        
        //     console.log("hello d3"+genres)
        // }
        genres += response[0][0]
        rating += response[1][0]
        // console.log(typeof(response))        
        // console.log("Rating is : " +rating)

    var tableBody = document.getElementById("table-body");
    var td1 = document.createElement("td");
    var td2 = document.createElement("td");
    var td3 = document.createElement("td");  
    var row = document.createElement("tr");

    td1.innerHTML = document.getElementById("input_title").value;
    td2.innerHTML = genres;
    td3.innerHTML = rating;
    // console.log("genre" + genre)

    row.appendChild(td1).className="wrap";
    row.appendChild(td2);
    row.appendChild(td3);
    tableBody.appendChild(row);
    document.getElementById("input_title").value = "";

    })
    // console.log(genres)
}
// Create the function to run for both events
function runEnter() {
   prediction(document.getElementById("input_title").value)
    
}



