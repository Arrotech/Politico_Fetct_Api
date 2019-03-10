document.getElementById('deleteParty').addEventListener('submit', deleteParty);

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

    function deleteParty(event){
            event.preventDefault();

            token = window.localStorage.getItem('token');

            let party_id = document.getElementById('party_id').value;

            fetch('https://politico-api-database.herokuapp.com/api/v2/parties/' + party_id, {
                method: 'DELETE',
                path: party_id,
                headers : {
                	Accept: 'application/json',
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer ' + token,
                },
                body:JSON.stringify({party_id:party_id})
            }).then((res) => res.json())
            .then((data) =>  {
                console.log(data);
                let status = data['status'];
                let message = data['message'];
                if (status === '200'){
                    onSuccess('Party deleted successfully!');
                }else{
                    raiseError(message);
                }
            })
            .catch((err)=>{
                raiseError("Please check your internet connection and try again!");
                console.log(err);
            })
        }

