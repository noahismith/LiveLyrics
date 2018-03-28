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
        url: "http://18.188.140.44/lyrics/search",
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        data: JSON.stringify(jsonob, null, '\t')
    })
    .done(function( msg ) {
      console.log(JSON.stringify(msg));

      if (!msg.result) {
        alert("Error! " + msg.error)
      }

      //clearing the list div
      $('.song-list').text("")
      
      msg.lyric_sheets.forEach(function(element) {

        //creating individual elements
        var artistSpan = $('<span/>').text("Artist: " + element.artist)
        var songTitleSpan = $('<span/>')
        var songTitleLink = $('<a/>').text("Song Title: " + element.songtitle).click(function() {

          localStorage.setItem("spotify_track_id", element.spotify_track_id)
          console.log(localStorage)
        })

        songTitleLink.attr('href', "/lyrics")
        songTitleSpan.append(songTitleLink)
        var spotifyTrackIdSpan = $('<span/>').text("Spotify Track ID: " + element.spotify_track_id)

        //appending all to the final element
        $('.song-list').append(
          $('<div/>')
            .attr("class", "indiv-song")
            .append(artistSpan)
            .append("<br>")
            .append(songTitleSpan)
            .append("<br>")
            .append(spotifyTrackIdSpan)
            .append("<br>")
            .append("<br>")
        )
      }, this);

    })
    .fail(function( jqXHR, textStatus ) {
      alert( "Request failed: " + textStatus );
    //});

    
  })
});

$('#sync-link').on('click', function (event) {
  var jsonob = {"data": 1}

  $.ajax({
        method: "POST",
        url: "http://18.188.140.44/currSong",
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        data: JSON.stringify(jsonob, null, '\t')
    })
    .done(function( msg ) {
      console.log(JSON.stringify(msg));

      localStorage.setItem("spotify_track_id", msg.lyric_page.spotify_track_id)
      console.log(localStorage)


    })
    .fail(function( jqXHR, textStatus ) {
      alert( "Request failed: " + textStatus );
      event.preventDefault()
    //});

    
  });

})