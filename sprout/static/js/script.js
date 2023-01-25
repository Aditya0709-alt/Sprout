function sleep(milliseconds) {
    const date = Date.now();
    let currentDate = null;
    do { currentDate = Date.now(); } 
    while (currentDate - date < milliseconds);
}

function httpPost(url)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("POST", url, true); 
    xmlHttp.send(null);
}