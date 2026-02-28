document.addEventListener("DOMContentLoaded", function () {
  var body = document.body;
  var toggle = document.querySelector(".site-nav-toggle");
  var nav = document.getElementById("primary-nav");
  var overlay = document.querySelector(".site-nav-overlay");
  if (!toggle || !nav) return;
  var mobileQuery = window.matchMedia("(max-width: 960px)");
  var syncNavState = function () {
    if (mobileQuery.matches) {
      nav.setAttribute("aria-hidden", body.classList.contains("nav-open") ? "false" : "true");
    } else {
      nav.removeAttribute("aria-hidden");
    }
  };
  var closeNav = function () {
    if (!body.classList.contains("nav-open")) return false;
    body.classList.remove("nav-open");
    toggle.setAttribute("aria-expanded", "false");
    syncNavState();
    return true;
  };
  var openNav = function () {
    if (body.classList.contains("nav-open")) return;
    body.classList.add("nav-open");
    toggle.setAttribute("aria-expanded", "true");
    syncNavState();
    var firstLink = nav.querySelector("a");
    if (firstLink) firstLink.focus();
  };
  syncNavState();
  toggle.addEventListener("click", function () {
    body.classList.contains("nav-open") ? closeNav() : openNav();
  });
  if (overlay) overlay.addEventListener("click", closeNav);
  nav.addEventListener("click", function (e) {
    if (e.target.closest("a") && mobileQuery.matches) closeNav();
  });
  document.addEventListener("keyup", function (e) {
    if (e.key === "Escape" && closeNav()) toggle.focus();
  });
  var mq = window.matchMedia("(min-width: 961px)");
  var mqHandler = function (e) { if (e.matches) closeNav(); syncNavState(); };
  if (mq.addEventListener) mq.addEventListener("change", mqHandler);
  else if (mq.addListener) mq.addListener(mqHandler);
  if (mobileQuery.addEventListener) mobileQuery.addEventListener("change", syncNavState);
  else if (mobileQuery.addListener) mobileQuery.addListener(syncNavState);
});
