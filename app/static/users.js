$( "#userForm" ).submit(function( event ) {
 
  // Stop form from submitting normally
  event.preventDefault();
 
  // Get some values from elements on the page:
  
  var $form = $( this ),
    user = $form.find( "input[name='username']" ).val(),
    urltar = $form.attr( "action" );
 
    var jsonob = { "username": user }
    console.log(JSON.stringify(jsonob))
    /*
  // Send the data using post
  var posting = $.post( url, { "username": user } );
 console.log(posting)
  // Put the results in a div
  posting.done(function( data ) {

      console.log(data)

    var content = $( data ).find( "#content" );
    $( "#result" ).empty().append( content );
    */

    console.log(user)
    console.log(urltar)
    $.ajax({
        method: "POST",
        url: "http://127.0.0.1:5000/users/info",
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        data: JSON.stringify(jsonob, null, '\t')
    })
    .done(function( msg ) {
      console.log(JSON.stringify(msg));

      //POPULATE PRETTY HTML
      //make it elegant

      var result = $('<div/>', {text: msg.user.username})
      $('#searchResults').append(result)
    })
    .fail(function( jqXHR, textStatus ) {
      alert( "Request failed: " + textStatus );
    //});

    
  });
});

$( '#editForm').submit(function(event) {
  event.preventDefault()

  var $form = $( this ),
    userf = $form.find( "input[name='username']" ).val(),
    birthdatef = $form.find( "input[name='birthdate']" ).val(),
    emailf = $form.find( "input[name='email']" ).val(),
    urltar = $form.attr( "action" );
  
  console.log(localStorage)
  var jsonob = {
    "username": userf,
    "birthdate": birthdatef,
    "email": emailf,
    "access_token": localStorage.getItem("access_token")
  }

  console.log(jsonob)

  $.ajax({
        type: "POST",
        url: "http://127.0.0.1:5000/users/edit",
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

    
  });

})