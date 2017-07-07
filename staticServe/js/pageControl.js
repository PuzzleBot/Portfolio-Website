var pageControl_currentPage = 0;
var pageControl_maxPages = 5;

function showNextPage(){
    var nextPage = (pageControl_currentPage + 1) % pageControl_maxPages;
    var currentPageClassName = ".pageControl_page-" + pageControl_currentPage;
    var nextPageClassName = ".pageControl_page-" + nextPage;

    /*Hide the current page elements, show the next page elements*/
    $( currentPageClassName ).hide(0);
    $( nextPageClassName ).show(0);

    pageControl_currentPage = nextPage;
    document.getElementById("pageCountText").innerHTML = "Page " + (pageControl_currentPage + 1) + " of " + pageControl_maxPages;

    /*Show the previous page button*/
    document.getElementById("projectPageLeft").style.visibility = "visible";

    /*If we're now on the last page, hide the next page button*/
    if((pageControl_currentPage + 1) >= pageControl_maxPages){
        document.getElementById("projectPageRight").style.visibility = "hidden";
    }
}

function showPreviousPage(){
    var prevPage = pageControl_currentPage - 1;
    /*Negative Modulus*/
    if(prevPage < 0){
        prevPage = pageControl_maxPages - 1;
    }

    var currentPageClassName = ".pageControl_page-" + pageControl_currentPage;
    var prevPageClassName = ".pageControl_page-" + prevPage;

    /*Hide the current page elements, show the previous page elements*/
    $( currentPageClassName ).hide(0);
    $( prevPageClassName ).show(0);

    pageControl_currentPage = prevPage;
    document.getElementById("pageCountText").innerHTML = "Page " + (pageControl_currentPage + 1) + " of " + pageControl_maxPages;

    /*Show the next page button*/
    document.getElementById("projectPageRight").style.visibility = "visible";

    /*If we're now on the first page, hide the previous page button*/
    if(pageControl_currentPage <= 0){
        document.getElementById("projectPageLeft").style.visibility = "hidden";
    }
}


function initializePages(numberOfPages){
    document.getElementById("projectButton").className = "active";
    pageControl_maxPages = numberOfPages;
    document.getElementById("pageCountText").innerHTML = "Page 1 of " + pageControl_maxPages;

    $( ".pageControl_page-0" ).show(0);
    for (var i = 1; i < numberOfPages; i++){
        $( (".pageControl_page-" + i) ).hide(0);
    }

    /*If there is only one page, hide the next page button*/
    if(pageControl_maxPages == 1){
        document.getElementById("projectPageRight").style.visibility = "hidden";
    }

    /*Set the button listeners here, so that the document will be ready before any of them can be clicked*/
    document.getElementById("projectPageLeft").addEventListener("click", showPreviousPage);
    document.getElementById("projectPageRight").addEventListener("click", showNextPage);

}
