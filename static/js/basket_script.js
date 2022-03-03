window.onload = () => {
    $('.basket-block').on('change', 'input[type="number"]', (event) => {
        let elem = event.target;
        console.log(elem.name)
        console.log(elem.value)

        $.ajax({
            url: '/basket/edit/' + elem.name + '/' + elem.value + '/',
            success: (data) => {
                $('.basket-block').html(data.result)
            }
        });

        event.preventDefault();
    });
}