DOMAIN = "solaredge_modbus"
DEFAULT_NAME = "solaredge"
DEFAULT_SCAN_INTERVAL = 30
DEFAULT_PORT = 1502
DEFAULT_READ_METER1 = False
DEFAULT_READ_METER2 = False
DEFAULT_READ_METER3 = False
CONF_SOLAREDGE_HUB = "solaredge_hub"
ATTR_STATUS_DESCRIPTION = "status_description"
ATTR_MANUFACTURER = "Solaredge"
CONF_INVERTER1_UNIT = "inverter1_unit"
CONF_INVERTER2_UNIT = "inverter2_unit"
CONF_INVERTER3_UNIT = "inverter3_unit"
DEFAULT_INVERTER_UNIT = 1
DEFAULT_DEACTIVATED_INVERTER_UNIT = 0
CONF_READ_METER1 = "read_meter_1"
CONF_READ_METER2 = "read_meter_2"
CONF_READ_METER3 = "read_meter_3"
CONF_READ_STORAGE = "read_storage"
DEFAULT_READ_STORAGE = False

INVERTER1_SENSOR_TYPES = {
    "I1_AC_Current": ["I1 AC Current", "i1_accurrent", "A", "mdi:current-ac"],
    "I1_AC_CurrentA": ["I1 AC Current A", "i1_accurrenta", "A", "mdi:current-ac"],
    "I1_AC_CurrentB": ["I1 AC Current B", "i1_accurrentb", "A", "mdi:current-ac"],
    "I1_AC_CurrentC": ["I1 AC Current C", "i1_accurrentc", "A", "mdi:current-ac"],
    "I1_AC_VoltageAB": ["I1 AC Voltage AB", "i1_acvoltageab", "V", None],
    "I1_AC_VoltageBC": ["I1 AC Voltage BC", "i1_acvoltagebc", "V", None],
    "I1_AC_VoltageCA": ["I1 AC Voltage CA", "i1_acvoltageca", "V", None],
    "I1_AC_VoltageAN": ["I1 AC Voltage AN", "i1_acvoltagean", "V", None],
    "I1_AC_VoltageBN": ["I1 AC Voltage BN", "i1_acvoltagebn", "V", None],
    "I1_AC_VoltageCN": ["I1 AC Voltage CN", "i1_acvoltagecn", "V", None],
    "I1_AC_Power": ["I1 AC Power", "i1_acpower", "W", "mdi:solar-power"],
    "I1_AC_Frequency": ["I1 AC Frequency", "i1_acfreq", "Hz", None],
    "I1_AC_VA": ["I1 AC VA", "i1_acva", "VA", None],
    "I1_AC_VAR": ["I1 AC VAR", "i1_acvar", "VAR", None],
    "I1_AC_PF": ["I1 AC PF", "i1_acpf", "%", None],
    "I1_AC_Energy_KWH": ["I1 AC Energy KWH", "i1_acenergy", "kWh", "mdi:solar-power"],
    "I1_DC_Current": ["I1 DC Current", "i1_dccurrent", "A", "mdi:current-dc"],
    "I1_DC_Voltage": ["I1 DC Voltage", "i1_dcvoltage", "V", None],
    "I1_DC_Power": ["I1 DC Power", "i1_dcpower", "W", "mdi:solar-power"],
    "I1_Temp_Sink": ["I1 Temp Sink", "i1_tempsink", "°C", None],
    "I1_Status": ["I1 Status", "i1_status", None, None],
    "I1_Status_Vendor": ["I1 Status Vendor", "i1_statusvendor", None, None],
}

