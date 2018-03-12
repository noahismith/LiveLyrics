
var jsonob;
  if (localStorage.getItem("spotify_track_id")) {
    jsonob = {
      "access_token": localStorage.getItem("access_token"),
      "spotify_track_id": localStorage.getItem("spotify_track_id")
    }

  $.ajax({
        type: "POST",
        url: "http://127.0.0.1:5000/lyrics/lyrics_page",
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        data: JSON.stringify(jsonob, null, '\t')
      })
      .done(function( msg ) {
        console.log(JSON.stringify(msg));
        //TODO print into html
        $('#song-title-input').val(msg.lyric_page.songtitle)
        $('#lyrics-input').val(msg.lyric_page.lyrics)
        $('#spotify-track-id-input').val(msg.lyric_page.spotify_track_id)
        $('#timestamps-input').val(msg.lyric_page.timestamps)
        
      })
      .fail(function( jqXHR, textStatus ) {
        alert( "Request failed: " + textStatus );
      //});

      
    })

  } else {
    jsonob = {
      "access_token": localStorage.getItem("access_token"),
      "spotify_track_id": null
    }
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
      //TODO print into html
      
    })
    .fail(function( jqXHR, textStatus ) {
      alert( "Request failed: " + textStatus );
    //});

    
  })

$( '#songEditForm').submit(function(event) {
  event.preventDefault()

  var $form = $( this ),
    songtitlef = $form.find( "input[name='songtitle']" ).val(),
    lyricsf = $form.find( "input[name='lyrics']" ).val(),
    spotify_track_idf = $form.find( "input[name='spotify_track_id']" ).val(),
    timestampsf = $form.find( "input[name='timestamps']" ).val(),
    urltar = $form.attr( "action" );
  
  console.log(localStorage)
  var jsonob = {
    "songtitle" : songtitlef,
    "lyrics" : lyricsf,
    "spotify_track_id" : spotify_track_idf,
    "timestamps" : timestampsf,
    "access_token": localStorage.getItem("access_token")
  }

  console.log(jsonob)

  $.ajax({
        type: "POST",
        url: "http://127.0.0.1:5000/lyrics/edit",
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