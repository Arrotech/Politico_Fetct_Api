document.getElementById('editParty').addEventListener('submit', editParty);

    function editParty(event){
            event.preventDefault();

            token = window.localStorage.getItem('token');

            let party_id = document.getElementById('party_id').value;
            let name = document.getElementById('name').value;
            let hqAddress = document.getElementById('hqAddress').value;
            let logoUrl = document.getElementById('logoUrl').value;

            fetch('https://politico-api-database.herokuapp.com/api/v2/parties/' + party_id, {
                method: 'PUT',
                path: party_id,
                headers : {
                	Accept: 'application/json',
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer ' + token,
                },
                body:JSON.stringify({party_id:party_id, name:name, hqAddress:hqAddress, logoUrl:logoUrl})
            }).then((res) => res.json())
            .then((data) =>  {
                console.log(data);
            })
            .catch((err)=>console.log(err))
        }

