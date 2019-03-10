document.getElementById('getParties').addEventListener('click', getParties);

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

    function getParties(event){
            event.preventDefault();

            token = window.localStorage.getItem('token');


            fetch('https://politico-api-database.herokuapp.com/api/v2/parties',{
                method: 'GET',
                headers : {
                    Accept: 'application/json',
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer ' + token,
                },
            })
            .then((res) => res.json())
            .then((data) => {
                let output = `<h3 style="margin-left: 10px;"> Parties grouped by ID, Name, Headquarters, and Logo.</h3>`;
                data.parties.forEach(party => {
                    const { party_id, name, hqAddress, logoUrl } = party
                    output +=
                        `<div>
                             <table>
                                <tr>
                                    <th>Party ID</th>
                                    <th>Party Name</th>
                                    <th>Party Headquarters</th>
                                    <th>Party Logo</th>
                                </tr>
                                <tr>
                                     <td>${party_id}</td>
                                     <td>${name}</td>
                                     <td>${hqAddress}</td>
                                     <td>${logoUrl}</td>
                                </tr>
                             </table>
                          </div>`;
                            document.getElementById('output').innerHTML = output;
                        });
                    })
            .catch((err)=>{
                raiseError("Please check your internet connection and try again!");
                console.log(err);
            })
    }