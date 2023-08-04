



/* BUILT-IN METHODS */

// Step 1: Declare and instantiate a variable of type Date to hold the current date
let date = new Date()
// Step 2: Declare a variable to hold the current year
let year = date.getFullYear()
// Step 3: Using the variable declared in Step 1, call the built-in getFullYear() method/function and assign it to the variable declared in Step 2

// Step 4: Assign the current year variable to an HTML form element with an ID of year
document.getElementById('year').textContent = year

/* ARRAY METHODS */





// FInal Area

// ELEMENTS TO CHANGE 

let your_div = document.getElementById("sumOfMultiplied").parentElement
let text_to_change = your_div.childNodes[0];

text_to_change.nodeValue = 'Random Fact : ';


document.getElementById("multiplied").parentElement.childNodes[0].nodeValue = "Character Name : "

document.getElementById("array").parentElement.textContent = arrayMain = ""
document.getElementById("odds").parentElement.textContent = odds = ""
document.getElementById("evens").parentElement.textContent = even = "" 
document.getElementById("sumOfArray").parentElement.textContent = sum = "" 




// Functions

function RandPersonID(){
    return  1//Math.floor(Math.random() * 39) + 1;
}

function RandInfoType(){
    let type = Math.floor(Math.random() * 7)
    let key = ""
    switch (type){
        case 0:
          key = "gender";
          break;
        case 1:
            key = "height";
          break;
        case 2:
            key = "mass";
          break;
        case 3:
          key = "hair_color";
          break;
        case 4:
          key = "skin_color";
          break;
        case 5:
          key = "eye_color";
          break;
        case 6:
          key = "birth_year";
        default:
          key = "gender"; 
      }
    return key
}





async function getStarWarsInfo(PersonID){

    //let Info = await fetch('https://swapi.dev/api/people/' + RandPersonID() + '/');
    let Info = await fetch('https://goblinengineering.github.io/web-fundementals/week03/scripts/data.json');
    if (Info.ok){
        data = await Info.json()
        //
        console.log(data)
        let infotype = RandInfoType()
        console.log(data["name"])
        console.log(infotype)
        console.log(data[infotype])
        document.getElementById("sumOfMultiplied").textContent = infotype + " - " + data[infotype]
        document.getElementById("multiplied").textContent = data["name"]
        
    }
}




let test = RandPersonID()
console.log(test)
getStarWarsInfo(test)
console.log(RandInfoType())

document.getElementById("divideNumbers").value = "CLICK ME PLEASE"
let buttonElementdiv = document.getElementById("divideNumbers")
buttonElementdiv.addEventListener("click", getStarWarsInfo)
