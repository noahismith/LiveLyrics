$( "#userForm" ).submit(function( event ) {
 
  // Stop form from submitting normally
  event.preventDefault();
 
  // Get some values from elements on the page:
  var $form = $( this ),
    user = $form.find( "input[name='username']" ).val(),
    url = $form.attr( "action" );
 
  // Send the data using post
  var posting = $.post( url, { username: user } );
 
  // Put the results in a div
  posting.done(function( data ) {

      console.log(data)
      /*
    var content = $( data ).find( "#content" );
    $( "#result" ).empty().append( content );
    */
  });
});