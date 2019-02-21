$(document).ready(function() {

  const BASE_URL = "http://localhost:5000";

  $("div#listContent").load(function(){
    $.get(BASE_URL + "/list", function(data){
      alert(data);
    });
  });
});
