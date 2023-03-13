var signupForm = document.getElementById("signup-form");
var loginForm = document.getElementById("login-form");
var signupBtn = document.getElementById("signup-btn");
var loginBtn = document.getElementById("login-btn");

signupBtn.addEventListener("click", () => {
  signupBtn.classList.add("btn-auth");
  loginBtn.classList.remove("btn-auth");
  signupForm.style.display = "block";
  loginForm.style.display = "none";
});

loginBtn.addEventListener("click", () => {
  loginBtn.classList.add("btn-auth");
  signupBtn.classList.remove("btn-auth");
  loginForm.style.display = "block";
  signupForm.style.display = "none";
});
