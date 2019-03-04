document.getElementById('postSignup').addEventListener('submit', postSignup);

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
                let user = data['user'];
                if (user.email === 'admin@admin.com'){
                    localStorage.setItem("user", JSON.stringify(data[0]));
                    window.location.replace('admin.html');
                }else{
                    localStorage.setItem("user", JSON.stringify(data[0]));
                    window.location.replace('user.html');
                }

            })
            .catch((err)=>console.log(err))
        }
