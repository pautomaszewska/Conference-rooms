document.addEventListener('DOMContentLoaded', function () {
    var box = document.querySelectorAll('.link');

    for (var i = 0; i < box.length; i++) {
        box[i].addEventListener('mouseover', function () {
            this.style.backgroundColor = '#6d479b';
            this.firstElementChild.style.color = 'white';
        });
        box[i].addEventListener('mouseleave', function () {
            this.style.backgroundColor = ''
            this.firstElementChild.style.color = '';

        });
    }
})




