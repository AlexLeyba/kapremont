//Set Search Input display to default
function definput() {
    $('#find').css('width', '80%');
    $('.header__main_find img').show();
    // $('#find').val('');
}

$(document).ready(function () {

    //рисуем стрелочку у элементов меню 
    $('.nav>ul>li>ul>li').each(function(i,elem) {
     
    if ($(this).find("ul").length!=0) {
        console.log($(this),'потомок есть');
        $(this).find("a:first").append( '<i class="fa fa-angle-right"></i>' );
    } else {
        console.log('потомка нет');
    }
});
    // var $ulElements = $('.nav>ul>li>ul');
    // if ($ulElements.find("li")) 
    // {
    //     $ulElements.find("a").append( "<i class="fa fa-angle-right"></i>" );
    // }

    $('.menu__icon').on('click', function() {

        if ($(this).find("ul").length != 0) {
            console.log($(this), 'потомок есть');
            $(this).find("a:first").append('<i class="fa fa-angle-right"></i>');
        } else {
            console.log('потомка нет');
        }
    });
    $('.menu__icon').on('click', function () {

        $(this).closest('.menu').toggleClass('menu_state_open');
        $('.header__main_menu').toggleClass('mobile');
        $('.header__main').toggle();
    });

    // settings for a new language (Russian)
    // make sure dhtmlxcalendar.js will be loaded
    dhtmlXCalendarObject.prototype.langData["ru"] = {
        // date format for inputs
        dateformat: "%d.%m.%Y",
        // header format
        hdrformat: "%F %Y",
        // full names of months
        monthesFNames: ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь",
            "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"
        ],
        // short names of months
        monthesSNames: ["Янв", "Фев", "Мар", "Апр", "Май", "Июн",
            "Июл", "Авг", "Сен", "Окт", "Ноя", "Дек"
        ],
        // full names of days
        daysFNames: ["Воскресенье", "Понедельник", "Вторник", "Среда",
            "Четверг", "Пятница", "Суббота"
        ],
        // short names of days
        daysSNames: ["Вс", "Пн", "Вт", "Ср", "Чт", "Пт", "Сб"],
        // starting day of a week. Number from 1(Monday) to 7(Sunday)
        weekstart: 1,
        // the title of the week number column
        weekname: "н",
        // name of the "Today" button
        today: "Сегодня",// name of the "Clear" button
        clear: "Очистить"
    };
    myCalendar = new dhtmlXCalendarObject("calendarHere");
    myCalendar.hideTime();
    myCalendar.attachEvent("onClick", function (d) {
        var c=myCalendar.getFormatedDate("%Y-%m-%d");
        $("#calendar").val(c);
        $("#form").submit();
        // $.ajax({
        //     type: "POST",
        //     url: "http://127.0.0.1:8000/sort/",
        //     data: "dt=" + myCalendar.getFormatedDate("%Y-%m-%d"),
        //     success: function (msg) {
        //         console.log("Прибыли данные");
        //     }
        // });
    });
    var ms = Date.parse('11 июня 2019');
    
    myCalendar.setDate(new Date());
    myCalendar.show();
    myCalendar.loadUserLanguage("ru");

    //animate numbers
var comma_separator_number_step = $.animateNumber.numberStepFactories.separator(' ');
    $('.ib__item_count').each(function(i,elem) {
         
        $(this).animateNumber(
      {
        number: $(this).html(),
        numberStep: comma_separator_number_step
      },
        {
    easing: 'swing',
    duration: 3000
  }
    );
    });
    
   

    $('.header__logo').click(function (e) {
        window.location.href = "/";
    })

    $('.header__profile').click(function (e) {
        window.open("http://portal.fkr48.ru", "_blank");
    })
    $('.slide1').click(function (e) {
        window.open("http://portal.fkr48.ru", "_blank");
        alert ('1');
    })

    $('#find').click(function (e) {
        $('#find').val('');
        $('#find').css('width', '100%');
        $('.header__main_find img').hide();
    })

    //Header Slider
    $('.slider').bxSlider({
        auto: true,
        stopAutoOnClick: true,
        pager: true,
    });

    //Partners Slider
    $('.pblock_content').slick({
        dots: false,
        infinite: true,
        speed: 300,
        slidesToShow: 7,
        slidesToScroll: 1,
        responsive: [{
            breakpoint: 1030,
            settings: {
                slidesToShow: 5,
                slidesToScroll: 1,
                infinite: true,
                dots: false
            }
        },
            {
                breakpoint: 770,
                settings: {
                    slidesToShow: 4,
                    slidesToScroll: 1,
                    infinite: true,
                    dots: false
                }
            },
            {
                breakpoint: 600,
                settings: {
                    slidesToShow: 2,
                    slidesToScroll: 1
                }
            },
            {
                breakpoint: 430,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1
                }

            }

            // You can unslick at a given breakpoint now by adding:
            // settings: "unslick"
            // instead of a settings object
        ]
    });
});