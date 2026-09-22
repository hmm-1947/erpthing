# Zivoc Branding

A small Frappe app that overrides ERPNext's default UI branding (app name,
logo, favicon, browser tab title) with "Zivoc" branding.

No Frappe or ERPNext core files are modified - all overrides go through
standard `hooks.py` (app_include_css/js, boot_session, after_install) so
this app can be safely removed or upgraded independently of core.

## Install

    bench get-app zivoc_branding /path/to/zivoc_branding
    bench --site your-site install-app zivoc_branding
    bench build --app zivoc_branding
    bench --site your-site clear-cache
