/*$(document).ready(function(){

$('#cmd').click(function(){    
var doc = new jsPDF();
var specialElementHandlers = {
    '#blog_corpus': function (element, renderer) {
        return true;
    }
};

  
    alert(document.getElementById('blog_corpus').value)
    doc.fromHTML($('#blog_corpus').html(), 15, 15, {
        'width': 170,
            'elementHandlers': specialElementHandlers
    });
    var myWindow = window.open("", "_self");
    myWindow.document.write(document.getElementById('blog_corpus').value);
    doc.save('sample-file.pdf');
});

});
*/
function descargar(){
    var doc = new jsPDF();
    var specialElementHandlers = {
        '#final': function (element, renderer) {
            return true;
        }
    };
    doc.fromHTML(document.getElementById('blog_corpus').value, 15, 15, {
        'width': 170,
        'elementHandlers': specialElementHandlers
    });


   

    
    doc.save("Mi_Blog.pdf")
    
};

/*
$(document).ready(function () {
    var element = $("#blog_corpus"); // global variable
    var getCanvas; //global variable
    html2canvas(element, {
        onrendered: function (canvas) {
            getCanvas = canvas;
        }
    });

    $("#share").on('click', function () {
        var imgageData = getCanvas.toDataURL("image/png");
        //Now browser starts downloading it instead of just showing it
        var newData = imgageData.replace(/^data:image\/png/, "data:application/octet-stream");
        $("#share").attr("download", "your_image.png").attr("href", newData);
    });
});*/
