document.getElementById('getOffices').addEventListener('click', getOffices);

    function getOffices(event){
            event.preventDefault();

            token = window.localStorage.getItem('token');

            fetch('https://politico-api-database.herokuapp.com/api/v2/offices',{
                method: 'GET',
                headers : {
                    Accept: 'application/json',
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer ' + token,
                },
            })
            .then((res) => res.json())
            .then((data) => {
                let result = `<h3 style="margin-left: 10px;"> Office grouped by ID, Category and Name.</h3>`;
                data.offices.forEach(office => {
                    const { office_id, category, name } = office
                    result +=
                        `<div>
                             <table>
                                <tr>
                                    <th>Office ID</th>
                                    <th>Office category name</th>
                                    <th>Office name</th>
                                </tr>
                                <tr>
                                     <td>${office_id}</td>
                                     <td>${category}</td>
                                     <td>${name} </td>
                                </tr>
                             </table>
                          </div>`;
                            document.getElementById('result').innerHTML = result;
                        });
                    }).catch((err)=>console.log(err))
    }