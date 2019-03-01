document.getElementById('deleteParty').addEventListener('submit', deleteParty);

    function deleteParty(event){
            event.preventDefault();

            token = window.localStorage.getItem('token');

            let party_id = document.getElementById('party_id').value;

            fetch('https://politico-api-database.herokuapp.com/api/v2/parties/' + party_id, {
                method: 'DELETE',
                path: party_id,
                headers : {
                	Accept: 'application/json',
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer ' + token,
                },
                body:JSON.stringify({party_id:party_id})
            }).then((res) => res.json())
            .then((data) =>  {
                console.log(data);
            })
            .catch((err)=>console.log(err))
        }

