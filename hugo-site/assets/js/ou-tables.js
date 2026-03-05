(function () {
  function normalizeHeader(text) {
    return (text || "").replace(/\s+/g, " ").trim();
  }

  function ensureWrapper(table) {
    var parent = table.parentElement;
    if (parent && parent.classList && parent.classList.contains("ou-table-scroll")) {
      return parent;
    }

    var wrap = document.createElement("div");
    wrap.className = "ou-table-scroll";
    // Improves keyboard accessibility for horizontally scrollable content.
    wrap.setAttribute("role", "region");
    wrap.setAttribute("tabindex", "0");
    wrap.setAttribute("aria-label", "Scrollable table");

    if (parent) {
      parent.insertBefore(wrap, table);
    }
    wrap.appendChild(table);
    return wrap;
  }

  function extractHeaders(table) {
    var ths = Array.prototype.slice.call(table.querySelectorAll("thead th"));
    if (ths.length === 0) {
      // Fallback: try first row of tbody if no thead exists.
      ths = Array.prototype.slice.call(table.querySelectorAll("tbody tr:first-child td, tbody tr:first-child th"));
    }

    var headers = ths.map(function (th, i) {
      var label = normalizeHeader(th.textContent);
      if (label) return label;
      if (i === 0) return "Field";
      return "Column " + String(i + 1);
    });

    // If a table has an empty leading header (common for row-label tables), make it explicit.
    if (headers.length > 0 && normalizeHeader(headers[0]) === "Column 1") {
      headers[0] = "Field";
    }

    return headers;
  }

  function applyDataLabels(table, headers) {
    var rows = Array.prototype.slice.call(table.querySelectorAll("tbody tr"));
    rows.forEach(function (tr) {
      // Include td and th to keep indexing aligned even when row headers are <th>.
      var cells = Array.prototype.slice.call(tr.children).filter(function (el) {
        return el && (el.tagName === "TD" || el.tagName === "TH");
      });

      cells.forEach(function (cell, idx) {
        if (!cell || cell.tagName !== "TD") return;
        var label = headers[idx] || ("Column " + String(idx + 1));
        cell.setAttribute("data-label", label);
      });
    });
  }

  function enhanceTable(table) {
    if (!table || table.dataset.ouTablesEnhanced === "1") return;
    table.dataset.ouTablesEnhanced = "1";
    table.classList.add("ou-table--enhanced");

    ensureWrapper(table);
    var headers = extractHeaders(table);
    var cols = headers.length;
    if (cols > 0) {
      table.classList.add("ou-table--cols-" + String(cols));
    }
    if (cols >= 4) table.classList.add("ou-table--wide");
    if (cols >= 6) table.classList.add("ou-table--xwide");
    applyDataLabels(table, headers);
  }

  function enhanceAll() {
    var tables = document.querySelectorAll(".ou-article-content table");
    for (var i = 0; i < tables.length; i++) {
      enhanceTable(tables[i]);
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", enhanceAll);
  } else {
    enhanceAll();
  }
})();
