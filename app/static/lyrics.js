

  

  var jsonob = {
    "access_token": localStorage.getItem("access_token"),
    "spotify_track_id": "6TwfdLbaxTKzQi3AgsZNzx"
  }

  console.log(jsonob)

  $.ajax({
        type: "POST",
        url: "http://127.0.0.1:5000/lyrics/lyrics_page",
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
