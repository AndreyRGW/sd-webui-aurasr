import launch

if not launch.is_installed("aura_sr"):
    launch.run_pip(f"install aura_sr", "aura_sr")
