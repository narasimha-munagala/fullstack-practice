// var number = 10;
// var string = "Hello World!!";
// var isGood = true;
// document.getElementById('test').innerHTML = string;
// document.getElementById('test').innerHTML = number * 5;

// if (number == 10) {
//     console.log("Number Equals to 10")
// }
// else {
//     console.log("It's not the required number")
// }

// function listItems() {
//     var items = ['Brand', 'Value', 'Speed']
//     for (var i = 0; i < items.length; i++) {
//         console.log(items[i])
//     }
// }

// listItems();

// document.getElementById('test').addEventListener("click", function() {
//     alert('Event listener listening');
// });
//-------------------------------------------Updated Codex-----------------------------------------------------
// function toggleForm(type) {
//     document.getElementById('loginForm').classList.remove('active');
//     document.getElementById('signupForm').classList.remove('active');
//     document.getElementById('showLogin').classList.remove('active');
//     document.getElementById('showSignUp').classList.remove('active');
//     if(type == 'login') {
//         document.getElementById('loginForm').classList.add('active');
//         document.getElementById('showLogin').classList.add('active');
//     }
//     else {
//         document.getElementById('signupForm').classList.add('active');
//         document.getElementById('showSignUp').classList.add('active');
//     }
// }
// document.getElementById('signupForm').addEventListener('submit', function (e) {
//     e.preventDefault();
//     const pwd = this.password.value;
//     const confirmPwd = this.confirm_password.value;
//     if (pwd != confirmPwd) {
//         alert("❌ Passwords do not match. Please try again.");
//         return;
//     }
//     alert("✅ Signup successful! (Dummy message for learning)");
//     this.reset(); // optional: reset form fields
// });
// document.getElementById('loginForm').addEventListener('submit', function (e) {
//     e.preventDefault(); // prevent page refresh
//     alert("✅ Login successful!")
// });
//--------------------------------Updated Codex----------------------------------------------------------------

function toggleForm(formType) {
    if (formType == 'login') {
        window.location.href = '/login';
    }
    else if (formType == 'signup') {
        window.location.href = '/signup';
    }
}