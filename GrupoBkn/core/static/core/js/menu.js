$(document).ready(function() {
    $.ajax({
      url: "{% templates core/menu %}",
      success: function(data) {
        $("nav").html(data);
      }
    });
  });