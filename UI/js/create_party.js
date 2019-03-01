document.getElementById('createParty').addEventListener('submit', createParty);

    function createParty(event){
            event.preventDefault();

            let name = document.getElementById('name').value;
            let hqAddress = document.getElementById('hqAddress').value;
            let logoUrl = document.getElementById('logoUrl').value;

            fetch('https://politico-api-database.herokuapp.com/api/v2/parties', {
                method: 'POST',
                headers : {
                	Accept: 'application/json',
                    'Content-Type': 'application/json',
                },
                body:JSON.stringify({name:name, hqAddress:hqAddress, logoUrl:logoUrl})
            }).then((res) => res.json())
            .then((data) =>  console.log(data))
            .catch((err)=>console.log(err))
        }
