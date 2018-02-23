
urlString = window.location.href
console.log(urlString)

var position = urlString.search("code=")
if (position != -1){
    position +=5
    console.log(position)
    var code = urlString.slice(position)
    console.log(code)

    var jsonob = {
        "code": code
    }

console.log(jsonob)
    $.ajax({
        method: "POST",
        url: "http://127.0.0.1:5000/login",
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        data: JSON.stringify(jsonob, null, '\t')
    })
    .done(function( msg ) {
      console.log(JSON.stringify(msg));


    myStorage = window.localStorage
    myStorage.setItem("access_token", msg.access_token)

    console.log(myStorage)

    })
    .fail(function( jqXHR, textStatus ) {
      alert( "Request failed: " + textStatus );
    //});

    
  });


}