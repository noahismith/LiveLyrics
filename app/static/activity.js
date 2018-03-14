var jsonob = {}

var currUser;
var activityFeedDiv = $('<div/>').attr('id', "activity-feed")
activityFeedDiv.text("Recent activity:")
activityFeedDiv.append('<br>')
$('#content').append(activityFeedDiv)

$.ajax({
        method: "GET",
        url: "http://127.0.0.1:5000/lyrics/getRecentActivity",
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        data: JSON.stringify(jsonob, null, '\t')
    })
    .done(function( msg ) {
      console.log(JSON.stringify(msg));
      msg.recent_activity.forEach(function(element) {

        var jsonob = {
            "access_token": localStorage.getItem("access_token"),
            "spotify_track_id": element.spotify_track_id
        }
        var activityDiv = $('<div/>').text("User: " + element.username)

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
            var songTitleSpan = $('<span/>').text(" -- Song: " + msg.lyric_page.songtitle)
            songTitleSpan.append('<br>')
            activityDiv.append(songTitleSpan)
           $('#activity-feed').append(activityDiv)
           console.log(activityDiv.text())
        })
        .fail(function( jqXHR, textStatus ) {
            alert( "Request failed: " + textStatus );
        
    })
    
    }, this);
})
.fail(function( jqXHR, textStatus ) {
    alert( "Request failed: " + textStatus );
//});

    
  });