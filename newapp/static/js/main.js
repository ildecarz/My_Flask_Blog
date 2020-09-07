const botton = document.querySelectorAll('.btn-primary');

if(botton) {
    const btnArray = Array.from(botton);
    btnArray.forEach((btn) => {
        btn.addEventListener('click', (e) => {
            if(!confirm('seguro que deseas continuar?')) {
                e.preventDefault();
            }
        });
    });
}
