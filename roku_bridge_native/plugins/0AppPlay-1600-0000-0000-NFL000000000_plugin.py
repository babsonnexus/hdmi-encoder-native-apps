# HDMI Encode Native Apps - Roku Bridge
# https://babsonnexus.github.io/hdmi-encoder-native-apps
# v2026.07.03.1617

from .base_plugin import BaseAppPlugin
import logging

class AppPlay_1600_0000_0000_NFL000000000(BaseAppPlugin):

    def __init__(self):
        super().__init__(app_id="44856", app_name="App Play - NFL")

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

        sequence.append({"wait": 20})
        if list_position >= 1:
            for i in range(list_position):
                sequence.append("Right")
                sequence.append({"wait": 5})
        sequence.append("Select")

        return sequence
