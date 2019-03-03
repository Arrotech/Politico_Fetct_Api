document.getElementById('editOffice').addEventListener('submit', editOffice);

    function editOffice(event){
            event.preventDefault();

            token = window.localStorage.getItem('token');

            let office_id = document.getElementById('office_id').value;
            let category = document.getElementById('category').value;
            let name = document.getElementById('name').value;

            fetch('https://politico-api-database.herokuapp.com/api/v2/offices/' + office_id, {
                method: 'PUT',
                path: office_id,
                headers : {
                	Accept: 'application/json',
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer ' + token,
                },
                body:JSON.stringify({office_id:office_id, category:category, name:name})
            }).then((res) => res.json())
            .then((data) =>  {
                console.log(data);
            })
            .catch((err)=>console.log(err))
        }

