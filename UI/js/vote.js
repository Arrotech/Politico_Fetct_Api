document.getElementById('newVote').addEventListener('submit', newVote);

    function newVote(event){
            event.preventDefault();

            token = window.localStorage.getItem('token');

            let createdBy = document.getElementById('createdBy').value;
            let office = document.getElementById('office').value;
            let candidate = document.getElementById('candidate').value;

            fetch('https://politico-api-database.herokuapp.com/api/v2/vote', {
                method: 'POST',
                headers : {
                	Accept: 'application/json',
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer ' + token,
                },
                body:JSON.stringify({createdBy:createdBy, office:office, candidate:candidate})
            }).then((res) => res.json())
            .then((data) =>  console.log(data))
            .catch((err)=>console.log(err))
        }
