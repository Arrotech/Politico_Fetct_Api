document.getElementById('getResults').addEventListener('click', getResults);

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

    function getResults(event){
            event.preventDefault();

            token = window.localStorage.getItem('token');


            fetch('https://politico-api-database.herokuapp.com/api/v2/vote',{
                method: 'GET',
                headers : {
                    Accept: 'application/json',
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer ' + token,
                },
            })
            .then((res) => res.json())
            .then((data) => {
                let disp = `<h3 style="margin-left: 10px;"> Results grouped by Candidate ID and count.</h3>`;
                data.votes.forEach(vote => {
                    const { candidate, count } = vote
                    disp +=
                        `<div>
                             <table>
                                <tr>
                                    <th>Candidate ID</th>
                                    <th>Votes</th>
                                </tr>
                                <tr>
                                     <td>${candidate}</td>
                                     <td>${count}</td>  
                                </tr>
                             </table>
                          </div>`;
                            document.getElementById('disp').innerHTML = disp;
                        });
                    })
            .catch((err)=>{
                raiseError("Please check your internet connection and try again!");
                console.log(err);
            })
    }