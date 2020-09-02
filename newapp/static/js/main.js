const boton = document.querySelectorAll('.btn-primary');

if(boton) {
    const btnArray = Array.from(boton);
    btnArray.forEach((btn) => {
        btn.addEventListener('click', (e) => {
            if(!confirm('seguro que deseas continuar?')) {
                e.preventDefault();
            }
        });
    });
}