/**
 * When closing the modal the iframe src is removed to stop video playing in background
 */
document.addEventListener('DOMContentLoaded', function () {
    var modal = document.getElementById('exampleModal');
    var iframe = document.getElementById('trailer');

    modal.addEventListener('hide.bs.modal', function (event) {
        if (event.target === modal) {
            iframe.src = iframe.src;
        }
    });
});