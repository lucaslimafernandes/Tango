console.log("Carregou!")


// NEW USER

//Show Password
check_passwd = document.querySelector('#show_pwd')
password = document.querySelectorAll('.password')


check_passwd.addEventListener('change', () => {

    if (check_passwd.checked){
        password[0].type = 'text'
        password[1].type = 'text'
    } else {
        password[0].type = 'password'
        password[1].type = 'password'
    }


})

//Password confirm

function pass_check_func(){
    if (password[0].value === password[1].value){
        check2passwd.style.display = 'none'
    } else {
        check2passwd.style.display = 'block'
    }
}

check2passwd = document.getElementById('check2passwd')

password[0].addEventListener('keyup', () => {
    pass_check_func()
})

password[1].addEventListener('keyup', () => {
    pass_check_func()
})

//https://developer.mozilla.org/pt-BR/docs/Web/HTML/Element/Input/password

