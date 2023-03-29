/**
 * Adds a mouseleave event listener to each card
 * When user moves outside card text will scroll back to original position
 * This is timed to 3 seconds
 */
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