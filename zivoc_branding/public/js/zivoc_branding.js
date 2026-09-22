// Zivoc branding overrides - runs on every desk/website page load.
// Swaps visible "Frappe" / "ERPNext" text nodes for "Zivoc" without
// touching Frappe core or ERPNext source files.

(function () {
	function relabel() {
		document.title = document.title
			.replace(/Frappe/gi, "Zivoc")
			.replace(/ERPNext/gi, "Zivoc");

		document.querySelectorAll(".navbar-brand, .app-logo, .brand-title").forEach(function (el) {
			if (el.textContent && /frappe|erpnext/i.test(el.textContent)) {
				el.textContent = "Zivoc";
			}
		});
	}

	relabel();

	// Desk is a SPA - re-apply on route change since the title/brand
	// nodes get re-rendered by the framework.
	if (window.frappe && frappe.router) {
		frappe.router.on("change", relabel);
	} else {
		document.addEventListener("DOMContentLoaded", relabel);
	}
})();
