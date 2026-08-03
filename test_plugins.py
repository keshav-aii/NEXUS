from core.plugin_loader import load_plugins

plugins = load_plugins()

print()
print("Plugins Loaded:", len(plugins))