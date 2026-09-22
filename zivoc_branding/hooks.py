app_name = "zivoc_branding"
app_title = "Zivoc"
app_publisher = "Zivoc"
app_description = "Zivoc branding overrides for ERPNext desk and website"
app_email = "support@zivoc.example"
app_license = "mit"

# ---------------------------------------------------------------------------
# Desk / login branding
# ---------------------------------------------------------------------------

# Injected into every page (desk + website) - overrides tab title, favicon,
# and swaps the Frappe logo for Zivoc's without touching core files.
app_include_css = "/assets/zivoc_branding/css/zivoc_branding.css"
app_include_js = "/assets/zivoc_branding/js/zivoc_branding.js"
web_include_css = "/assets/zivoc_branding/css/zivoc_branding.css"

# Website / desk title shown in the browser tab and PDF exports
app_logo_url = "/assets/zivoc_branding/images/zivoc-logo.svg"

# Favicon
website_context = {
	"favicon": "/assets/zivoc_branding/images/zivoc-favicon.svg",
	"splash_image": "/assets/zivoc_branding/images/zivoc-logo.svg",
}

# Overrides the "Powered by Frappe" / site title text used across desk,
# login page and password-reset emails.
boot_session = "zivoc_branding.branding.boot_session"

# Runs once after this app is installed on a site - sets Website Settings
# (banner, app name) and System Settings so the change is baked into the
# site's own DB config, not just static assets.
after_install = "zivoc_branding.branding.after_install"
after_migrate = "zivoc_branding.branding.after_install"
