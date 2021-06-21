$( document ).ready(function() {
    const  api_base_url = 'http://127.0.0.1:8000/';
    let csrf_token = document.getElementsByName('csrfmiddlewaretoken')[0].value; //получим токен защиты от csrf
    $("#fibonachi-search").click(function () {
        let dict = {};
        let fibonachi_input = $("#fibonachi_input").val();
        dict['int_for_search'] = Number(fibonachi_input);
        $.ajax({
            type: 'GET',
            url: api_base_url+'api/findfibonachiint/',
            data: dict,
            dataType: 'json',
            headers:{"X-CSRFToken": csrf_token},
            success: function(response) { // если запрос успешен
                $("#fibonachi_output").val(response.output);
            },
            error: function() {
                alert("Что то пошло не так((");
            }
        });
    });

});