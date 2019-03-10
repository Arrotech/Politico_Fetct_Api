document.getElementById('createParty').addEventListener('submit', createParty);

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

    function createParty(event){
            event.preventDefault();

            token = window.localStorage.getItem('token');

            let name = document.getElementById('name').value;
            let hqAddress = document.getElementById('hqAddress').value;
            let logoUrl = document.getElementById('logoUrl').value;

            fetch('https://politico-api-database.herokuapp.com/api/v2/parties', {
                method: 'POST',
                headers : {
                	Accept: 'application/json',
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer ' + token,
                },
                body:JSON.stringify({name:name, hqAddress:hqAddress, logoUrl:logoUrl})
            }).then((res) => res.json())
            .then((data) =>  {
                console.log(data);
                let status = data['status'];
                let message = data['message'];
                if (status === '201'){
                    onSuccess('Party created successfully!');
                }else{
                    raiseError(message);
                }
            })
            .catch((err)=>{
                raiseError("Please check your internet connection and try again!");
                console.log(err);
            })
        }

