"""Platform for sensor integration."""
from __future__ import annotations
from typing import List
from datetime import timedelta
import requests
from requests import Response
from datetime import datetime

SCAN_INTERVAL = timedelta(minutes=5)

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
)
from homeassistant.const import UnitOfTemperature
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType


def setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None) -> None:
    """Set up the sensor platform."""
    add_entities([BabtempSensor()])


class BabtempSensor(SensorEntity):
    _attr_name = "Babice's temperature"
    _attr_native_unit_of_measurement = UnitOfTemperature.CELSIUS
    _attr_device_class = SensorDeviceClass.TEMPERATURE
    _attr_state_class = SensorStateClass.MEASUREMENT

    def update(self) -> None:
        actual_time: str = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
        url: str = f"https://teplomery.gc-system.cz/modules/teplomery/graf_data.php?tab=1&mac=00204AF4E13E&lang=cs&time={actual_time}"
        response: Response = requests.get(url)
        data: str = response.text

        sections: List[str] = data.split("---new-data---")
        first_section: str = sections[0]
        line: str = first_section.strip().split('\n')[-1]
        data_for_sensor: float = line.split('|')[1]

        self._attr_native_value = data_for_sensor