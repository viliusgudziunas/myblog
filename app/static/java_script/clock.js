function startTime() {
    var today = new Date(),
        h = today.getHours(),
        m = today.getMinutes(),
    m = checkTime(m);
    document.getElementById("clock").innerHTML = h + ":" + m;
    var t = setTimeout(startTime, 500);
}

function checkTime(i) {
    if (i < 10) {i = "0" + i}; // add zero in front of numbers < 10
    return i;
}