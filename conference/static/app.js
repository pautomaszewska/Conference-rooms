document.addEventListener('DOMContentLoaded', function () {
    var box = document.querySelectorAll('.link');
    for (i=0; i<box.length; i++) {
        box.addEventListener('mouseenter', function () {
            this.style.backgroundColor = 'red'
        })
    } console.log(box)
})