INVERTER2_SENSOR_TYPES = {
    "I2_AC_Current": ["I2 AC Current", "i2_accurrent", "A", "mdi:current-ac"],
    "I2_AC_CurrentA": ["I2 AC Current A", "i2_accurrenta", "A", "mdi:current-ac"],
    "I2_AC_CurrentB": ["I2 AC Current B", "i2_accurrentb", "A", "mdi:current-ac"],
    "I2_AC_CurrentC": ["I2 AC Current C", "i2_accurrentc", "A", "mdi:current-ac"],
    "I2_AC_VoltageAB": ["I2 AC Voltage AB", "i2_acvoltageab", "V", None],
    "I2_AC_VoltageBC": ["I2 AC Voltage BC", "i2_acvoltagebc", "V", None],
    "I2_AC_VoltageCA": ["I2 AC Voltage CA", "i2_acvoltageca", "V", None],
    "I2_AC_VoltageAN": ["I2 AC Voltage AN", "i2_acvoltagean", "V", None],
    "I2_AC_VoltageBN": ["I2 AC Voltage BN", "i2_acvoltagebn", "V", None],
    "I2_AC_VoltageCN": ["I2 AC Voltage CN", "i2_acvoltagecn", "V", None],
    "I2_AC_Power": ["I2 AC Power", "i2_acpower", "W", "mdi:solar-power"],
    "I2_AC_Frequency": ["I2 AC Frequency", "i2_acfreq", "Hz", None],
    "I2_AC_VA": ["I2 AC VA", "i2_acva", "VA", None],
    "I2_AC_VAR": ["I2 AC VAR", "i2_acvar", "VAR", None],
    "I2_AC_PF": ["I2 AC PF", "i2_acpf", "%", None],
    "I2_AC_Energy_KWH": ["I2 AC Energy KWH", "i2_acenergy", "kWh", "mdi:solar-power"],
    "I2_DC_Current": ["I2 DC Current", "i2_dccurrent", "A", "mdi:current-dc"],
    "I2_DC_Voltage": ["I2 DC Voltage", "i2_dcvoltage", "V", None],
    "I2_DC_Power": ["I2 DC Power", "i2_dcpower", "W", "mdi:solar-power"],
    "I2_Temp_Sink": ["I2 Temp Sink", "i2_tempsink", "°C", None],
    "I2_Status": ["I2 Status", "i2_status", None, None],
    "I2_Status_Vendor": ["I2 Status Vendor", "i2_statusvendor", None, None],
}

INVERTER3_SENSOR_TYPES = {
    "I3_AC_Current": ["I3 AC Current", "i3_accurrent", "A", "mdi:current-ac"],
    "I3_AC_CurrentA": ["I3 AC Current A", "i3_accurrenta", "A", "mdi:current-ac"],
    "I3_AC_CurrentB": ["I3 AC Current B", "i3_accurrentb", "A", "mdi:current-ac"],
    "I3_AC_CurrentC": ["I3 AC Current C", "i3_accurrentc", "A", "mdi:current-ac"],
    "I3_AC_VoltageAB": ["I3 AC Voltage AB", "i3_acvoltageab", "V", None],
    "I3_AC_VoltageBC": ["I3 AC Voltage BC", "i3_acvoltagebc", "V", None],
    "I3_AC_VoltageCA": ["I3 AC Voltage CA", "i3_acvoltageca", "V", None],
    "I3_AC_VoltageAN": ["I3 AC Voltage AN", "i3_acvoltagean", "V", None],
    "I3_AC_VoltageBN": ["I3 AC Voltage BN", "i3_acvoltagebn", "V", None],
    "I3_AC_VoltageCN": ["I3 AC Voltage CN", "i3_acvoltagecn", "V", None],
    "I3_AC_Power": ["I3 AC Power", "i3_acpower", "W", "mdi:solar-power"],
    "I3_AC_Frequency": ["I3 AC Frequency", "i3_acfreq", "Hz", None],
    "I3_AC_VA": ["I3 AC VA", "i3_acva", "VA", None],
    "I3_AC_VAR": ["I3 AC VAR", "i3_acvar", "VAR", None],
    "I3_AC_PF": ["I3 AC PF", "i3_acpf", "%", None],
    "I3_AC_Energy_KWH": ["I3 AC Energy KWH", "i3_acenergy", "kWh", "mdi:solar-power"],
    "I3_DC_Current": ["I3 DC Current", "i3_dccurrent", "A", "mdi:current-dc"],
    "I3_DC_Voltage": ["I3 DC Voltage", "i3_dcvoltage", "V", None],
    "I3_DC_Power": ["I3 DC Power", "i3_dcpower", "W", "mdi:solar-power"],
    "I3_Temp_Sink": ["I3 Temp Sink", "i3_tempsink", "°C", None],
    "I3_Status": ["I3 Status", "i3_status", None, None],
    "I3_Status_Vendor": ["I3 Status Vendor", "i3_statusvendor", None, None],
}


