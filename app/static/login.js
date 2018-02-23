
urlString = window.location.href
console.log(urlString)

var position = urlString.search("code=")
if (position != 0){
    position +=5
    console.log(position)
    var accessKey = urlString.slice(position)
    console.log(accessKey)

    myStorage = window.localStorage
    myStorage.setItem("accessKey", accessKey)

    console.log(myStorage)
}