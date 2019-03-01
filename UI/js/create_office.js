document.getElementById('postOffice').addEventListener('submit', postOffice);

    function postOffice(event){
            event.preventDefault();

            token = window.localStorage.getItem('token');

            let category = document.getElementById('category').value;
            let name = document.getElementById('name').value;

            fetch('https://politico-api-database.herokuapp.com/api/v2/offices', {
                method: 'POST',
                headers : {
                	Accept: 'application/json',
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer ' + token,
                },
                body:JSON.stringify({category:category, name:name})
            }).then((res) => res.json())
            .then((data) =>  console.log(data))
            .catch((err)=>console.log(err))
        }
