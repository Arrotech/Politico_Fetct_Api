document.getElementById('logout').addEventListener('click', logout);

    function on_logout(){

        localStorage.clear();

        window.location.replace('register.html')
    }