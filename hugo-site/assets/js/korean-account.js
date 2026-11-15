(function () {
  function reveal(hash) {
    if (!hash || hash.charAt(0) !== "#") return;
    var id;
    try { id = decodeURIComponent(hash.slice(1)); } catch (_) { return; }
    var target = document.getElementById(id);
    if (!target) return;
    var element = target;
    var opened = false;
    while (element) {
      if (element.tagName === "DETAILS" && element.classList.contains("ko-audit-dossier") && !element.open) {
        element.open = true;
        opened = true;
      }
      element = element.parentElement;
    }
    if (opened) target.scrollIntoView({ block: "start" });
  }

  function start() {
    reveal(window.location.hash);
    window.addEventListener("hashchange", function () { reveal(window.location.hash); });
    // Also handle a repeated link to a disclosure manually closed after navigation.
    document.addEventListener("click", function (event) {
      var link = event.target.closest && event.target.closest("a[href]");
      if (!link || event.defaultPrevented || event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
      var url = new URL(link.href, window.location.href);
      if (url.origin === window.location.origin && url.pathname === window.location.pathname && url.search === window.location.search) {
        reveal(url.hash);
      }
    });
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", start);
  else start();
})();
