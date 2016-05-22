$("#id_sender").on("keyup change", function() {
  var emailRegex = new RegExp("^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$");
  if (emailRegex.test($(this).val())) {
    changeToValid($(this));
  } else {
    changeToInvalid($(this));
  }
});

$("#id_subject, #id_message").on("keyup change", function() {
  if ($(this).val() === "") {
    changeToInvalid($(this));
  } else {
    changeToValid($(this));
  }
});

function changeToValid(element) {
  if (element.hasClass("invalid")) {
    element.removeClass("invalid");
  }
  if (!element.hasClass("valid")) {
    element.addClass("valid");
  }
}

function changeToInvalid(element) {
  if (element.hasClass("valid")) {
    element.removeClass("valid");
  }
  if (!element.hasClass("invalid")) {
    element.addClass("invalid");
  }
}
