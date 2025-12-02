(function () {
  "use strict";

  /**
   * Easy selector helper function
   */
  const select = (el, all = false) => {
    el = el.trim();
    if (all) {
      return [...document.querySelectorAll(el)];
    } else {
      return document.querySelector(el);
    }
  };

  /**
   * Easy event listener function
   */
  const on = (type, el, listener, all = false) => {
    let selectEl = select(el, all);
    if (selectEl) {
      if (all) {
        selectEl.forEach((e) => e.addEventListener(type, listener));
      } else {
        selectEl.addEventListener(type, listener);
      }
    }
  };
  
  /**
   * Porfolio isotope and filter
   */
  window.addEventListener("load", () => {
    let recipeContainer = select(".recipe-container");
    if (recipeContainer) {
      let recipeIsotope = new Isotope(recipeContainer, {
        itemSelector: ".recipe-item",
      });

      let recipeFilters = select("#recipe-flters li", true);

      on(
        "click",
        "#recipe-flters li",
        function (e) {
          e.preventDefault();
          recipeFilters.forEach(function (el) {
            el.classList.remove("active-filter");
          });
          this.classList.add("active-filter");

          recipeIsotope.arrange({
            filter: this.getAttribute("data-filter"),
          });
          recipeIsotope.on("arrangeComplete", function () {
            AOS.refresh();
          });
        },
        true
      );
    }
  });
})();
