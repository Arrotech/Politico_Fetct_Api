document.getElementById('postSignup').addEventListener('submit', postSignup);

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

 function postSignup(event){
            event.preventDefault();

            let firstname = document.getElementById('firstname').value;
            let lastname = document.getElementById('lastname').value;
            let email = document.getElementById('email').value;
            let password = document.getElementById('password').value;
            let phoneNumber = document.getElementById('phoneNumber').value;
            let passportUrl = document.getElementById('passportUrl').value;
            let role = document.getElementById('role').value;

            fetch('https://politico-api-database.herokuapp.com/api/v2/auth/signup', {
                method: 'POST',
                headers : {
                	Accept: 'application/json',
                    'Content-Type': 'application/json'
                },
                body:JSON.stringify({firstname:firstname, lastname:lastname, email:email, password:password, phoneNumber:phoneNumber, passportUrl:passportUrl, role:role})
            }).then((res) => res.json())
            .then((data) =>  {

                console.log(data);
                let status = data['status'];
                let message = data['message'];
                if (status === '201'){
                    localStorage.setItem("user", JSON.stringify(data[0]));
                    window.location.replace('user.html');
                }else{
                    raiseError(message);
                }
            })
            .catch((err)=>{
                raiseError("Please check your internet connection and try again!");
                console.log(err);
            })
        }
