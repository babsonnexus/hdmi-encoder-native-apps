# HDMI Encode Native Apps - Roku Bridge
# https://babsonnexus.github.io/hdmi-encoder-native-apps
# v2026.05.14.1806

from .base_plugin import BaseAppPlugin
import logging

class AppPlay_1051_0000_0000_MSNBC0000000(BaseAppPlugin):

    def __init__(self):
        super().__init__(app_id="820590", app_name="App Play - MS NOW")

    def tune_channel(self, roku_ip, channel_data):
        # Base station tuning
        logging.info(f"[{self.app_name} Plugin] Tuning to '{channel_data.get('name')}'.")

        plugin_data = channel_data.get('plugin_data', {})
        list_position = plugin_data.get('list_position')

        try:
            list_position = int(list_position)
        except (ValueError, TypeError):
             list_position = 0

        # Custom station tuning
        sequence = []

        sequence.append({"wait": 10})
        sequence.append("Select")
        sequence.append({"wait": 5})
        sequence.append("Back")

        return sequence
