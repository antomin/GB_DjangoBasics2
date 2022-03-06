window.onload = () => {
    $('.category-menu').on('click', '.list-group-item', (event) => {
        let elem = event.target;

        $.ajax({
           url: elem.href,
           success: (data) => {
               $('.products-list').html(data.result)
           }
        });

        event.preventDefault();
    });
}