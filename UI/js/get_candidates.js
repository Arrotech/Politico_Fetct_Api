document.getElementById('getCandidates').addEventListener('click', getCandidates);

    function callToast() {

      var x = document.getElementById("snackbar");
      x.className = "show";
      setTimeout(function(){ x.className = x.className.replace("show", ""); }, 3000);
    }

    function onSuccess(msg){

        document.getElementById('snackbar').innerText = msg
        callToast();
    }

    function raiseError(msg){

        document.getElementById('snackbar').innerText = msg
        callToast();
    }


    function getCandidates(event){
            event.preventDefault();

            token = window.localStorage.getItem('token');


            fetch('https://politico-api-database.herokuapp.com/api/v2/candidates',{
                method: 'GET',
                headers : {
                    Accept: 'application/json',
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer ' + token,
                },
            })
            .then((res) => res.json())
            .then((data) => {
                let display = `<h3 style="margin-left: 10px;"> Candidates grouped by ID, Office, Name, and Party.</h3>`;
                data.users.forEach(user => {
                    const { candidate_id, office, candidate, party } = user
                    display +=
                        `<div>
                             <table>
                                <tr>
                                    <th>Candidate ID</th>
                                    <th>Office ID</th>
                                    <th>User ID</th>
                                    <th>Party ID</th>
                                </tr>
                                <tr>
                                     <td>${candidate_id}</td>
                                     <td>${office}</td>
                                     <td>${candidate}</td>
                                     <td>${party}</td>
                                </tr>
                             </table>
                          </div>`;
                            document.getElementById('display').innerHTML = display;
                        });
                    })
            .catch((err)=>{
                raiseError("Please check your internet connection and try again!");
                console.log(err);
            })
    }