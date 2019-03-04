document.getElementById('showInterest').addEventListener('submit', showInterest);

    function showInterest(event){
            event.preventDefault();

            token = window.localStorage.getItem('token');

            let office = document.getElementById('office').value;
            let candidate = document.getElementById('candidate').value;
            let party = document.getElementById('party').value;

            fetch('https://politico-api-database.herokuapp.com/api/v2/candidates', {
                method: 'POST',
                headers : {
                	Accept: 'application/json',
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer ' + token,
                },
                body:JSON.stringify({office:office, candidate:candidate, party:party})
            }).then((res) => res.json())
            .then((data) =>  {
                console.log(data);
                let status = data['status'];
                if (status === '201'){
                    window.location.reload();
                }else{
                    window.location.replace('index.html');
                }
            })
            .catch((err)=>console.log(err))
        }
