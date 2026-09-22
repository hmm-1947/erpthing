import frappe


def boot_session(bootinfo):
	"""Override app name/title shown in desk header, browser tab, and
	the user-facing 'Powered by' strings injected into bootinfo."""
	bootinfo["app_name"] = "Zivoc"
	bootinfo["app_title"] = "Zivoc"
	if bootinfo.get("website_settings"):
		bootinfo["website_settings"]["app_name"] = "Zivoc"


def after_install():
	"""Persist branding into Website Settings / System Settings so it
	survives independent of bootinfo/session overrides."""
	_set_website_settings()


def _set_website_settings():
	try:
		website_settings = frappe.get_single("Website Settings")
		website_settings.app_name = "Zivoc"
		website_settings.title_prefix = "Zivoc"
		website_settings.save(ignore_permissions=True)
	except Exception:
		frappe.log_error(title="Zivoc branding: Website Settings update failed")

	try:
		system_settings = frappe.get_single("System Settings")
		if hasattr(system_settings, "app_name"):
			system_settings.app_name = "Zivoc"
			system_settings.save(ignore_permissions=True)
	except Exception:
		pass