METER1_SENSOR_TYPES = {
    "M1_AC_Current": ["M1 AC Current", "m1_accurrent", "A", "mdi:current-ac"],
    "M1_AC_Current_A": ["M1 AC Current_A", "m1_accurrenta", "A", "mdi:current-ac"],
    "M1_AC_Current_B": ["M1 AC Current_B", "m1_accurrentb", "A", "mdi:current-ac"],
    "M1_AC_Current_C": ["M1 AC Current_C", "m1_accurrentc", "A", "mdi:current-ac"],
    "M1_AC_Voltage_LN": ["M1 AC Voltage LN", "m1_acvoltageln", "V", None],
    "M1_AC_Voltage_AN": ["M1 AC Voltage AN", "m1_acvoltagean", "V", None],
    "M1_AC_Voltage_BN": ["M1 AC Voltage BN", "m1_acvoltagebn", "V", None],
    "M1_AC_Voltage_CN": ["M1 AC Voltage CN", "m1_acvoltagecn", "V", None],
    "M1_AC_Voltage_LL": ["M1 AC Voltage LL", "m1_acvoltagell", "V", None],
    "M1_AC_Voltage_AB": ["M1 AC Voltage AB", "m1_acvoltageab", "V", None],
    "M1_AC_Voltage_BC": ["M1 AC Voltage BC", "m1_acvoltagebc", "V", None],
    "M1_AC_Voltage_CA": ["M1 AC Voltage CA", "m1_acvoltageca", "V", None],
    "M1_AC_Frequency": ["M1 AC Frequency", "m1_acfreq", "Hz", None],
    "M1_AC_Power": ["M1 AC Power", "m1_acpower", "W", None],
    "M1_AC_Power_A": ["M1 AC Power A", "m1_acpowera", "W", None],
    "M1_AC_Power_B": ["M1 AC Power B", "m1_acpowerb", "W", None],
    "M1_AC_Power_C": ["M1 AC Power C", "m1_acpowerc", "W", None],
    "M1_AC_VA": ["M1 AC VA", "m1_acva", "VA", None],
    "M1_AC_VA_A": ["M1 AC VA A", "m1_acvaa", "VA", None],
    "M1_AC_VA_B": ["M1 AC VA B", "m1_acvab", "VA", None],
    "M1_AC_VA_C": ["M1 AC VA C", "m1_acvac", "VA", None],
    "M1_AC_VAR": ["M1 AC VAR", "m1_acvar", "VAR", None],
    "M1_AC_VAR_A": ["M1 AC VAR A", "m1_acvara", "VAR", None],
    "M1_AC_VAR_B": ["M1 AC VAR B", "m1_acvarb", "VAR", None],
    "M1_AC_VAR_C": ["M1 AC VAR C", "m1_acvarc", "VAR", None],
    "M1_AC_PF": ["M1 AC PF", "m1_acpf", "%", None],
    "M1_AC_PF_A": ["M1 AC PF A", "m1_acpfa", "%", None],
    "M1_AC_PF_B": ["M1 AC PF B", "m1_acpfb", "%", None],
    "M1_AC_PF_C": ["M1 AC PF C", "m1_acpfc", "%", None],
    "M1_EXPORTED_KWH": ["M1 EXPORTED KWH", "m1_exported", "kWh", None],
    "M1_EXPORTED_A_KWH": ["M1 EXPORTED A KWH", "m1_exporteda", "kWh", None],
    "M1_EXPORTED_B_KWH": ["M1 EXPORTED B KWH", "m1_exportedb", "kWh", None],
    "M1_EXPORTED_C_KWH": ["M1 EXPORTED C KWH", "m1_exportedc", "kWh", None],
    "M1_IMPORTED_KWH": ["M1 IMPORTED KWH", "m1_imported", "kWh", None],
    "M1_IMPORTED_KWH_A": ["M1 IMPORTED A KWH", "m1_importeda", "kWh", None],
    "M1_IMPORTED_KWH_B": ["M1 IMPORTED B KWH", "m1_importedb", "kWh", None],
    "M1_IMPORTED_KWH_C": ["M1 IMPORTED C KWH", "m1_importedc", "kWh", None],
    "M1_EXPORTED_VA": ["M1 EXPORTED VAh", "m1_exportedva", "VAh", None],
    "M1_EXPORTED_VA_A": ["M1 EXPORTED A VAh", "m1_exportedvaa", "VAh", None],
    "M1_EXPORTED_VA_B": ["M1 EXPORTED B VAh", "m1_exportedvab", "VAh", None],
    "M1_EXPORTED_VA_C": ["M1 EXPORTED C VAh", "m1_exportedvac", "VAh", None],
    "M1_IMPORTED_VA": ["M1 IMPORTED VAh", "m1_importedva", "VAh", None],
    "M1_IMPORTED_VA_A": ["M1 IMPORTED A VAh", "m1_importedvaa", "VAh", None],
    "M1_IMPORTED_VA_B": ["M1 IMPORTED B VAh", "m1_importedvab", "VAh", None],
    "M1_IMPORTED_VA_C": ["M1 IMPORTED C VAh", "m1_importedvac", "VAh", None],
    "M1_IMPORT_VARH_Q1": ["M1 IMPORT VARH Q1", "m1_importvarhq1", "VARh", None],
    "M1_IMPORT_VARH_Q1_A": ["M1 IMPORT VARH Q1 A", "m1_importvarhq1a", "VARh", None],
    "M1_IMPORT_VARH_Q1_B": ["M1 IMPORT VARH Q1 B", "m1_importvarhq1b", "VARh", None],
    "M1_IMPORT_VARH_Q1_C": ["M1 IMPORT VARH Q1 C", "m1_importvarhq1c", "VARh", None],
    "M1_IMPORT_VARH_Q2": ["M1 IMPORT VARH Q2", "m1_importvarhq2", "VARh", None],
    "M1_IMPORT_VARH_Q2_A": ["M1 IMPORT VARH Q2 A", "m1_importvarhq2a", "VARh", None],
    "M1_IMPORT_VARH_Q2_B": ["M1 IMPORT VARH Q2 B", "m1_importvarhq2b", "VARh", None],
    "M1_IMPORT_VARH_Q2_C": ["M1 IMPORT VARH Q2 C", "m1_importvarhq2c", "VARh", None],
    "M1_IMPORT_VARH_Q3": ["M1 IMPORT VARH Q3", "m1_importvarhq3", "VARh", None],
    "M1_IMPORT_VARH_Q3_A": ["M1 IMPORT VARH Q3 A", "m1_importvarhq3a", "VARh", None],
    "M1_IMPORT_VARH_Q3_B": ["M1 IMPORT VARH Q3 B", "m1_importvarhq3b", "VARh", None],
    "M1_IMPORT_VARH_Q3_C": ["M1 IMPORT VARH Q3 C", "m1_importvarhq3c", "VARh", None],
    "M1_IMPORT_VARH_Q4": ["M1 IMPORT VARH Q4", "m1_importvarhq4", "VARh", None],
    "M1_IMPORT_VARH_Q4_A": ["M1 IMPORT VARH Q4 A", "m1_importvarhq4a", "VARh", None],
    "M1_IMPORT_VARH_Q4_B": ["M1 IMPORT VARH Q4 B", "m1_importvarhq4b", "VARh", None],
    "M1_IMPORT_VARH_Q4_C": ["M1 IMPORT VARH Q4 C", "m1_importvarhq4c", "VARh", None],
}

