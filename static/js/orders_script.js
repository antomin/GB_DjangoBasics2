'use strict';

window.onload = () => {
    let TOTAL_FORMS = parseInt($('input[name="orderitems-TOTAL_FORMS"]').val());
    let price, quantity, orderitem_num, orderitem_quantity, delta_quantity, delta_cost;
    let total_cost = parseFloat($('.order_total_cost').text()) || 0;
    let total_quantity = parseInt($('.order_total_quantity').text()) || 0;
    let price_arr = [];
    let quantity_arr = [];

    for (let i = 0; i < TOTAL_FORMS; i++) {
        price = parseFloat($('.orderitems-' + i + '-price').text());
        quantity = parseInt($('input[name="orderitems-' + i + '-quantity"]').val());

        price_arr[i] = price ? price : 0;
        quantity_arr[i] = quantity;
    }

    if (!total_quantity) {
        for (let i = 0; i < TOTAL_FORMS; i++) {
            total_quantity += quantity_arr[i];
            total_cost += price_arr[i] * quantity_arr[i];
        }
        $('.order_total_cost').html(Number(total_cost.toFixed(2)).toString());
        $('.order_total_quantity').html(total_quantity.toString());
    }


    $('.order_form').on('change', 'input[type="number"]', ({target}) => {
        orderitem_num = parseInt(target.name.replace('orderitems-', '').replace('-quantity', ''));
        if (price_arr[orderitem_num]) {
            orderitem_quantity = parseInt(target.value);
            delta_quantity = orderitem_quantity - quantity_arr[orderitem_num];
            quantity_arr[orderitem_num] = orderitem_quantity;
            orderSummaryUpdate(price_arr[orderitem_num], delta_quantity);
        }
    });


    // $('.order_form').on('change', 'input[type="checkbox"]', ({target}) => {
    //     orderitem_num = parseInt((target.name.replace('orderitems-', '').replace('-DELETE', '')));
    //     delta_quantity = quantity_arr[orderitem_num] * (target.checked ? -1 : 1);
    //     orderSummaryUpdate(price_arr[orderitem_num], delta_quantity);
    // });


    function orderSummaryUpdate(orderitem_price, delta_quantity) {
        delta_cost = orderitem_price * delta_quantity;

        total_cost = Number((total_cost + delta_cost).toFixed(2))
        total_quantity = total_quantity + delta_quantity;

        $('.order_total_cost').html(total_cost.toString());
        $('.order_total_quantity').html(total_quantity.toString());
    }


    // Django-dinamic-formset
    $('.formset_row').formset({
        addText: 'добавить продукт',
        addCssClass: 'btn btn-warning btn-round form-control w-25 my-2 last',
        deleteText: 'X',
        deleteCssClass: 'btn btn-danger btn-round form-control',
        prefix: 'orderitems',
        removed: deleteOrderItem
    });

    function deleteOrderItem(row) {
        let target_name = row[0].querySelector('input[type="number"]').name;
        orderitem_num = parseInt((target_name.replace('orderitems-', '').replace('-DELETE', '')));
        delta_quantity = -quantity_arr[orderitem_num];
        orderSummaryUpdate(price_arr[orderitem_num], delta_quantity)
    }

    // Ajax price add

}