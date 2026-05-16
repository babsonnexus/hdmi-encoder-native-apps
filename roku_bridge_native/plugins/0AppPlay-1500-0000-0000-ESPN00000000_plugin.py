# HDMI Encode Native Apps - Roku Bridge
# https://babsonnexus.github.io/hdmi-encoder-native-apps
# v2026.05.15.1635

from .base_plugin import BaseAppPlugin
import logging

class AppPlay_1500_0000_0000_ESPN00000000(BaseAppPlugin):

    def __init__(self):
        super().__init__(app_id="34376", app_name="App Play - ESPN")

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

        sequence.append({"wait": 15})
        for i in range(50):
            sequence.append("Down")
        sequence.append({"wait": 1})
        for i in range(10):
            sequence.append("Left")
        sequence.append({"wait": 1})
        sequence.append("Right")
        sequence.append({"wait": 1})
        if list_position >= 1:
            for i in range(list_position):
                sequence.append("Right")
                sequence.append({"wait": 1})
        sequence.append("Select")
        sequence.append({"wait": 5})
        sequence.append("Select")
        sequence.append({"wait": 1})
        sequence.append("Select")

        return sequence