METER2_SENSOR_TYPES = {
    "M2_AC_Current": ["M2 AC Current", "m2_accurrent", "A", "mdi:current-ac"],
    "M2_AC_Current_A": ["M2 AC Current_A", "m2_accurrenta", "A", "mdi:current-ac"],
    "M2_AC_Current_B": ["M2 AC Current_B", "m2_accurrentb", "A", "mdi:current-ac"],
    "M2_AC_Current_C": ["M2 AC Current_C", "m2_accurrentc", "A", "mdi:current-ac"],
    "M2_AC_Voltage_LN": ["M2 AC Voltage LN", "m2_acvoltageln", "V", None],
    "M2_AC_Voltage_AN": ["M2 AC Voltage AN", "m2_acvoltagean", "V", None],
    "M2_AC_Voltage_BN": ["M2 AC Voltage BN", "m2_acvoltagebn", "V", None],
    "M2_AC_Voltage_CN": ["M2 AC Voltage CN", "m2_acvoltagecn", "V", None],
    "M2_AC_Voltage_LL": ["M2 AC Voltage LL", "m2_acvoltagell", "V", None],
    "M2_AC_Voltage_AB": ["M2 AC Voltage AB", "m2_acvoltageab", "V", None],
    "M2_AC_Voltage_BC": ["M2 AC Voltage BC", "m2_acvoltagebc", "V", None],
    "M2_AC_Voltage_CA": ["M2 AC Voltage CA", "m2_acvoltageca", "V", None],
    "M2_AC_Frequency": ["M2 AC Frequency", "m2_acfreq", "Hz", None],
    "M2_AC_Power": ["M2 AC Power", "m2_acpower", "W", None],
    "M2_AC_Power_A": ["M2 AC Power A", "m2_acpowera", "W", None],
    "M2_AC_Power_B": ["M2 AC Power B", "m2_acpowerb", "W", None],
    "M2_AC_Power_C": ["M2 AC Power C", "m2_acpowerc", "W", None],
    "M2_AC_VA": ["M2 AC VA", "m2_acva", "VA", None],
    "M2_AC_VA_A": ["M2 AC VA A", "m2_acvaa", "VA", None],
    "M2_AC_VA_B": ["M2 AC VA B", "m2_acvab", "VA", None],
    "M2_AC_VA_C": ["M2 AC VA C", "m2_acvac", "VA", None],
    "M2_AC_VAR": ["M2 AC VAR", "m2_acvar", "VAR", None],
    "M2_AC_VAR_A": ["M2 AC VAR A", "m2_acvara", "VAR", None],
    "M2_AC_VAR_B": ["M2 AC VAR B", "m2_acvarb", "VAR", None],
    "M2_AC_VAR_C": ["M2 AC VAR C", "m2_acvarc", "VAR", None],
    "M2_AC_PF": ["M2 AC PF", "m2_acpf", "%", None],
    "M2_AC_PF_A": ["M2 AC PF A", "m2_acpfa", "%", None],
    "M2_AC_PF_B": ["M2 AC PF B", "m2_acpfb", "%", None],
    "M2_AC_PF_C": ["M2 AC PF C", "m2_acpfc", "%", None],
    "M2_EXPORTED_KWH": ["M2 EXPORTED KWH", "m2_exported", "kWh", None],
    "M2_EXPORTED_A_KWH": ["M2 EXPORTED A KWH", "m2_exporteda", "kWh", None],
    "M2_EXPORTED_B_KWH": ["M2 EXPORTED B KWH", "m2_exportedb", "kWh", None],
    "M2_EXPORTED_C_KWH": ["M2 EXPORTED C KWH", "m2_exportedc", "kWh", None],
    "M2_IMPORTED_KWH": ["M2 IMPORTED KWH", "m2_imported", "kWh", None],
    "M2_IMPORTED_KWH_A": ["M2 IMPORTED A KWH", "m2_importeda", "kWh", None],
    "M2_IMPORTED_KWH_B": ["M2 IMPORTED B KWH", "m2_importedb", "kWh", None],
    "M2_IMPORTED_KWH_C": ["M2 IMPORTED C KWH", "m2_importedc", "kWh", None],
    "M2_EXPORTED_VA": ["M2 EXPORTED VAh", "m2_exportedva", "VAh", None],
    "M2_EXPORTED_VA_A": ["M2 EXPORTED A VAh", "m2_exportedvaa", "VAh", None],
    "M2_EXPORTED_VA_B": ["M2 EXPORTED B VAh", "m2_exportedvab", "VAh", None],
    "M2_EXPORTED_VA_C": ["M2 EXPORTED C VAh", "m2_exportedvac", "VAh", None],
    "M2_IMPORTED_VA": ["M2 IMPORTED VAh", "m2_importedva", "VAh", None],
    "M2_IMPORTED_VA_A": ["M2 IMPORTED A VAh", "m2_importedvaa", "VAh", None],
    "M2_IMPORTED_VA_B": ["M2 IMPORTED B VAh", "m2_importedvab", "VAh", None],
    "M2_IMPORTED_VA_C": ["M2 IMPORTED C VAh", "m2_importedvac", "VAh", None],
    "M2_IMPORT_VARH_Q1": ["M2 IMPORT VARH Q1", "m2_importvarhq1", "VARh", None],
    "M2_IMPORT_VARH_Q1_A": ["M2 IMPORT VARH Q1 A", "m2_importvarhq1a", "VARh", None],
    "M2_IMPORT_VARH_Q1_B": ["M2 IMPORT VARH Q1 B", "m2_importvarhq1b", "VARh", None],
    "M2_IMPORT_VARH_Q1_C": ["M2 IMPORT VARH Q1 C", "m2_importvarhq1c", "VARh", None],
    "M2_IMPORT_VARH_Q2": ["M2 IMPORT VARH Q2", "m2_importvarhq2", "VARh", None],
    "M2_IMPORT_VARH_Q2_A": ["M2 IMPORT VARH Q2 A", "m2_importvarhq2a", "VARh", None],
    "M2_IMPORT_VARH_Q2_B": ["M2 IMPORT VARH Q2 B", "m2_importvarhq2b", "VARh", None],
    "M2_IMPORT_VARH_Q2_C": ["M2 IMPORT VARH Q2 C", "m2_importvarhq2c", "VARh", None],
    "M2_IMPORT_VARH_Q3": ["M2 IMPORT VARH Q3", "m2_importvarhq3", "VARh", None],
    "M2_IMPORT_VARH_Q3_A": ["M2 IMPORT VARH Q3 A", "m2_importvarhq3a", "VARh", None],
    "M2_IMPORT_VARH_Q3_B": ["M2 IMPORT VARH Q3 B", "m2_importvarhq3b", "VARh", None],
    "M2_IMPORT_VARH_Q3_C": ["M2 IMPORT VARH Q3 C", "m2_importvarhq3c", "VARh", None],
    "M2_IMPORT_VARH_Q4": ["M2 IMPORT VARH Q4", "m2_importvarhq4", "VARh", None],
    "M2_IMPORT_VARH_Q4_A": ["M2 IMPORT VARH Q4 A", "m2_importvarhq4a", "VARh", None],
    "M2_IMPORT_VARH_Q4_B": ["M2 IMPORT VARH Q4 B", "m2_importvarhq4b", "VARh", None],
    "M2_IMPORT_VARH_Q4_C": ["M2 IMPORT VARH Q4 C", "m2_importvarhq4c", "VARh", None],
}

