document.getElementById('deleteOffice').addEventListener('submit', deleteOffice);


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

    function deleteOffice(event){
            event.preventDefault();

            token = window.localStorage.getItem('token');

            let office_id = document.getElementById('office_id').value;

            fetch('https://politico-api-database.herokuapp.com/api/v2/offices/' + office_id, {
                method: 'DELETE',
                path: office_id,
                headers : {
                	Accept: 'application/json',
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer ' + token,
                },
                body:JSON.stringify({office_id:office_id})
            }).then((res) => res.json())
            .then((data) =>  {
                console.log(data);
                let status = data['status'];
                let message = data['message'];
                if (status === '200'){
                    onSuccess('Office deleted successfully!');
                }else{
                    raiseError(message);
                }
            })
            .catch((err)=>{
                raiseError("Please check your internet connection and try again!");
                console.log(err);
            })
        }

