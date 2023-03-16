document.addEventListener('DOMContentLoaded', function () {
    let cards = document.querySelectorAll('.card');

    cards.forEach(function (card) {
        let timeoutId;

        card.addEventListener('mouseleave', function () {
            clearTimeout(timeoutId);

            timeoutId = setTimeout(function () {
                card.querySelector('.card-body').scrollTo({
                    top: 0,
                    behavior: 'smooth'
                });
            }, 3000);
        });
    });
});