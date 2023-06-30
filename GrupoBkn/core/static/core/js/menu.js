$(document).ready(function() {
    $.ajax({
      url: "../../../templates/core/menu.html",
      success: function(data) {
        $("nav").html(data);
      }
    });
  });