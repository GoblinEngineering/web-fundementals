

// saves only strings, anything else it trys to coerce to a string
localStorage.setItem("key", "Value")
// you can get around this by swapping between data types by useing
// JSON.stringify({YOUR ARRAY HERE}) to change your array into a string and then back with
// JSON.parse("YOUR STRING HERE") when you call it.


//retrives item
localStorage.getItem("key")

// if data is already saved, instead of throwing a error it saves over it
if (localStorage.getItem("key") === null) {
    //we now know that there previous data
}
// remove data
localStorage.removeItem("key")

// clears everything
localStorage.clear()
// local storage can only hold 5MB

// session storage equivilant
sessionStorage.setItem("key", "Value")

// usage ideas
// search history on a search bar
// dark mode/light mode or other site prefrences
