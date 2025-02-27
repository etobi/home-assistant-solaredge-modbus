import logging
from typing import Optional, Dict, Any
from .const import (
    INVERTER1_SENSOR_TYPES,
    INVERTER2_SENSOR_TYPES,
    INVERTER3_SENSOR_TYPES,
    METER1_SENSOR_TYPES,
    METER2_SENSOR_TYPES,
    METER3_SENSOR_TYPES,
    DOMAIN,
    ATTR_STATUS_DESCRIPTION,
    DEVICE_STATUSSES,
    ATTR_MANUFACTURER,
    STORAGE_SENSOR_TYPES,
)
from homeassistant.helpers.entity import Entity
from homeassistant.const import CONF_NAME
from homeassistant.core import callback

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(hass, entry, async_add_entities):
    hub_name = entry.data[CONF_NAME]
    hub = hass.data[DOMAIN][hub_name]["hub"]

    device_info = {
        "identifiers": {(DOMAIN, hub_name)},
        "name": hub_name,
        "manufacturer": ATTR_MANUFACTURER,
    }

    entities = []

    if hub.inverter1_unit > 0:
        for sensor_info in INVERTER1_SENSOR_TYPES.values():
            sensor = SolarEdgeSensor(
                hub_name,
                hub,
                device_info,
                sensor_info[0],
                sensor_info[1],
                sensor_info[2],
                sensor_info[3],
            )
            entities.append(sensor)

    if hub.inverter2_unit > 0:
        for sensor_info in INVERTER2_SENSOR_TYPES.values():
            sensor = SolarEdgeSensor(
                hub_name,
                hub,
                device_info,
                sensor_info[0],
                sensor_info[1],
                sensor_info[2],
                sensor_info[3],
            )
            entities.append(sensor)

    if hub.inverter3_unit > 0:
        for sensor_info in INVERTER3_SENSOR_TYPES.values():
            sensor = SolarEdgeSensor(
                hub_name,
                hub,
                device_info,
                sensor_info[0],
                sensor_info[1],
                sensor_info[2],
                sensor_info[3],
            )
            entities.append(sensor)

    if hub.read_meter1 == True:
        for meter_sensor_info in METER1_SENSOR_TYPES.values():
            sensor = SolarEdgeSensor(
                hub_name,
                hub,
                device_info,
                meter_sensor_info[0],
                meter_sensor_info[1],
                meter_sensor_info[2],
                meter_sensor_info[3],
            )
            entities.append(sensor)

    if hub.read_meter2 == True:
        for meter_sensor_info in METER2_SENSOR_TYPES.values():
            sensor = SolarEdgeSensor(
                hub_name,
                hub,
                device_info,
                meter_sensor_info[0],
                meter_sensor_info[1],
                meter_sensor_info[2],
                meter_sensor_info[3],
            )
            entities.append(sensor)

    if hub.read_meter3 == True:
        for meter_sensor_info in METER3_SENSOR_TYPES.values():
            sensor = SolarEdgeSensor(
                hub_name,
                hub,
                device_info,
                meter_sensor_info[0],
                meter_sensor_info[1],
                meter_sensor_info[2],
                meter_sensor_info[3],
            )
            entities.append(sensor)

    if hub.read_storage == True:
        for sensor_info in STORAGE_SENSOR_TYPES.values():
            sensor = SolarEdgeSensor(
                hub_name,
                hub,
                device_info,
                sensor_info[0],
                sensor_info[1],
                sensor_info[2],
                sensor_info[3],
            )
            entities.append(sensor)

    async_add_entities(entities)
    return True


class SolarEdgeSensor(Entity):
    """Representation of an SolarEdge Modbus sensor."""

    def __init__(self, platform_name, hub, device_info, name, key, unit, icon):
        """Initialize the sensor."""
        self._platform_name = platform_name
        self._hub = hub
        self._key = key
        self._name = name
        self._unit_of_measurement = unit
        self._icon = icon
        self._device_info = device_info

    async def async_added_to_hass(self):
        """Register callbacks."""
        self._hub.async_add_solaredge_sensor(self._modbus_data_updated)

    async def async_will_remove_from_hass(self) -> None:
        self._hub.async_remove_solaredge_sensor(self._modbus_data_updated)

    @callback
    def _modbus_data_updated(self):
        self.async_write_ha_state()

    @callback
    def _update_state(self):
        if self._key in self._hub.data:
            self._state = self._hub.data[self._key]

    @property
    def name(self):
        """Return the name."""
        return f"{self._platform_name} ({self._name})"

    @property
    def unique_id(self) -> Optional[str]:
        return f"{self._platform_name}_{self._key}"

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement."""
        return self._unit_of_measurement

    @property
    def icon(self):
        """Return the sensor icon."""
        return self._icon

    @property
    def state(self):
        """Return the state of the sensor."""
        if self._key in self._hub.data:
            return self._hub.data[self._key]

    @property
    def state_attributes(self) -> Optional[Dict[str, Any]]:
        if self._key in ["i1_status", "i2_status", "i3_status", "i1_statusvendor", "i2_statusvendor", "i3_statusvendor"]:
            if self.state in DEVICE_STATUSSES:
                return {ATTR_STATUS_DESCRIPTION: DEVICE_STATUSSES[self.state]}
        if self._key in ["storage_status"]:
            if self.state in STORAGE_STATUSSES:
                return {ATTR_STATUS_DESCRIPTION: STORAGE_STATUSSES[self.state]}
        return None

    @property
    def should_poll(self) -> bool:
        """Data is delivered by the hub"""
        return False

    @property
    def device_info(self) -> Optional[Dict[str, Any]]:
        return self._device_info
