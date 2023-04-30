async function send(e,form) {
    const response = await fetch(form.action, {method:'post', redirect:'manual', body: new FormData(form)});
  
    console.log(response);
    e.preventDefault();
  }

// Register User

function registerUser() {
    var formdata = new FormData();
    formdata.append("username", "pita");
    formdata.append("password", "password@123");
    formdata.append("email", "pita@email.com");

    var requestOptions = {
        method: 'POST',
        body: formdata,
        redirect: 'follow'
    };

    fetch("http://localhost:8000/api/auth/register/", requestOptions)
        .then(response => response.text())
        .then(result => console.log(result))
        .catch(error => console.log('error', error));
}


// Login user 
async function loginUser() {

    const form = document.getElementById("login-form");
    const submitter = document.querySelector("button[value=submit]");
    var formData = new FormData(form, submitter);

    var username = formData.get('username');
    var password = formData.get('password');

    var formdata = {
        username: username,
        password: password,
    }

    var requestOptions = {
        method: 'POST',
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(formdata),
        redirect: 'follow'
    };


    const response = await fetch("http://localhost:8000/api/auth/login/", requestOptions)
        .then(response => response.text())
        .then(result => console.log(result))
        .catch(error => console.log('error', error));

    const data = response;
    return data
}

// Logout authenticated user
function logoutUser() {
    var myHeaders = new Headers();
    myHeaders.append("Authorization", "Token 09d9345a28cddc912048518803fde4d10480e2f2e3c1620bd8d2fb4dfadc41a4");

    var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        redirect: 'follow'
    };

    fetch("http://localhost:8000/api/auth/logout/", requestOptions)
        .then(response => response.text())
        .then(result => console.log(result))
        .catch(error => console.log('error', error));
}
