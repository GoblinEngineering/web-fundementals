google.load('visualization', '1', {'packages':['corechart']});

getData()

async function getData() {
    let Info = await fetch('https://goblinengineering.github.io/web-fundementals/week03/scripts/data.json');
    if (Info.ok){
    myJsonInfo = await Info.json()
    console.log(myJsonInfo)
    google.charts.load('current', {'packages':['corechart']});
    google.charts.setOnLoadCallback(drawChart());
    //google.charts.setOnLoadCallback(drawChart(data));
    


}
}

//console.log(data["name"])

function drawChart() {
    console.log(myJsonInfo)
    

    var data = google.visualization.arrayToDataTable([
    ['tournament name', 'burnt offering', 'ad naus',"sun"],
    [myJsonInfo["tournamentInfo"]["tournyNamesList"][0],  .5,      .25,.9],
    ['punt city',  .7,      .5,.7],
    ['cash 2',  .6,       .3,.6],
    ['deviant esquire',  .2,      .15,.4]
    ]);

    var options = {
    title: 'Card Playrate',
    curveType: '',
    legend: { position: 'bottom' }
    };

    var chart = new google.visualization.LineChart(document.getElementById('curve_chart'));

    chart.draw(data, options);
}

function click(){
    console.log("click")
}

let buttonElementdiv = document.getElementById("RefreshButton")
buttonElementdiv.addEventListener("click", getData)
