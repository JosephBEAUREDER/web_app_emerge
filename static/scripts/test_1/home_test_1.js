showProjects();

async function showProjects() {

    const requete = { 
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
    };

    const response = await fetch('/show_all_projects', requete)

    const data = await response.json();

    console.log(data['projects'])

    var projectsDiv = document.getElementById('all-projects');
    projectsDiv.innerHTML = "";

    data['projects'].forEach((project) => {
        var projectRow = `
        <tr class="table-primary">
            <th scope="row">
               <a href="edit_project/${project.id}">${project.name}</a>
            </th>
            <td>${project.id}</td>
            <td>
            <button type="button" class="btn btn-secondary" data-bs-container="body" data-bs-toggle="popover" data-bs-placement="top" data-bs-content="<div class='color-bubble'></div>" data-bs-original-title="Popover Title" aria-describedby="popover590883">Top</button>    </td>
            
        </tr>
        `;
        projectsDiv.innerHTML += projectRow;
    });
    initializePopovers();
}

async function create_project() {
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






  function initializePopovers() {
    var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'))
    var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl)
    })
}


