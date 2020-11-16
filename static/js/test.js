(function ($) {
    $(document).ready(function () {

        $("#createTest").modalForm({
            formURL: "{% url 'create_test' %}",
            successURL: "{% url 'success_view' %}"
        });

    });
})(jQuery);

