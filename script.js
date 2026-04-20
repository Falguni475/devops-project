function validateForm(){

let name=document.getElementById("name").value;
let email=document.getElementById("email").value;
let password=document.getElementById("password").value;
let confirm=document.getElementById("confirm").value;
let course=document.getElementById("course").value;

if(name==""){
alert("Name cannot be empty");
return false;
}

if(email==""){
alert("Email cannot be empty");
return false;
}

if(password.length<6){
alert("Password must be at least 6 characters");
return false;
}

if(password!=confirm){
alert("Passwords do not match");
return false;
}

if(course==""){
alert("Please select a course");
return false;
}

alert("Registration Successful");
return true;

}