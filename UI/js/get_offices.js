document.getElementById('getOffices').addEventListener('click', getOffices);

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

    function getOffices(event){
            event.preventDefault();

            token = window.localStorage.getItem('token');


            fetch('https://politico-api-database.herokuapp.com/api/v2/offices',{
                method: 'GET',
                headers : {
                    Accept: 'application/json',
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer ' + token,
                },
            })
            .then((res) => res.json())
            .then((data) => {
                let result = `<h3 style="margin-left: 10px;"> Office grouped by ID, Category and Name.</h3>`;
                data.offices.forEach(office => {
                    const { office_id, category, name } = office
                    result +=
                        `<div>
                             <table>
                                <tr>
                                    <th>Office ID</th>
                                    <th>Office category name</th>
                                    <th>Office name</th>
                                </tr>
                                <tr>
                                     <td>${office_id}</td>
                                     <td>${category}</td>
                                     <td>${name} </td>
                                </tr>
                             </table>
                          </div>`;
                            document.getElementById('result').innerHTML = result;
                        });
                    })
            .catch((err)=>{
                raiseError("Please check your internet connection and try again!");
                console.log(err);
            })
    }