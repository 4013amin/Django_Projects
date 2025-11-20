document.addEventListener('DOMContentLoaded', function () {
    const loginForm = document.getElementById('login-form');
    const registerForm = document.getElementById('register-form');
    const otpForm = document.getElementById('otp-form');

    const showRegisterLink = document.getElementById('show-register');
    const showLoginLink = document.getElementById('show-login');

    const loginPhoneInput = document.getElementById('login-phone');
    const registerPhoneInput = document.getElementById('register-phone');
    const otpPhoneDisplay = document.getElementById('otp-phone-display');

    showRegisterLink.addEventListener('click', function (e) {
        e.preventDefault();
        loginForm.classList.add('hidden');
        registerForm.classList.remove('hidden');
    });

    showLoginLink.addEventListener('click', function (e) {
        e.preventDefault();
        registerForm.classList.add('hidden');
        loginForm.classList.remove('hidden');
    });

    loginForm.querySelector('form').addEventListener('submit', function (e) {
        e.preventDefault();
        const phone = loginPhoneInput.value;
        if (phone) {
            otpPhoneDisplay.textContent = phone;
            loginForm.classList.add('hidden');
            otpForm.classList.remove('hidden');
        }
    });

    registerForm.querySelector('form').addEventListener('submit', function (e) {
        e.preventDefault();
        const phone = registerPhoneInput.value;
        if (phone) {
            otpPhoneDisplay.textContent = phone;
            registerForm.classList.add('hidden');
            otpForm.classList.remove('hidden');
        }
    });
});
