const botao1 = document.getElementById('botao_ler1');

botao1.addEventListener('click', function() {
    var card1 = document.querySelector('.card1');
    
    card1.classList.toggle('active');

    if (card1.classList.contains('active')) {

        return botao1.textContent = 'Ler menos';
    }
    
    botao1.textContent = 'Ler mais';

   
});


// const botao2 = document.getElementById('botao_ler2');

// botao2.addEventListener('click', function() {
//     var card2 = document.querySelector('.card2');
    
//     card2.classList.toggle('active');

//     if (card2.classList.contains('active')) {
//         return botao2.textContent = 'Ler menos';
//     }
    
//     botao2.textContent = 'Ler mais';
// });



// const botao3 = document.getElementById('botao_ler3');

// botao3.addEventListener('click', function() {
//     var card3 = document.querySelector('.card3');
    
//     card3.classList.toggle('active');

//     if (card3.classList.contains('active')) {
//         return botao3.textContent = 'Ler menos';
//     }
    
//     botao3.textContent = 'Ler mais';
// });

