const LOGIN_CONTAINER = document.querySelector('.login_container');
const REGISTER_CONTAINER = document.querySelector('.register_container');
const BTN_SHOW_REGISTER = document.getElementById('btn_show_register');
const BTN_SHOW_LOGIN = document.getElementById('btn_show_login');

BTN_SHOW_REGISTER.addEventListener('click', (e)=>{
    e.preventDefault();
    LOGIN_CONTAINER.classList.add('animated');
    setTimeout(()=>{
        LOGIN_CONTAINER.classList.add('display_none');
        REGISTER_CONTAINER.classList.remove('display_none');
        REGISTER_CONTAINER.classList.remove('animated');
    }, 700)
});

BTN_SHOW_LOGIN.addEventListener('click', (e)=>{
    e.preventDefault();
    REGISTER_CONTAINER.classList.add('animated');
    setTimeout(()=>{
        REGISTER_CONTAINER.classList.add('display_none');
        LOGIN_CONTAINER.classList.remove('display_none');
        LOGIN_CONTAINER.classList.remove('animated');
    }, 700)

});

