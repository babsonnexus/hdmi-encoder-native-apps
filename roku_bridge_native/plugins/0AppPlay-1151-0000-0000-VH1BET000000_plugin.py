# HDMI Encode Native Apps - Roku Bridge
# https://babsonnexus.github.io/hdmi-encoder-native-apps
# v2026.05.14.1806

from .base_plugin import BaseAppPlugin
import logging

class AppPlay_1151_0000_0000_VH1BET000000(BaseAppPlugin):

    def __init__(self):
        super().__init__(app_id="85100", app_name="App Play - VH1 & BET")

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
        sequence.append("Left")
        sequence.append({"wait": 1})
        sequence.append("Down")
        sequence.append({"wait": 1})
        sequence.append("Select")

        return sequence
