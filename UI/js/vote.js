document.getElementById('newVote').addEventListener('submit', newVote);

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
            .then((data) =>  {
                console.log(data);
                let status = data['status'];
                let message = data['message'];
                if (status === '201'){
                    onSuccess('Voted successfully!');
                }else{
                    raiseError(message);
                }
            })
            .catch((err)=>{
                raiseError("Please check your internet connection and try again!");
                console.log(err);
            })
        }