METER3_SENSOR_TYPES = {
    "M3_AC_Current": ["M3 AC Current", "m3_accurrent", "A", "mdi:current-ac"],
    "M3_AC_Current_A": ["M3 AC Current_A", "m3_accurrenta", "A", "mdi:current-ac"],
    "M3_AC_Current_B": ["M3 AC Current_B", "m3_accurrentb", "A", "mdi:current-ac"],
    "M3_AC_Current_C": ["M3 AC Current_C", "m3_accurrentc", "A", "mdi:current-ac"],
    "M3_AC_Voltage_LN": ["M3 AC Voltage LN", "m3_acvoltageln", "V", None],
    "M3_AC_Voltage_AN": ["M3 AC Voltage AN", "m3_acvoltagean", "V", None],
    "M3_AC_Voltage_BN": ["M3 AC Voltage BN", "m3_acvoltagebn", "V", None],
    "M3_AC_Voltage_CN": ["M3 AC Voltage CN", "m3_acvoltagecn", "V", None],
    "M3_AC_Voltage_LL": ["M3 AC Voltage LL", "m3_acvoltagell", "V", None],
    "M3_AC_Voltage_AB": ["M3 AC Voltage AB", "m3_acvoltageab", "V", None],
    "M3_AC_Voltage_BC": ["M3 AC Voltage BC", "m3_acvoltagebc", "V", None],
    "M3_AC_Voltage_CA": ["M3 AC Voltage CA", "m3_acvoltageca", "V", None],
    "M3_AC_Frequency": ["M3 AC Frequency", "m3_acfreq", "Hz", None],
    "M3_AC_Power": ["M3 AC Power", "m3_acpower", "W", None],
    "M3_AC_Power_A": ["M3 AC Power A", "m3_acpowera", "W", None],
    "M3_AC_Power_B": ["M3 AC Power B", "m3_acpowerb", "W", None],
    "M3_AC_Power_C": ["M3 AC Power C", "m3_acpowerc", "W", None],
    "M3_AC_VA": ["M3 AC VA", "m3_acva", "VA", None],
    "M3_AC_VA_A": ["M3 AC VA A", "m3_acvaa", "VA", None],
    "M3_AC_VA_B": ["M3 AC VA B", "m3_acvab", "VA", None],
    "M3_AC_VA_C": ["M3 AC VA C", "m3_acvac", "VA", None],
    "M3_AC_VAR": ["M3 AC VAR", "m3_acvar", "VAR", None],
    "M3_AC_VAR_A": ["M3 AC VAR A", "m3_acvara", "VAR", None],
    "M3_AC_VAR_B": ["M3 AC VAR B", "m3_acvarb", "VAR", None],
    "M3_AC_VAR_C": ["M3 AC VAR C", "m3_acvarc", "VAR", None],
    "M3_AC_PF": ["M3 AC PF", "m3_acpf", "%", None],
    "M3_AC_PF_A": ["M3 AC PF A", "m3_acpfa", "%", None],
    "M3_AC_PF_B": ["M3 AC PF B", "m3_acpfb", "%", None],
    "M3_AC_PF_C": ["M3 AC PF C", "m3_acpfc", "%", None],
    "M3_EXPORTED_KWH": ["M3 EXPORTED KWH", "m3_exported", "kWh", None],
    "M3_EXPORTED_A_KWH": ["M3 EXPORTED A KWH", "m3_exporteda", "kWh", None],
    "M3_EXPORTED_B_KWH": ["M3 EXPORTED B KWH", "m3_exportedb", "kWh", None],
    "M3_EXPORTED_C_KWH": ["M3 EXPORTED C KWH", "m3_exportedc", "kWh", None],
    "M3_IMPORTED_KWH": ["M3 IMPORTED KWH", "m3_imported", "kWh", None],
    "M3_IMPORTED_KWH_A": ["M3 IMPORTED A KWH", "m3_importeda", "kWh", None],
    "M3_IMPORTED_KWH_B": ["M3 IMPORTED B KWH", "m3_importedb", "kWh", None],
    "M3_IMPORTED_KWH_C": ["M3 IMPORTED C KWH", "m3_importedc", "kWh", None],
    "M3_EXPORTED_VA": ["M3 EXPORTED VAh", "m3_exportedva", "VAh", None],
    "M3_EXPORTED_VA_A": ["M3 EXPORTED A VAh", "m3_exportedvaa", "VAh", None],
    "M3_EXPORTED_VA_B": ["M3 EXPORTED B VAh", "m3_exportedvab", "VAh", None],
    "M3_EXPORTED_VA_C": ["M3 EXPORTED C VAh", "m3_exportedvac", "VAh", None],
    "M3_IMPORTED_VA": ["M3 IMPORTED VAh", "m3_importedva", "VAh", None],
    "M3_IMPORTED_VA_A": ["M3 IMPORTED A VAh", "m3_importedvaa", "VAh", None],
    "M3_IMPORTED_VA_B": ["M3 IMPORTED B VAh", "m3_importedvab", "VAh", None],
    "M3_IMPORTED_VA_C": ["M3 IMPORTED C VAh", "m3_importedvac", "VAh", None],
    "M3_IMPORT_VARH_Q1": ["M3 IMPORT VARH Q1", "m3_importvarhq1", "VARh", None],
    "M3_IMPORT_VARH_Q1_A": ["M3 IMPORT VARH Q1 A", "m3_importvarhq1a", "VARh", None],
    "M3_IMPORT_VARH_Q1_B": ["M3 IMPORT VARH Q1 B", "m3_importvarhq1b", "VARh", None],
    "M3_IMPORT_VARH_Q1_C": ["M3 IMPORT VARH Q1 C", "m3_importvarhq1c", "VARh", None],
    "M3_IMPORT_VARH_Q2": ["M3 IMPORT VARH Q2", "m3_importvarhq2", "VARh", None],
    "M3_IMPORT_VARH_Q2_A": ["M3 IMPORT VARH Q2 A", "m3_importvarhq2a", "VARh", None],
    "M3_IMPORT_VARH_Q2_B": ["M3 IMPORT VARH Q2 B", "m3_importvarhq2b", "VARh", None],
    "M3_IMPORT_VARH_Q2_C": ["M3 IMPORT VARH Q2 C", "m3_importvarhq2c", "VARh", None],
    "M3_IMPORT_VARH_Q3": ["M3 IMPORT VARH Q3", "m3_importvarhq3", "VARh", None],
    "M3_IMPORT_VARH_Q3_A": ["M3 IMPORT VARH Q3 A", "m3_importvarhq3a", "VARh", None],
    "M3_IMPORT_VARH_Q3_B": ["M3 IMPORT VARH Q3 B", "m3_importvarhq3b", "VARh", None],
    "M3_IMPORT_VARH_Q3_C": ["M3 IMPORT VARH Q3 C", "m3_importvarhq3c", "VARh", None],
    "M3_IMPORT_VARH_Q4": ["M3 IMPORT VARH Q4", "m3_importvarhq4", "VARh", None],
    "M3_IMPORT_VARH_Q4_A": ["M3 IMPORT VARH Q4 A", "m3_importvarhq4a", "VARh", None],
    "M3_IMPORT_VARH_Q4_B": ["M3 IMPORT VARH Q4 B", "m3_importvarhq4b", "VARh", None],
    "M3_IMPORT_VARH_Q4_C": ["M3 IMPORT VARH Q4 C", "m3_importvarhq4c", "VARh", None],
}

STORAGE_SENSOR_TYPES = {
    "STORAGE_Power": ["Storage AC Power", "storage_power", "W", "mdi:battery-charging-100"],
    "STORAGE_SOC": ["Storage State of Charge", "storage_soc", "%", "mdi:battery-high"],
    "STORAGE_Status": ["Storage Status", "storage_status", None, None],
}

DEVICE_STATUSSES = {
    1: "Off",
    2: "Sleeping (auto-shutdown) – Night mode",
    3: "Grid Monitoring/wake-up",
    4: "Inverter is ON and producing power",
    5: "Production (curtailed)",
    6: "Shutting down",
    7: "Fault",
    8: "Maintenance/setup",
}

STORAGE_STATUSSES = {
    0: "Unknown",
    1: "Off",
    2: "Unknown",
    3: "Charging",
    4: "Discharging",
    5: "Unknown",
    6: "Conservation"
}
