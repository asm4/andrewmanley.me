// Clicking on a link in the nav closes the nav
$(".navbar-right").on("click", "li", function () {
  $(".nav-btn.active").removeClass("active");
  $(this).addClass("active");
  $(".collapse").collapse("hide");
});

// Clicking out side of the mobile nav closes the nav
$("html").bind("click", function(e) {
  if ($(e.target).closest(".navbar").length == 0) {
    var opened = $(".navbar-collapse").hasClass("collapse in");
    if (opened == true) {
      $(".navbar-collapse").collapse("hide");
    }
  }
});
