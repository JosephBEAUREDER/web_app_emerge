showProjects();


async function showTopics() {
    const requete = { 
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
    };

    const response = await fetch('show_all_topics', requete)

    const data = await response.json();

    console.log(data)
}



async function showProjects() {

    const requete = { 
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
    };


    const response = await fetch('show_all_projects', requete)

    const data = await response.json();

    console.log(data)


    var projectsDiv = document.getElementById('all-projects');
    projectsDiv.innerHTML = "";

    let bubbles = '';
    data['topics'].forEach(topic => {
        var topicBubble = `<div class='color-bubble' style='background-color:${topic.color}'></div>`;
        bubbles += topicBubble;
    });

    console.log(bubbles); // Log the bubbles variable

    let projectRows = '';
    data['projects'].forEach((project) => {
    
        console.log(project.color);

        var projectRow = `
        <tr class="table-primary">
            <th scope="row">
               <a href="edit_project/${project.id}">${project.name}</a>
            </th>
            <td>${project.id}</td>
            <td>


            <details data-popover="up">

                <summary> 
                    <div class='color-bubble' style='background-color:${project.color}'></div> 
                </summary>

                <div class="popover-wrapper">
                <div class="popover-title"> Here are your topics </div>

                    <div class="popover-content">
                        <div class="bubble-wrapper">
                            <div class='bubble-row'>
                                ${bubbles}

                                <div class='color-bubble plus-bubble'>+</div>
                            </div>
                        </div>
                    </div>
                    <div class='bubble-row'></div> <!-- Extra row -->

                </div>
          </details>

        </td>
    </tr>
        `;
        projectsDiv.innerHTML += projectRow;
    });
    

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

  function testbutton() {
    console.log("test");
  }










