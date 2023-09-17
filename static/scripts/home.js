async function saveText() {

    var title = document.getElementById('editableTitle').textContent;
    var inText = document.getElementById('inText').value;

    var colis = {
        titre: title,
        texte: inText
    }
    const requete = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(colis)
    };
    const response = await fetch('/save_text/', requete)
    const data = await response.json();
}


async function createNewProject() {
    const requete = { 
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
    };

    const response = await fetch('/create_new_project/', requete)
    const data = await response.json();

    showProjects();

  }




async function showProjects() {

    const requete = { 
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
    };

    const response = await fetch('/show_all_projects', requete)

    const data = await response.json();


    var projectsDiv = document.getElementById('all-projects');
    projectsDiv.innerHTML = "";

    var rowDiv = document.createElement('div');
    rowDiv.className = 'row align-items-center';

    data['projects'].forEach((project, index) => {
        const cardHTML = `
            <div class="col-md-4">
                <div class="card text-white bg-primary mb-3" style="max-width: 20rem;">
                    <div class="card-body" id="${project.id}">
                        <div class="d-flex justify-content-between align-items-center">
                        <h4 class="card-title" id="editableTitle{{ project.id }}" contentEditable data-projectId="{{ project.id }}"> ${ project.name }</h4>
                        <button type="button" class="btn btn-danger" onclick="delProject('${project.id}')">
                                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" fill="currentColor" class="bi bi-trash" viewBox="0 0 16 16">
                                    <path d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0V6z"/>
                                    <path fill-rule="evenodd" d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1v1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4H4.118zM2.5 3V2h11v1h-11z"/>
                                </svg>
                            </button>
                        </div>
                        <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                        <div class="row">
                            <div class="col-md-12">
                                <textarea id="inText${project.id}" class="form-control" rows="3"></textarea>
                            </div>
                        </div>
                        <div class="row">
                            <div class="text-end mt-2 ml-6">
                                <button name="save" id="send_item${project.id}" onclick="saveText()" class="btn btn-success">Add content</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        `;

        rowDiv.innerHTML += cardHTML;

        // Check if we need to create a new row div or if it's the last card
        if ((index + 1) % 3 === 0 || (index + 1) === data['projects'].length) {
            projectsDiv.appendChild(rowDiv);
            rowDiv = document.createElement('div');
            rowDiv.className = 'row align-items-center';
        }
    });

    const buttonHTML = `
        <div class="col-md-4">
            <button id="createProjectBtn" class="btn btn-primary" onclick="createNewProject()">Create New Project</button>
        </div>
    `;
    rowDiv.innerHTML += buttonHTML;
    projectsDiv.appendChild(rowDiv);
    
}


  async function delProject(id) {
    
    var colis = {
        id: id
    }    
    const requete = { 
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(colis)
    };
    const response = await fetch('/del_project/', requete)
    const data = await response.json();
    console.log(data);
    
    showProjects();
  }


  document.querySelectorAll('[contentEditable]').forEach(contentEditableElement => {
    contentEditableElement.addEventListener('blur', async (event) => {
    const projectId = event.target.getAttribute('data-projectId');
      const newName = event.target.textContent;

      alert(newName)
      alert(projectId)

      // Send an AJAX request to update the project name
    try {
        const response = await fetch('/update_project_name', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ id: projectId, name: newName }),
        });
  
        if (response.ok) {
          console.log('Project name updated successfully.');
        } else {
          console.error('Failed to update project name.');
        }
      } catch (error) {
        console.error('Error updating project name:', error);
      }
     });
  });

















































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






