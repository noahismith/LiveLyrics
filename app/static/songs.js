$( '#songsForm').submit(function(event) {
  event.preventDefault()

  var $form = $( this ),
    songf = $form.find( "input[name='song']" ).val(),
    urltar = $form.attr( "action" );
  
  console.log(localStorage)
  var jsonob = {
    "search_string": songf,
    "access_token": localStorage.getItem("access_token")
  }

  console.log(jsonob)

  $.ajax({
        type: "POST",
        url: "http://127.0.0.1:5000/lyrics/search",
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        data: JSON.stringify(jsonob, null, '\t')
    })
    .done(function( msg ) {
      console.log(JSON.stringify(msg));

      
    })
    .fail(function( jqXHR, textStatus ) {
      alert( "Request failed: " + textStatus );
    //});

    
  })
});