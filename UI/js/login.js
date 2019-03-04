document.getElementById('postLogin').addEventListener('submit', postLogin);

    function postLogin(event){
            event.preventDefault();

            let email = document.getElementById('email').value;
            let password = document.getElementById('password').value;

            fetch('https://politico-api-database.herokuapp.com/api/v2/auth/login', {
                method: 'POST',
                headers : {
                	Accept: 'application/json',
                    'Content-Type': 'application/json'
                },
                body:JSON.stringify({email:email, password:password})
            }).then((res) => res.json())
            .then((data) =>  {

                console.log(data);
                let user = data['user'];
                if (user.email === 'admin@admin.com'){
                    localStorage.setItem('token', data.token);
                    
                    window.location.replace('admin.html');
                }else{
                    localStorage.setItem('token', data.token);
                    window.location.replace('user.html');
                }
            })
            .catch((err)=>console.log(err))
        }


