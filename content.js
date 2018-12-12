// const BASE_URL = "http://localhost:5000";

// function getLists() {
//   xhttp.open("GET", BASE_URL + "/list", true);
//   xhttp.send();
// }
$(document).ready(function() {
  debugger;
  const BASE_URL = "http://localhost:5000"
  $("div#listContent").load(function(){
    $.get(BASE_URL + "/list", function(data){
      alert(data);
    });
  });
});
