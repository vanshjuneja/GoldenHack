function goPython(){
    $.ajax({
        url:"PythonScripts/Main.py",
        context:document.body
    }).done(function() {
        alert('finished python script');;
    });
}