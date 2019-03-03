document.getElementById('getResults').addEventListener('click', getResults);

    function getResults(event){
            event.preventDefault();

            token = window.localStorage.getItem('token');


            fetch('https://politico-api-database.herokuapp.com/api/v2/vote',{
                method: 'GET',
                headers : {
                    Accept: 'application/json',
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer ' + token,
                },
            })
            .then((res) => res.json())
            .then((data) => {
                let show = `<h3 style="margin-left: 10px;"> Results grouped by Candidate ID and count.</h3>`;
                data.office.forEach(off => {
                    const { candidate, count } = off
                    show +=
                        `<div>
                             <table>
                                <tr>
                                    <th>Candidate ID</th>
                                    <th>Votes</th>
                                </tr>
                                <tr>
                                     <td>${candidate}</td>
                                     <td>${count}</td>  
                                </tr>
                             </table>
                          </div>`;
                            document.getElementById('show').innerHTML = counts;
                        });
                    }).catch((err)=>console.log(err))
    }