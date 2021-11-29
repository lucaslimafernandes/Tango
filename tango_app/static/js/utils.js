console.log("Carregou!")

var tlist = document.getElementById('tlist')
var rows = document.getElementsByTagName('tr')

//console.log(rows.length)

/*
CHECKBOX
*/

var check_STARTED = document.getElementById('STARTED')
var check_RESPONSES = document.getElementById('RESPONSES')
var check_CLOSED = document.getElementById('CLOSED')
var marcar = document.getElementById('marcar')
var desmarcar = document.getElementById('desmarcar')


check_STARTED.addEventListener('change', () => {
    for (let i=1; i<rows.length; i++){
        let cels = rows[i].cells[4]
        
        if(cels.textContent == 'STARTED'){
            if(check_STARTED.checked){
                rows[i].style.display = ''
            } else {
                rows[i].style.display = 'none'
            }
        }
    }
})

check_RESPONSES.addEventListener('change', () => {
    for (let i=1; i<rows.length; i++){
        let cels = rows[i].cells[4]
        
        if(cels.textContent == 'RESPONSES'){
            if(check_RESPONSES.checked){
                rows[i].style.display = ''
            } else {
                rows[i].style.display = 'none'
            }
        }
    }
})

check_CLOSED.addEventListener('change', () => {
    for (let i=1; i<rows.length; i++){
        let cels = rows[i].cells[4]
        
        if(cels.textContent == 'CLOSED'){
            if(check_CLOSED.checked){
                rows[i].style.display = ''
            } else {
                rows[i].style.display = 'none'
            }
        }
    }
})

marcar.addEventListener('click', () => {
    check_CLOSED.checked = true
    check_RESPONSES.checked = true
    check_STARTED.checked = true

    for(let i=1; i<rows.length; i++){
        rows[i].style.display = ''
    }
})

desmarcar.addEventListener('click', () => {
    check_CLOSED.checked = false
    check_RESPONSES.checked = false
    check_STARTED.checked = false

    for(let i=1; i<rows.length; i++){
        rows[i].style.display = 'none'
    }
})


// NEW USER

//Show Password
check_passwd = document.querySelector('#show_pwd')
password = document.querySelectorAll('.password')


check_passwd.addEventListener('change', () => {

    if (check_passwd){
        console.log('RRERECC')
    } else {
        console.log('RRRE')
    }


})



//Password confirm
