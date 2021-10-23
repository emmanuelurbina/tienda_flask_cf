document.addEventListener("DOMContentLoaded", function () {
    const btnsComprar = document.querySelectorAll(".btnComprar")
    const csrf_token = document.querySelector("input[name='csrf_token']").value
    let isbn = null

    btnsComprar.forEach(btn => {
        btn.addEventListener("click", () => {
            isbn = window.event.target.id
            console.log(window.event.target.id);
            confirmarCompra(isbn, csrf_token)
        })
    })
})




function confirmarCompra(isbn, csrf_token) {
    Swal.fire({
        title: '¿Confirma la compra del libro seleccionado?',
        inputAttributes: {
            autocapitalize: 'off'
        },
        showCancelButton: true,
        confirmButtonText: 'Comprar',
        showLoaderOnConfirm: true,
        preConfirm: async () => {
            // console.log(window.origin);
            return await fetch('/comprar_libro', {
                method: 'POST',
                mode: 'same-origin',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRF-TOKEN': csrf_token
                },
                body: JSON.stringify({
                    'isbn': isbn
                })
            })
                .then(response => {
                    if (!response.ok) {
                        notificationSwal('Error', response.statusText, 'error', 'Cerrar');
                    } else {
                        return response.json()
                    }
                })
                .then(data => {
                    if(data.exito){
                        notificationSwal('Exito','Libro comprado', 'success', 'Ok!');
                    }else {
                        notificationSwal('Alerta',data.mensaje, 'warning', 'Ok');
                    }
                })
                .catch(err => {
                    notificationSwal('Error', error, 'error', 'Cerrar');
                })
        },
        allowOutsideClick: () => false,
        allowEscapeKey: () => false
    });

}