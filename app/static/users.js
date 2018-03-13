$( "#userForm" ).submit(function( event ) {
 
  // Stop form from submitting normally
  event.preventDefault();
 
  // Get some values from elements on the page:
  
  var $form = $( this ),
    user = $form.find( "input[name='username']" ).val(),
    urltar = $form.attr( "action" );
 
    var jsonob = { "username": user }
    console.log(JSON.stringify(jsonob))

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

      $('#searchResults').empty()
      
      var result = $('<div/>')
      var resultLink = $('<a/>').attr('href', "/")
      resultLink.text(msg.user.username)
      resultLink.click(function (event) {
        event.preventDefault()

        var usernameSpan = $('<span/>').text("Username: " + msg.user.username)
        var emailSpan = $('<span/>').text(" E-mail: " + msg.user.email)
        var birthdateSpan = $('<span/>').text("Birthdate: " + msg.user.birthdate)
        var contributionsSpan = $('<span/>').text("Number of Contributions: " + msg.user.num_of_contributions)

        $('.user-box').empty()
        $('.user-box').show()

        $('.user-box')
        .append(usernameSpan)
        .append("<br>")
        .append(emailSpan)
        .append("<br>")
        .append(birthdateSpan)
        .append("<br>")
        .append(contributionsSpan)
      })

      result.append(resultLink)
      $('#searchResults').append(result)

      $('#searchResults').append('<br>')
  
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