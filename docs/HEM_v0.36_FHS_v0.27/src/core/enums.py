"""
Enums used across the input schema and potentially other modules.
Extracted from input.py for better code organization.
"""

from enum import StrEnum, IntEnum


class ApplianceReference(StrEnum):
    DEFAULT = "Default"
    NOT_INSTALLED = "Not Installed"


class BatteryLocation(StrEnum):
    INSIDE = "inside"
    OUTSIDE = "outside"


class BoilerHotWaterTest(StrEnum):
    M_L = "M&L"
    M_S = "M&S"
    M_ONLY = "M_only"
    NO_ADDITIONAL_TESTS = "No_additional_tests"


class ControlCombinationOperation(StrEnum):
    AND_ = "AND"
    OR_ = "OR"
    XOR = "XOR"
    NOT_ = "NOT"
    MAX = "MAX"
    MIN = "MIN"
    MEAN = "MEAN"


class ControlLogicType(StrEnum):
    CELECT = "celect"
    HEAT_BATTERY = "heat_battery"
    HHRSH = "hhrsh"
    AUTOMATIC = "automatic"
    MANUAL = "manual"


class DaylightSavingsConfig(StrEnum):
    APPLICABLE_AND_TAKEN_INTO_ACCOUNT = "applicable and taken into account"
    APPLICABLE_BUT_NOT_TAKEN_INTO_ACCOUNT = "applicable but not taken into account"
    NOT_APPLICABLE = "not applicable"


class DiverterHeatSourceType(StrEnum):
    IMMERSION = "immersion"


class DuctShape(StrEnum):
    CIRCULAR = "circular"
    RECTANGULAR = "rectangular"


class DuctType(StrEnum):
    INTAKE = "intake"
    SUPPLY = "supply"
    EXTRACT = "extract"
    EXHAUST = "exhaust"


class EcoDesignControllerClass(IntEnum):
    # TODO Duplicates src/core/heating_systems/emitters.py, reconcile these.
    CLASS_I = 1
    "On/off room thermostat"
    CLASS_II = 2
    "Weather compensator with modulating heaters"
    CLASS_III = 3
    "Weather compensator with on/off heaters"
    CLASS_IV = 4
    "TPI room thermostat with on/off heaters"
    CLASS_V = 5
    "Modulating room thermostat with modulating heaters"
    CLASS_VI = 6
    "Weather compensator with room sensor for modulating heaters"
    CLASS_VII = 7
    "Weather compensator with room sensor for on/off heaters"
    CLASS_VIII = 8
    "Multi room temperature control with modulating heaters"


class FloorType(StrEnum):
    SLAB_NO_EDGE_INSULATION = "Slab_no_edge_insulation"
    SLAB_EDGE_INSULATION = "Slab_edge_insulation"
    SUSPENDED_FLOOR = "Suspended_floor"
    HEATED_BASEMENT = "Heated_basement"
    UNHEATED_BASEMENT = "Unheated_basement"


class FuelType(StrEnum):
    LPG_BOTTLED = "LPG_bottled"
    LPG_BULK = "LPG_bulk"
    LPG_CONDITION_11_F = "LPG_condition_11F"
    CUSTOM = "custom"
    ELECTRICITY = "electricity"
    ENERGY_FROM_ENVIRONMENT = "energy_from_environment"
    MAINS_GAS = "mains_gas"
    UNMET_DEMAND = "unmet_demand"


class HeatPumpBackupControlType(StrEnum):
    NONE = "None"
    TOP_UP = "TopUp"
    SUBSTITUTE = "Substitute"


class HeatPumpSinkType(StrEnum):
    WATER = "Water"
    AIR = "Air"
    GLYCOL25 = "Glycol25"


class HeatPumpSourceType(StrEnum):
    GROUND = "Ground"
    OUTSIDE_AIR = "OutsideAir"
    EXHAUST_AIR_MEV = "ExhaustAirMEV"
    EXHAUST_AIR_MVHR = "ExhaustAirMVHR"
    EXHAUST_AIR_MIXED = "ExhaustAirMixed"
    WATER_GROUND = "WaterGround"
    WATER_SURFACE = "WaterSurface"
    HEAT_NETWORK = "HeatNetwork"


class HeatSourceLocation(StrEnum):
    INTERNAL = "internal"
    EXTERNAL = "external"


class InverterType(StrEnum):
    OPTIMISED_INVERTER = "optimised_inverter"
    STRING_INVERTER = "string_inverter"


class MVHRLocation(StrEnum):
    INSIDE = "inside"
    OUTSIDE = "outside"


class MassDistributionClass(StrEnum):
    D = "D"
    E = "E"
    I = "I"  # noqa: E741  # Ambiguous variable name: `I`
    IE = "IE"
    M = "M"


class PhotovoltaicVentilationStrategy(StrEnum):
    UNVENTILATED = "unventilated"
    MODERATELY_VENTILATED = "moderately_ventilated"
    STRONGLY_OR_FORCED_VENTILATED = "strongly_or_forced_ventilated"
    REAR_SURFACE_FREE = "rear_surface_free"


