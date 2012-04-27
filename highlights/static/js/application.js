$(document).ready(function(){
$('.card-body').tooltip({
      selector: "a[rel=tooltip]"
    });
$("a[rel=tooltip]").tooltip();
$("a[rel=popover]").popover("toggle");
$('.dropdown-toggle').dropdown();
$('#myForm tbody tr').formset();
});

