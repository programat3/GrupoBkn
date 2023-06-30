$(document).ready(function() {
    $.ajax({
      url: "../../../templates/core/footer.html",
      success: function(data) {
        $("footer").html(data);
      }
    });
  });