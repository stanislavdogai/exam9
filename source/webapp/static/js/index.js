async function makeRequest(url, method='GET') {
    let response = await fetch(url, {method});

    if (response.ok) {
        return await response.json();
    } else {
        let error = new Error(response.statusText);
        error.response = response;
        throw error;
    }
}
let favorite = async function (event){
    let url = event.target.dataset.photoUrl
    let data = await makeRequest(url)
    let button = event.target
    if (button.innerText == 'В избранное'){
        button.innerText = 'Удалить из избранного'
    }
    else {
        button.innerText = 'В избранное'
    }

}

let favorite_album = async function (event){
    let url = event.target.dataset.photoUrl
    let data = await makeRequest(url)
    let button = event.target
    if (button.innerText == 'В избранное'){
        button.innerText = 'Удалить из избранного'
    }
    else {
        button.innerText = 'В избранное'
    }

}