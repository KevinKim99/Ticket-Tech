function testDisplay() {

    if (document.readyState=='complete'){
        console.log("Success: My Details page is displayed correctly.");
    } else {
        console.error("Error: My Details page is incorrectly displayed");
    }
   
    //  http://127.0.0.1:5500/code/Details.html
}

testDisplay()