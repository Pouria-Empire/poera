//get elements:
const name_ = document.getElementById("name");
const lastName = document.getElementById("last-name");
const password = document.getElementById("password");
const passwordConfirm = document.getElementById("password-confirm");
const email = document.getElementById("email");
const phone = document.getElementById("phone");
let isAllValid = false;
const submitBtn = document.getElementsByClassName('btn-primary');
//adding deactive
for(success of document.getElementsByClassName('alert-success')){
  success.classList.add('deactive')
}
for(success of document.getElementsByClassName('alert-danger')){
  success.classList.add('deactive')
}
//stop login form to refresh
var form = document.getElementById("login_form");
form.addEventListener('submit',handleForm)
function handleForm(event) { event.preventDefault(); } 

document.addEventListener("DOMContentLoaded", function() {
    var elements = document.getElementsByTagName("INPUT");
    for (var i = 0; i < elements.length; i++) {
        elements[i].oninvalid = function(e) {
            e.target.setCustomValidity("");
            if (!e.target.validity.valid) {
                e.target.setCustomValidity("please fill out the form properly");
            }
        };
        elements[i].oninput = function(e) {
            e.target.setCustomValidity("");
        };
    }
})


submitBtn[0].addEventListener("click",e=>{
  console.log('test')
  passwordValid();
  let a = document.getElementsByClassName('alert-success')[0]
  let b = document.getElementsByClassName('alert-danger')[0]
  if(isAllValid){
    a.classList.toggle('deactive')
    var form = document.getElementById("myform");
    function handleForm(event) { event.preventDefault(); } 
    form.addEventListener('submit', handleForm);
    window.setTimeout(function(){location.reload()},3000)
  }else{
    b.classList.toggle('deactive')
  }
})

document.getElementById('command_button').addEventListener('click',e=>{
  let a = document.getElementsByClassName('alert-success')[1]
  if(validateEmail(document.getElementById('forget_email').value.trim())){
    a.classList.toggle('deactive')
  }
  empty()
})
const nameValid = (e) => {
  let a = name_.nextElementSibling.nextElementSibling;
  if (name_.value.trim().length < 5) {
    runInvalid(a, name_);
    isAllValid = false;
  } else {
    runValid(a, name_);
    isAllValid = true;
  }
};

const lastNameValid = (e) => {
  let a = lastName.nextElementSibling.nextElementSibling;
  if (lastName.value.trim().length < 5) {
    runInvalid(a, lastName);
    isAllValid = false;
  } else {
    runValid(a, lastName);
    isAllValid = true;
  }
  nameValid();
};

function validateEmail(email) {
  const re =
    /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  return re.test(String(email).toLowerCase());
}

const emailValid = (e) => {
  let a = email.nextElementSibling.nextElementSibling;
  if (!validateEmail(email.value.trim())) {
    runInvalid(a, email);
    isAllValid = false;
  } else {
    runValid(a, email);
    isAllValid = true;
  }
};

const phoneValid = (e) => {
  let a = phone.nextElementSibling.nextElementSibling;
  if (phone.value.trim().length < 10 || phone.value.trim().length > 10) {
    runInvalid(a, phone);
    console.log("sth");
    isAllValid = false;
  } else {
    runValid(a, phone);
    isAllValid = true;
  }
  lastNameValid();
  emailValid();
};
function hasNumber(myString) {
  return /\d/.test(myString);
}
const passwordValid = (e) => {
  let a = password.nextElementSibling.nextElementSibling;
  let b = passwordConfirm.nextElementSibling.nextElementSibling;
  if (
    password.value.trim().length < 6 ||
    (!hasNumber(password.value.trim())) ||
    password.value.trim() !== passwordConfirm.value.trim()
  ) {
    runInvalid(a, password);
    runInvalid(b, passwordConfirm);
    isAllValid = false;

  } else {
    runValid(a, password);
    runValid(b, passwordConfirm);
    isAllValid = true;
    
  }
  phoneValid();
};

phone.addEventListener("click", emailValid);
lastName.addEventListener("click", nameValid);
password.addEventListener("click", lastNameValid);
email.addEventListener("click", phoneValid);
passwordConfirm.addEventListener('click',passwordValid);
password.addEventListener('click',passwordValid);


function runValid(a, element) {
  element.classList.remove("invalid");
  element.classList.add("valid");
  a.classList.remove("deactive");
  a.classList.add("active");
}

function runInvalid(a, element) {
  element.classList.remove("valid");
  element.classList.add("invalid");
  a.classList.add("deactive");
  a.classList.remove("active");
}
function empty(){
    for(a of document.querySelectorAll('input')){
        a.value = "";
        a.classList.remove('valid');
        a.classList.remove('invalid');
        a.classList.add('refreshed');
    }
    for(a of document.querySelectorAll('.valid-feedback')){
        a.classList.remove('active');
        a.classList.add('deactive');
    }
};

for(b of document.querySelectorAll(".d-inline a")){
  b.addEventListener('click',e=>{
    empty();
  });
}

document.getElementById('refreshBtn').addEventListener('click', empty);
// Fetch all the forms we want to apply custom Bootstrap validation styles to
var forms = document.querySelectorAll(".needs-validation");

// Loop over them and prevent submission
// Array.prototype.slice.call(forms).forEach(function (form) {
//   form.addEventListener(
//     "submit",
//     function (event) {
//       if (!form.checkValidity()) {
//         event.preventDefault();
//         event.stopPropagation();
//       }

//       form.classList.add("was-validated");
//     },
//     false
//   );
// });
