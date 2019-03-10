document.getElementById('editParty').addEventListener('submit', editParty);

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

    function editParty(event){
            event.preventDefault();

            token = window.localStorage.getItem('token');

            let party_id = document.getElementById('party_id').value;
            let name = document.getElementById('name').value;
            let hqAddress = document.getElementById('hqAddress').value;
            let logoUrl = document.getElementById('logoUrl').value;


            fetch('https://politico-api-database.herokuapp.com/api/v2/parties/' + party_id, {
                method: 'PUT',
                path: party_id,
                headers : {
                	Accept: 'application/json',
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer ' + token,
                },
                body:JSON.stringify({party_id:party_id, name:name, hqAddress:hqAddress, logoUrl:logoUrl})
            }).then((res) => res.json())
            .then((data) =>  {
                console.log(data);
                let status = data['status'];
                let message = data['message'];
                if (status === '200'){
                    onSuccess('Pary updated successfully!');
                }else{
                    raiseError(message);
                }
            })
            .catch((err)=>{
                raiseError("Please check your internet connection and try again!");
                console.log(err);
            })
        }

