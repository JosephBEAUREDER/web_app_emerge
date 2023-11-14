$(document).ready(function(){
    console.log("Document is readyyyy");
    $('.project_text').on('change', async function() {
        var newText = $(this).val();
        var projectId = $(this).attr('id');
;


        var colis = {
            'project_id': projectId,
            'new_text': newText,
        };

    // console.log(newText);

        const requete = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(colis)
        };

    var url = '/test_1/edit_project/' + projectId + '/update_project_text/'
    
    const response = await fetch(url, requete);

    const data = await response.json();
    
    });
});