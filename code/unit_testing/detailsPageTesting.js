let host = '127.0.0.1:5500'

function testPage() {

    if (document.readyState=='loading'){
        console.log("Success: My Details page is displayed correctly.");
    } else {
        console.error("Error: My Details page is incorrectly displayed");
    }
        //  http://127.0.0.1:5500/code/Details.html
    if (self.location.host == host){
        console.log("Sucess: The website has the correct domain")
    } else {
        console.error("Error: The website is not on the correct domain");
    }



}

testPage()