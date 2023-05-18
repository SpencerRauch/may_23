// alert("Linked!")

const URL = 'https://pokeapi.co/api/v2/pokemon/'
const resultDiv = document.querySelector('#pokeResult')
const nameInput = document.querySelector('#pokeName')

function getPoke(event){
    event.preventDefault()
    // console.log("function ran")
    console.log(nameInput.value)
    resultDiv.innerHTML = "Loading...."
    fetch(URL + nameInput.value)
        .then(response => response.json())
        .then(data => {
            console.log(data)
            resultDiv.innerHTML = `
                <h3> Poke No: ${data.id} ${data.name} </h3>
                <img src="${data.sprites.front_default}" alt="${data.name}">
            `

        })
        .catch(err => {
            resultDiv.innerHTML = 'Not found'
        })

}

async function randPoke(){
    console.log("clicked rand")
    let rand = Math.floor(Math.random() * 900)
    let response = await fetch(URL + rand)
    let data = await response.json()
    resultDiv.innerHTML = `
                <h3> Poke No: ${data.id} ${data.name} </h3>
                <img src="${data.sprites.front_default}" alt="${data.name}">
            `


}