async function sendText() {
    // ON RÉCUPÈRE LES VARIABLES À ENVOYER AU SERVEUR
    var title = document.getElementById('editableTitle').textContent;
    var inText = document.getElementById('inText').value;

    // ON EMBALLE NOTRE VARIABLE DANS UN DICTIONNAIRE
    // ON PEUT ENVOYER AUTANT DE VARIABLES QU'ON VEUT, ICI ON SE CONTENTE D'ENVOYER inText
    var colis = {
        titre: title,
        texte: inText
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
    const response = await fetch('/save_text/', requete)
    const data = await response.json();
    alert(data.reponse);
}





const editableTitle = document.getElementById('editableTitle');
const saveButton = document.getElementById('saveButton');

// Load saved content on page load
window.addEventListener('load', () => {
    const savedTitle = localStorage.getItem('savedTitle');
    if (savedTitle) {
        editableTitle.textContent = savedTitle;
    }
});

// Save the content when Enter key is pressed
editableTitle.addEventListener('keydown', (event) => {
    if (event.key === 'Enter') {
        event.preventDefault(); // Prevent line break
        saveTitle();
    }
});

// Save the content when the element loses focus (blur event)
editableTitle.addEventListener('blur', () => {
    saveTitle();
});

function saveTitle() {
    const newTitle = editableTitle.textContent;
    localStorage.setItem('savedTitle', newTitle); // Save content to localStorage
    console.log('New title:', newTitle);
}






