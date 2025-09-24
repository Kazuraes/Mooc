document.addEventListener('DOMContentLoaded', () => {
    const button = document.querySelector('.button')
    const bouton = document.querySelector('.bouton')
    const ouvriere = document.querySelector('.creer_une_page_html')
    bouton.addEventListener('click', () => {
        ouvriere.style.display = 'flex'
        button.style.display = 'block'
})
   button.addEventListener('click', () => {
    ouvriere.style.display = 'none'
    button.style.display = 'none'
   })
})
