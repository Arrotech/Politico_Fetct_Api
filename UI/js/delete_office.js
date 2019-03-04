document.getElementById('deleteOffice').addEventListener('submit', deleteOffice);

    function deleteOffice(event){
            event.preventDefault();

            token = window.localStorage.getItem('token');

            let office_id = document.getElementById('office_id').value;

            fetch('https://politico-api-database.herokuapp.com/api/v2/offices/' + office_id, {
                method: 'DELETE',
                path: office_id,
                headers : {
                	Accept: 'application/json',
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer ' + token,
                },
                body:JSON.stringify({office_id:office_id})
            }).then((res) => res.json())
            .then((data) =>  {
                console.log(data);
                let status = data['status'];
                if (status === '200'){
                    window.location.reload();
                }else{
                    window.location.replace('index.html');
                }
            })
            .catch((err)=>console.log(err))
        }

