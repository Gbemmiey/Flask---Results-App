function checkPasswords() {
  const p1 = document.getElementById("pwrd1");
  const p2 = document.getElementById("pwrd2");
  const checkMessage = document.getElementById("check-pass");

  if (p1.innerText === p2.innerText) {
    checkMessage.textContent = "Correct";
  } else {
    checkMessage.textContent = "Passwords don't match";
  }
  console.log(checkMessage.textContent);
}
