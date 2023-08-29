async function getItems() {

    // PARAMÈTRES DE LA REQUÊTE
    const requete = { 
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
    };

    // ENVOI ET RÉCUPÉRATION DE LA RÉPONSE
    const response = await fetch('/todolist/list', requete)
    const data = await response.json();
    console.table(data['items']);


var itemsDiv = document.getElementById('items');
itemsDiv.innerHTML = ""; // on vide la div pour la réinitialiser

data['items'].forEach( (item) => {
    itemsDiv.innerHTML += `<div class="card border-primary m-3" style="width: 30rem;">
                         <div class="card-header d-flex justify-content-between">
                         <div>Item id ${item.id}</div>
                          <button type="button" class="btn btn-danger" onclick="delItem(${item.id})">
                              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-trash" viewBox="0 0 16 16">
                                <path d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0V6z"/>
                                 <path fill-rule="evenodd" d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1v1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4H4.118zM2.5 3V2h11v1h-11z"/>
                              </svg>
                         </button>
                    </div>
                     <div class="card-body">
                    <h4 class="card-title">${item.titre}</h4>
                    <p class="card-text">${item.texte}</p>
                    </div>
                </div>`
})
}




function addItem() {
    var titre = document.getElementById('addItemTitre').value;
    var texte = document.getElementById('addItemTexte').value;

    fetch('/todolist/create_item/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ titre, texte })
    })

    .then(response => response.json())
    .then(data => {
        console.log("Item added successfully with ID:", data.item_id);
    })
    .catch(error => {
        console.error("Failed to add item:", error);
    });
}


async function delItem(id) {
    
    var colis = {
        identifiant: id
    }    
    console.log('Envoi colis:',colis);

    // PARAMÈTRES DE LA REQUÊTE
    const requete = { 
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(colis)
    };

    // ENVOI ET RÉCUPÉRATION DE LA RÉPONSE
    const response = await fetch('/todolist/del', requete)
    const data = await response.json();
    console.log(data);

    getItems(); // on reliste les items pour mettre à jour la page.
}