class EnergySupplyPriorityEntry(StrEnum):
    ELECTRIC_BATTERY = "ElectricBattery"
    DIVERTER = "diverter"


class ShadingObjectType(StrEnum):
    OBSTACLE = "obstacle"
    OVERHANG = "overhang"


class SolarCollectorLoopLocation(StrEnum):
    """Location of the main part of the solar thermal collector loop piping.

    This affects the ambient temperature used for heat loss calculations
    in the collector loop piping.
    """

    OUT = "OUT"
    "Outside - collector loop piping is located outdoors, uses external air temperature"

    HS = "HS"
    "Heated Space - collector loop piping is in heated space, uses internal air temperature"

    NHS = "NHS"
    "Non-Heated Space - collector loop piping is in unheated space, uses average of internal and external temperatures"


class SpaceCoolSystemType(StrEnum):
    AIR_CONDITIONING = "AirConditioning"


class AirFlowType(StrEnum):
    FAN_ASSISTED = "fan-assisted"
    DAMPER_ONLY = "damper-only"


class SupplyAirFlowRateControlType(StrEnum):
    ODA = "ODA"


class SupplyAirTemperatureControlType(StrEnum):
    CONST = "CONST"
    NO_CTRL = "NO_CTRL"
    LOAD_COM = "LOAD_COM"


class TerrainClass(StrEnum):
    OPEN_WATER = "OpenWater"
    OPEN_FIELD = "OpenField"
    SUBURBAN = "Suburban"
    URBAN = "Urban"


class TestLetter(StrEnum):
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    F = "F"


class MechVentType(StrEnum):
    INTERMITTENT_MEV = "Intermittent MEV"
    CENTRALISED_CONTINUOUS_MEV = "Centralised continuous MEV"
    DECENTRALISED_CONTINUOUS_MEV = "Decentralised continuous MEV"
    MVHR = "MVHR"


class VentilationShieldClass(StrEnum):
    OPEN = "Open"
    NORMAL = "Normal"
    SHIELDED = "Shielded"


class WaterPipeContentsType(StrEnum):
    WATER = "water"
    GLYCOL25 = "glycol25"


class WaterPipeworkLocation(StrEnum):
    INTERNAL = "internal"
    EXTERNAL = "external"


class WindShieldLocation(StrEnum):
    SHELTERED = "Sheltered"
    AVERAGE = "Average"
    EXPOSED = "Exposed"


class WindowShadingType(StrEnum):
    OVERHANG = "overhang"
    SIDEFINRIGHT = "sidefinright"
    SIDEFINLEFT = "sidefinleft"
    REVEAL = "reveal"


class WindowTreatmentControl(StrEnum):
    AUTO_MOTORISED = "auto_motorised"
    COMBINED_LIGHT_BLIND_HVAC = "combined_light_blind_HVAC"
    MANUAL = "manual"
    MANUAL_MOTORISED = "manual_motorised"


class WindowTreatmentType(StrEnum):
    BLINDS = "blinds"
    CURTAINS = "curtains"


class WasteWaterHeatRecoverySystemType(StrEnum):
    INSTANTANEOUS_SYSTEM_A = "WWHRS_InstantaneousSystemA"
    INSTANTANEOUS_SYSTEM_B = "WWHRS_InstantaneousSystemB"
    INSTANTANEOUS_SYSTEM_C = "WWHRS_InstantaneousSystemC"


class ZoneTemperatureControlBasis(StrEnum):
    AIR = "air"
    OPERATIVE = "operative"


# FHS-specific enums
class EnergySupplyType(StrEnum):
    MAINS_ELECTRIC = "mains elec"
    MAINS_GAS = "mains gas"


class HeatingControlType(StrEnum):
    SEPARATE_TIME_AND_TEMP_CONTROL = "SeparateTimeAndTempControl"
    SEPARATE_TEMP_CONTROL = "SeparateTempControl"


class SpaceHeatControlType(StrEnum):
    LIVINGROOM = "livingroom"
    RESTOFDWELLING = "restofdwelling"


class BuildType(StrEnum):
    HOUSE = "house"
    FLAT = "flat"


class CombustionAirSupplySituation(StrEnum):
    ROOM_AIR = "room_air"
    OUTSIDE = "outside"


class CombustionApplianceType(StrEnum):
    OPEN_FIREPLACE = "open_fireplace"
    CLOSED_WITH_FAN = "closed_with_fan"
    OPEN_GAS_FLUE_BALANCER = "open_gas_flue_balancer"
    OPEN_GAS_KITCHEN_STOVE = "open_gas_kitchen_stove"
    OPEN_GAS_FIRE = "open_gas_fire"
    CLOSED_FIRE = "closed_fire"


class CombustionFuelType(StrEnum):
    WOOD = "wood"
    GAS = "gas"
    OIL = "oil"
    COAL = "coal"


class FlueGasExhaustSituation(StrEnum):
    INTO_ROOM = "into_room"
    INTO_SEPARATE_DUCT = "into_separate_duct"
    INTO_MECH_VENT = "into_mech_vent"


class WaterHeatingSchedule(StrEnum):
    ALL_DAY = "AllDay"
    HEATING_HOURS = "HeatingHours"
