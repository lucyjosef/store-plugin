window.addEventListener('load', function() {

  options.username.value = localStorage.username;

  options.username.onchange = function() {
    localStorage.username = options.username.value;
  };
});
