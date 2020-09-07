const button = document.querySelectorAll('.btn-primary');

if(button) {
    const btnArray = Array.from(button);
    btnArray.forEach((btn) => {
        btn.addEventListener('click', (e) => {
            if(!confirm('seguro que deseas continuar?')) {
                e.preventDefault();
            }
        });
    });
}
