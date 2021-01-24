$(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
    $('.collapsible').collapsible();
    $('.modal').modal();
    $('.fixed-action-btn').floatingActionButton();
    $("a[href='#top']").click(function() {
    $("html, body").animate({ scrollTop: 0 }, "slow");
    return false;
    });
    
  });


