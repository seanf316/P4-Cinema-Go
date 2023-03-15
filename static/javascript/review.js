document.addEventListener('DOMContentLoaded', function () {
    let cards = document.querySelectorAll('.card');

    cards.forEach(function (card) {
        card.addEventListener('mouseleave', function () {
            card.querySelector('.card-body').scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
        card.addEventListener('touchend', function () {
            card.querySelector('.card-body').scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    });
});