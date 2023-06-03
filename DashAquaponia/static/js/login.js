var formEntrar = document.querySelector('#entrar')
var formCadastrar = document.querySelector('#cadastrar')
var btnColor = document.querySelector('.btnColor')

document.querySelector('#btnEntrar')
  .addEventListener('click', () => {
    formEntrar.style.left = "25px"
    formCadastrar.style.left = "450px"
    btnColor.style.left = "0px"
})

document.querySelector('#btnCadastrar')
  .addEventListener('click', () => {
    formEntrar.style.left = "-450px"
    formCadastrar.style.left = "25px"
    btnColor.style.left = "110px"
})