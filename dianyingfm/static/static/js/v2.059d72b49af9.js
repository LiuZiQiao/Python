UI.navSlidable = function(){
    if(UI.$scrWindow.width() > 1200){
        return true;
    }
    return false;
};


UI.updateScrollState = function(){
   if ( UI.$scrWindow.scrollTop() > 150 ) {
        if( 'none' == UI.$gotop.css('display')  && UI.navSlidable()) {
            UI.$gotop.show();
            if(UI.$subnav.length){
                $('.subnav').css('top', '0');
                $('body').css('padding', '46px');
                $('.navbar').hide();
            }
        }
    }else {
        if( 'none' != UI.$gotop.css('display')  && UI.navSlidable()) {
            UI.$gotop.hide();
            if(UI.$subnav.length){
                $('.subnav').css('top', '46px');
                $('.navbar').show();
                $('body').css('padding', '82px');
            }
        }
    }

    UI.updateWaterfallState();
    return false;
};


UI.getUrlParamByName = function(name) {
    var results = new RegExp('[\?&]' + name + '=([^&#]*)').exec(window.location.href);
    if (results==null){
       return null;
    }
    else{
       return results[1] || 0;
    }
};


/* Scroll to top button */
$(window).on('click', '.fm-totop', function(){
    $.scrollTo(0, 500);
    return false;
});


/* FM Ajax Like/Dislike Buttons */
$('body').on('click', '.fm-btn-ajax', function(){
    var link = $(this);
    var btnClass = link.attr('data-class');
    if(link.hasClass(btnClass)){
        var type = 'undo_tag';
    }else{
        var type = 'tag';
    }

    var url = '/movie/' + link.attr('data-movie') + '/' + type + '/' + link.attr('data-cat') + '?type=json&_=' + Math.random();
    var cat = link.attr('data-cat');
    var exclusive = {
        "planned": "watched",
        "watched": "planned",
        "disliked": "liked",
        "liked": "disliked"
    };
    $.getJSON(url, function(j){
        if(j.ret == 0){
            if(type == 'tag'){

                link.addClass(btnClass);
                link.removeClass('btn-default');

                if (exclusive[cat]) {
                    var exclu = $(link.parent().children("[data-cat='" + exclusive[cat] + "']")[0]);
                    exclu.removeClass(exclu.attr("data-class"));
                    exclu.addClass("btn-default");
                }

            }else{
                link.addClass('btn-default');
                link.removeClass(btnClass);
            }
        }
    });
    return false;
});


/* FM Ajax waterfall movie load */
UI.isScrollBarShown = function () {
    return $(document).height() > $(window).height();
};


UI.runWaterfall = function () {

    if (UI.allowRunWaterfall) {
        UI.allowRunWaterfall = false;
        $("#loading-div").removeClass("hide");

        var genre = UI.getUrlParamByName("genre") || "";
        var region = UI.getUrlParamByName("region") || "";
        var sort = UI.getUrlParamByName("sort") || "";
        var year = UI.getUrlParamByName("year") || "";
        var director = UI.getUrlParamByName("director") || "";
        var starring = UI.getUrlParamByName("starring") || "";
        var text = UI.getUrlParamByName("text") || "";

        var jsonUrl =
            "?genre=" + genre +
            "&p=" + (UI.waterfallCurrentPage + 1) +
            "&region=" + region +
            "&sort=" + sort +
            "&year=" + year +
            "&director=" + director +
            "&starring=" + starring +
            "&text=" + text +
            "&waterfall=water";

        $.getJSON(jsonUrl, function (j) {

            if (j.ret == 0) {
                UI.waterfallCurrentPage++;
                $("#loading-div").addClass("hide");

                $(".fm-result-list")[0].innerHTML += j.html;

                // set false if empty html returned
                UI.allowRunWaterfall = j.html.length > 10;


            } else if (j.ret == 302) {
                //var params = '/' + window.location.href.substring(window.location.href.indexOf('search'));
                //window.location.href = "http://" + window.location.host + j.redirect + "?next=" + params;
                $("#loading-div")[0].innerText = "您需要登录之后才能搜索更多电影。";
                UI.allowRunWaterfall = false;
            }
        });
    }
};


$("#useWaterfallLoad").change(function() {
    if ($(this).is(':checked')) {
        UI.allowRunWaterfall = true;
        $("#pagination").addClass("hide");

        while (!UI.isScrollBarShown() && UI.allowRunWaterfall) {
            UI.runWaterfall();
        }

    } else {
        UI.allowRunWaterfall = false;
        $("#pagination").removeClass("hide");
    }
});


UI.updateWaterfallState = function(){
    var scrolled_at_bottom =
        $(window).scrollTop() + 300 >= $(document).height() - $(window).height();
    if (scrolled_at_bottom) {
        UI.runWaterfall();
    }
};
/* END of FM Ajax waterfall movie load */


$('.fm-write-comment textarea').on('keyup', function(){
    var $txt = $(this);
    setTimeout(function(){
        var length = $txt.val().length;
        var $counter = $txt.parent().find('.counter');
        $counter.text(length);
        if(length > 200){
            $counter.addClass('red');
            $txt.parent().find('button').prop('disabled', true);
        }else{
            $counter.removeClass('red');
            $txt.parent().find('button').removeProp('disabled');
        }
    }, 200);
    return true;
});


if(typeof String.prototype.trim !== 'function') {
    String.prototype.trim = function() {
        return this.replace(/^\s+|\s+$/g, '');
    }
}


UI.setCookie = function(cname,cvalue,exsecs)
{
    var d = new Date();
    d.setTime(d.getTime()+(exsecs*1000));
    var expires = "expires="+d.toGMTString();
    document.cookie = cname + "=" + cvalue + "; " + expires + '; path=/';
};


UI.getCookie = function(cname)
{
    var name = cname + "=";
    var ca = document.cookie.split(';');
    for(var i=0; i<ca.length; i++)
    {
        var c = ca[i].trim();
        if (c.indexOf(name)==0) return c.substring(name.length,c.length);
    }
    return "";
};


$(function(){
    UI.$scrWindow = $(window);
    UI.fadeTime = 500;
    UI.$gotop = $('.fm-totop');
    UI.$gotop.hide();
    UI.$subnav = $('.subnav');
    UI.updateScrollState();
    UI.$scrWindow.scroll(UI.updateScrollState);

    UI.allowRunWaterfall = false;
    if (UI.allowRunWaterfall) $("#useWaterfallLoad")[0].click();
    UI.waterfallCurrentPage = (parseInt(UI.getUrlParamByName("p")) || 1);
});
