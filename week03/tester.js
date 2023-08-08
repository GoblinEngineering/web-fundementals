
async function getData() {

    let Info = await fetch('https://goblinengineering.github.io/web-fundementals/week03/scripts/data.json');
    if (Info.ok){
    myJsonInfo = await Info.json()
    console.log(myJsonInfo)
    google.charts.load('current', {'packages':['corechart']});
    google.charts.setOnLoadCallback(drawChart());
    //dataValidator("naus")
    //console.log("entering tester area")
    //CreateGraphArray("naus")

    


}
}

function dataValidator(string){
    //making sure we have data on the card --
    var exists = (element) => element === string;
    //send back a True OR False
    return (Object.keys(myJsonInfo).some(exists))
}

function pullCardData(card){
    var infoArray = [card]
    myJsonInfo["tournamentInfo"]["tournyNamesList"].forEach(tournyName => {
        // logs the values and if they dont exist, makes them 0
        infoArray.push(myJsonInfo[card]["tournamentData"][tournyName] || 0)
    });
    console.log(infoArray)
    return infoArray
}

function CreateGraphArray(card1 = "", card2 = "", card3 = "", card4 = "", card5 = ""){
    // makes our Array by starting a list for each tourny
    var completedArray = [["Cards"]]
    myJsonInfo["tournamentInfo"]["tournyNamesList"].forEach(tournyName => {
        completedArray.push([tournyName])
    });

    // used to match index values in arrays when merging
    var x = 0 
    
    if (dataValidator(card1)){
        var cardData1 = pullCardData(card1)
        // logging data into our finished array
        cardData1.forEach(element => {
            completedArray[x].push(element)
            x++
        });
        x = 0
    }else{
        //console.log("missing Data on card" + card1)
    }
    //repeat for cards 2-5
    if (dataValidator(card2)){
        var cardData1 = pullCardData(card2)
        cardData1.forEach(element => {
            completedArray[x].push(element)
            x++
        });
        x = 0
    }else{
        //console.log("missing Data on card" + card2)
    }
    //card 3
    if (dataValidator(card3)){
        var cardData1 = pullCardData(card3)
        cardData1.forEach(element => {
            completedArray[x].push(element)
            x++
        });
        x = 0
    }else{
        //console.log("missing Data on card" + card3)
    }
    //card 4
    if (dataValidator(card4)){
        var cardData1 = pullCardData(card4)
        cardData1.forEach(element => {
            completedArray[x].push(element)
            x++
        });
        x = 0
    }else{
        //console.log("missing Data on card" + card4)
    }
    //card 5
    if (dataValidator(card5)){
        var cardData1 = pullCardData(card5)
        cardData1.forEach(element => {
            completedArray[x].push(element)
            x++
        });
        x = 0
    }else{
        //console.log("missing Data on card" + card5)
    }

    return completedArray
}


function drawChart() {
    console.log(myJsonInfo)
    
    

    // var data = google.visualization.arrayToDataTable([
    // ['tournament name', 'burnt offering', 'ad naus',"sun"],
    // [myJsonInfo["tournamentInfo"]["tournyNamesList"][0],  .5,      .25,.9],
    // ['punt city',  .7,      .5,.7],
    // ['cash 2',  .6,       .3,.6],
    // ['deviant esquire',  .2,      .15,.4],
    // ['jhon Wick',  .2,      .15,.4]
    // ]);

    var card1 = document.getElementById("CardInput1").value
    var card2 = document.getElementById("CardInput2").value
    var card3 = document.getElementById("CardInput3").value
    var card4 = document.getElementById("CardInput4").value
    var card5 = document.getElementById("CardInput5").value
    //card1 = "naus"
    if (card1 === "" || dataValidator(card1) === false){
        card1 = "naus"
    }

    var completedArray = CreateGraphArray(card1, card2, card3, card4, card5)
    var data = google.visualization.arrayToDataTable(completedArray);

    var options = {
    title: 'Card Playrate percent%',
    curveType: '',
    legend: { position: 'bottom' }
    };

    var chart = new google.visualization.LineChart(document.getElementById('curve_chart'));

    chart.draw(data, options);
}



google.load('visualization', '1', {'packages':['corechart']});


getData()


let buttonElementdiv = document.getElementById("RefreshButton")
buttonElementdiv.addEventListener("click", getData)
