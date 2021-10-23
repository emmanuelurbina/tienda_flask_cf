function notificationSwal(titleText, text, icon, confirmBtn){
    Swal.fire({
        titleText: titleText,
        text: text,
        icon: icon,
        confirmBtn: confirmBtn
    })
}