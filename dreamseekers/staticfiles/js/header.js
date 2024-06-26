$(document).ready(function () {
  try {
    // 페이지 제목 가져옴
    var pageTitle = document.querySelector("#top-content h1").textContent;
    if (pageTitle) {
      var menuItems = document.querySelectorAll(".menu");
      var menuTab = document.querySelector("#top-content .menu-tab");

      for (var i = 0; i < menuItems.length; i++) {
        var menuItem = menuItems[i];
        var title = menuItem.querySelector("a").textContent;
        var submenus = menuItem.querySelectorAll(".submenu a");

        // 메뉴 이름이 일치하고 주요강의가 아닐때
        if (title === pageTitle && title !== "주요 강의") {
          // 서브메뉴 개수만큼 반복
          for (var j = 0; j < submenus.length; j++) {
            var submenu = submenus[j];
            var url = submenu.href;

            // 버튼 생성
            var a = document.createElement("a");
            a.textContent = submenu.textContent;
            a.href = url;
            a.className = "btn";

            // 현재 페이지와 같다면
            if (window.location.href == url) {
              a.className = "btn-active";
            }
            menuTab.appendChild(a);
          }
        }
        // 메뉴 이름이 일치하고 주요강의 일때
        else if (title === pageTitle && title == "주요 강의") {
          var lectures = document.querySelectorAll(".lecture-title");

          // 전체 강의 추가
          var submenu = submenus[0];
          var a = document.createElement("a");
          a.textContent = "전체 강의";
          a.href = submenu.href;
          a.className = "btn";

          // 현재 페이지와 같다면
          if (window.location.href == submenu.href) {
            a.className = "btn-active";
          }

          menuTab.appendChild(a);

          // 서브메뉴 개수만큼 반복
          for (var j = 0; j < lectures.length; j++) {
            var lecture = lectures[j];
            var lectureId = lecture.dataset.id;
            var lectureHref = "/lecture/list/detail/" + lectureId + "/";

            // 버튼 생성
            var a = document.createElement("a");
            a.textContent = lecture.textContent;
            a.href = lectureHref;
            a.className = "btn";

            // 현재 페이지와 같다면
            if (window.location.pathname == lectureHref) {
              a.className = "btn-active";
            }

            menuTab.appendChild(a);
          }
        }
      }
    }
  } catch (error) {
    /* pass */
  }

  /* 서브 메뉴 */
  $(".menu-list").each(function () {
    var blind = $("#blind");
    var submenu = $(this).find(".submenu-container");
    var menu = $(this).find(".menu");

    menu.each(function () {
      $(this).hover(
        function () {
          blind.height("180px");
          submenu.height("180px");
          $(this).addClass("on");
        },
        function () {
          blind.height("0");
          submenu.height("0");
          $(this).removeClass("on");
        }
      );
    });
  });

  /* (햄버거)사이드 동작  */
  $(".burger-toggle").on("click", function () {
    var sidebar = document.getElementById("sidebar");
    var background = document.querySelector("#sidebar .background");
    var inner = document.querySelector("#sidebar .inner");

    if (sidebar.style.display === "none") {
      sidebar.style.display = "block";
      requestAnimationFrame(function () {
        background.style.opacity = "0.7";
      });
      setTimeout(function () {
        inner.classList.add("active");
      }, 10);
      // 스크롤 비활성화
      document.body.style.overflow = "hidden";
    } else {
      background.style.opacity = "0";
      inner.classList.remove("active");
      setTimeout(function () {
        sidebar.style.display = "none";
      }, 1000);
      // 스크롤 활성화
      document.body.style.overflow = "auto";
    }
  });

  // top-header에 마우스를 올려도 글자색변경
  document
    .querySelector(".top-header")
    .addEventListener("mouseover", function () {
      var menuItems = document.querySelectorAll(".menu-list .menu a");
      var burger = document.querySelectorAll(".menu-trigger span");
      menuItems.forEach(function (item) {
        item.style.color = "black";
      });
      burger.forEach(function (item) {
        item.style.backgroundColor = "black";
      });
    });
  // 원래 색상으로 되돌림
  document
    .querySelector(".top-header")
    .addEventListener("mouseout", function () {
      var menuItems = document.querySelectorAll(".menu-list .menu a");
      var burger = document.querySelectorAll(".menu-trigger span");
      menuItems.forEach(function (item) {
        item.style.color = "";
      });
      burger.forEach(function (item) {
        item.style.backgroundColor = "";
      });
    });

  // 사이드 버튼 숨김
  var float = document.querySelector(".floating");
  var main = document.querySelector("#top-content");
  if (!main) {
    float.style.opacity = 0;
  }

  /* 스크롤 애니메이션 */
  // 클래스가 "scroll_on"인 모든 요소를 선택합니다.
  const $counters = $(".scroll_on");

  // 노출 비율(%)과 애니메이션 반복 여부(true/false)를 설정합니다.
  const exposurePercentage = 30; // ex) 스크롤 했을 때 $counters 컨텐츠가 화면에 100% 노출되면 숫자가 올라갑니다.
  const loop = true; // 애니메이션 반복 여부를 설정합니다. (true로 설정할 경우, 요소가 화면에서 사라질 때 다시 숨겨집니다.)

  // 윈도우의 스크롤 이벤트를 모니터링합니다.
  $(window)
    .on("scroll", function () {
      // 각 "scroll_on" 클래스를 가진 요소에 대해 반복합니다.
      $counters.each(function () {
        const $el = $(this);

        // 요소의 위치 정보를 가져옵니다.
        const rect = $el[0].getBoundingClientRect();
        const winHeight = window.innerHeight; // 현재 브라우저 창의 높이
        const contentHeight = rect.bottom - rect.top; // 요소의 높이

        // 요소가 화면에 특정 비율만큼 노출될 때 처리합니다.
        if (
          rect.top <= winHeight - (contentHeight * exposurePercentage) / 100 &&
          rect.bottom >= (contentHeight * exposurePercentage) / 100
        ) {
          $el.addClass("active");
        }
        // 요소가 화면에서 완전히 사라졌을 때 처리합니다.
        if (loop && (rect.bottom <= 0 || rect.top >= window.innerHeight)) {
          $el.removeClass("active");
        }
      });
    })
    .scroll();
});

/* header에 on클래스 추가 (스크롤시 변경) */
window.onscroll = function () {
  var header = document.querySelector("header");
  var float = document.querySelector(".floating");
  var main = document.querySelector("#top-content");

  var scrollPosition = window.scrollY;

  if (scrollPosition > 50) {
    header.classList.add("on");
    if (!main) {
      float.style.opacity = 1;
    }
  } else {
    header.classList.remove("on");
    if (!main) {
      float.style.opacity = 0;
    }
  }
};

// 메뉴 색 변경
document.querySelectorAll(".menu-list > li.menu a").forEach(function (item) {
  item.addEventListener("mouseover", function () {
    // 마우스를 올렸을 때의 스타일
    item.style.color = "var(--primary-color)";
  });
  item.addEventListener("mouseout", function () {
    // 마우스를 내렸을 때의 스타일
    item.style.color = "";
  });
});
