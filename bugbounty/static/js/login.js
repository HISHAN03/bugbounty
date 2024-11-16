const signInButton = document.getElementById('signIn');
const signUpButton = document.getElementById('signUp');
const container = document.getElementById('container');

if (signInButton && signUpButton && container) {
    signUpButton.addEventListener('click', () => {
        container.classList.add('right-panel-active');
    });

    signInButton.addEventListener('click', () => {
        container.classList.remove('right-panel-active');
    });
}

document.addEventListener('DOMContentLoaded', () => {
    const loginBtn = document.getElementById('loginBtn');
    const signupBtn = document.getElementById('signupBtn');
    const loginForm = document.getElementById('loginForm');
    const signupForm = document.getElementById('signupForm');

    // Function to switch forms
    function switchForm(formType) {
        if (formType === 'login') {
            loginForm.style.display = 'block';
            signupForm.style.display = 'none';
            loginBtn.classList.add('active');
            signupBtn.classList.remove('active');
        } else if (formType === 'signup') {
            loginForm.style.display = 'none';
            signupForm.style.display = 'block';
            signupBtn.classList.add('active');
            loginBtn.classList.remove('active');
        }
    }

    // Event listeners for buttons
    loginBtn.addEventListener('click', () => switchForm('login'));
    signupBtn.addEventListener('click', () => switchForm('signup'));
});
