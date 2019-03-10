document.getElementById('showInterest').addEventListener('submit', showInterest);

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
                let message = data['message'];
                if (status === '201'){
                    onSuccess('User promoted successfully!');
                }else{
                    raiseError(message);
                }
            })
            .catch((err)=>{
                raiseError("Please check your internet connection and try again!");
                console.log(err);
            })
        }
