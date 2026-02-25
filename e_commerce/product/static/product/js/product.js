let OFFSET = 0;
const LIMIT = 1;
let SEARCH_QUERY = "" 


function handle_search(event){
     SEARCH_QUERY = document.getElementById('search').value
     api_handler()
     console.log(SEARCH_QUERY)
}
function handle_next(){
    OFFSET += LIMIT
    api_handler()
    console.log(OFFSET)

}
function handle_prev(){
    OFFSET -= LIMIT
    if (OFFSET < 0){
        OFFSET = 0
       
    }
     api_handler()
    console.log(OFFSET)
}

async function api_handler(){
    const url = `/product/api/?offset=${OFFSET}&limit=${LIMIT}&search=${SEARCH_QUERY}`
    const  response = await fetch(url)
    const data = await response.json()
    console.log( "Ramesh das",data)
    
}



