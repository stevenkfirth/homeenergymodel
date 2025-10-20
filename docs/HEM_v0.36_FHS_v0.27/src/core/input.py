from pydantic import BaseModel, ConfigDict, Field, RootModel, model_validator
from typing import Annotated, Literal, Optional, Self, Union

# Import all enums from the new enums module
from .enums import (
    ApplianceReference,
    BatteryLocation,
    BoilerHotWaterTest,
    ControlCombinationOperation,
    ControlLogicType,
    DuctShape,
    DuctType,
    EcoDesignControllerClass,
    FloorType,
    FuelType,
    HeatPumpBackupControlType,
    HeatPumpSinkType,
    HeatPumpSourceType,
    HeatSourceLocation,
    InverterType,
    MVHRLocation,
    MassDistributionClass,
    PhotovoltaicVentilationStrategy,
    EnergySupplyPriorityEntry,
    ShadingObjectType,
    SolarCollectorLoopLocation,
    AirFlowType,
    SupplyAirFlowRateControlType,
    SupplyAirTemperatureControlType,
    TerrainClass,
    TestLetter,
    MechVentType,
    VentilationShieldClass,
    WaterPipeContentsType,
    WaterPipeworkLocation,
    WindShieldLocation,
    WindowShadingType,
    WindowTreatmentControl,
    WindowTreatmentType,
    WasteWaterHeatRecoverySystemType,
    ZoneTemperatureControlBasis,
)


# Common type definitions for reuse
PitchAngle = Annotated[
    float,
    Field(
        description="Tilt angle of the surface from horizontal, between 0 and 180, where 0 means the external surface is facing up, 90 means the external surface is vertical and 180 means the external surface is facing down (unit: ˚)"
    ),
]

PitchAnglePV = Annotated[
    float,
    Field(
        description="The tilt angle (inclination) of the PV panel from horizontal, measured upwards facing, 0 to 90 (unit: ˚)"
    ),
]

Orientation360 = Annotated[
    float,
    Field(
        description="The orientation angle of the inclined surface, expressed as the geographical azimuth angle of the horizontal projection of the inclined surface normal, 0 to 360 (unit: ˚)"
    ),
]


class StrictBaseModel(BaseModel):
    """Base model class that forbids extra fields by default."""

    model_config = ConfigDict(extra="forbid")


class AirTerminalDevice(StrictBaseModel):
    area_cm2: float
    pressure_difference_ref: float


class ApplianceGainsEvent(StrictBaseModel):
    demand_w: Annotated[float, Field(alias="demand_W")]
    duration: float
    start: float


class ApplianceLoadShifting(StrictBaseModel):
    control: Annotated[Optional[str], Field(alias="Control")] = None
    demand_limit_weighted: float
    max_shift_hrs: float
    priority: Optional[int] = None
    weight_timeseries: list[float]


class ColdWaterSource(StrictBaseModel):
    start_day: Annotated[
        int,
        Field(description="First day of the time series, day of the year, 0 to 365", ge=0, le=365),
    ]
    temperatures: Annotated[
        list[float],
        Field(description="List of cold water temperatures, one entry per hour (unit: ˚C)"),
    ]
    time_series_step: Annotated[
        float, Field(description="Timestep of the time series data (unit: hours)")
    ]


class CustomEnergySourceFactor(StrictBaseModel):
    emissions_factor_kg_co2e_k_wh: Annotated[float, Field(alias="Emissions Factor kgCO2e/kWh")]
    emissions_factor_kg_co2e_k_wh_including_out_of_scope_emissions: Annotated[
        float, Field(alias="Emissions Factor kgCO2e/kWh including out-of-scope emissions")
    ]
    primary_energy_factor_k_wh_k_wh_delivered: Annotated[
        float, Field(alias="Primary Energy Factor kWh/kWh delivered")
    ]


class EdgeInsulationHorizontal(StrictBaseModel):
    type: Literal["horizontal"]
    edge_thermal_resistance: float
    width: float


class EdgeInsulationVertical(StrictBaseModel):
    type: Literal["vertical"]
    edge_thermal_resistance: float
    depth: float


EdgeInsulation = Annotated[
    Union[EdgeInsulationHorizontal, EdgeInsulationVertical],
    Field(discriminator="type"),
]


class ElectricBattery(StrictBaseModel):
    battery_age: float
    battery_location: BatteryLocation
    capacity: float
    charge_discharge_efficiency_round_trip: float
    grid_charging_possible: bool
    maximum_charge_rate_one_way_trip: float
    maximum_discharge_rate_one_way_trip: float
    minimum_charge_rate_one_way_trip: float


class ExternalSensorCorrelation(StrictBaseModel):
    temperature: float
    max_charge: float


class FanSpeedData(StrictBaseModel):
    power_output: list[float]
    temperature_diff: float


class FancoilTestData(StrictBaseModel):
    fan_power_w: Annotated[list[float], Field(alias="fan_power_W")]
    fan_speed_data: list[FanSpeedData]


class HeatPumpBufferTank(StrictBaseModel):
    daily_losses: float
    pump_fixed_flow_rate: float
    pump_power_at_flow_rate: float
    volume: float


class HeatPumpHotWaterOnlyTestDatum(StrictBaseModel):
    cop_dhw: float
    energy_input_measured: float
    hw_tapping_prof_daily_total: float
    hw_vessel_loss_daily: float
    power_standby: float


class HeatPumpHotWaterTestData(StrictBaseModel):
    l: Annotated[Optional[HeatPumpHotWaterOnlyTestDatum], Field(alias="L")] = None  # noqa: E741  # Ambiguous variable name: `l`
    m: Annotated[HeatPumpHotWaterOnlyTestDatum, Field(alias="M")]


class BoilerBase(StrictBaseModel):
    """Base class containing common boiler properties"""

    energy_supply: Annotated[str, Field(alias="EnergySupply")]
    energy_supply_aux: Annotated[str, Field(alias="EnergySupply_aux")]
    boiler_location: HeatSourceLocation
    efficiency_full_load: float
    efficiency_part_load: float
    electricity_circ_pump: float
    electricity_full_load: float
    electricity_part_load: float
    electricity_standby: float
    modulation_load: float
    rated_power: float


class HeatSourceWetBoiler(BoilerBase):
    """Standalone boiler heat source"""

    type: Literal["Boiler"]


class HeatSourceWetHeatBattery(StrictBaseModel):
    type: Literal["HeatBattery"]
    a: Annotated[float, Field(alias="A")]
    b: Annotated[float, Field(alias="B")]
    control_charge: Annotated[str, Field(alias="ControlCharge")]
    energy_supply: Annotated[str, Field(alias="EnergySupply")]
    capillary_diameter_m: float
    electricity_circ_pump: float
    electricity_standby: float
    flow_rate_l_per_min: float
    heat_exchanger_surface_area_m2: float
    heat_storage_zone_material_k_j_per_k_above_phase_transition: Annotated[
        float, Field(alias="heat_storage_zone_material_kJ_per_K_above_Phase_transition")
    ]
    heat_storage_zone_material_k_j_per_k_below_phase_transition: Annotated[
        float, Field(alias="heat_storage_zone_material_kJ_per_K_below_Phase_transition")
    ]
    heat_storage_zone_material_k_j_per_k_during_phase_transition: Annotated[
        float, Field(alias="heat_storage_zone_material_kJ_per_K_during_Phase_transition")
    ]
    max_rated_losses: float
    max_temperature: float
    number_of_units: Annotated[int, Field(ge=0)]
    phase_transition_temperature_upper: float
    phase_transition_temperature_lower: float
    rated_charge_power: float
    simultaneous_charging_and_discharging: bool
    velocity_in_hex_tube_at_1_l_per_min_m_per_s: Annotated[
        float, Field(alias="velocity_in_HEX_tube_at_1_l_per_min_m_per_s")
    ]


class HeatSourceWetHIU(StrictBaseModel):
    type: Literal["HIU"]
    energy_supply: Annotated[str, Field(alias="EnergySupply")]
    hiu_daily_loss: Annotated[float, Field(alias="HIU_daily_loss")]
    building_level_distribution_losses: float
    power_max: float


class HotWaterSourceCombiBoiler(StrictBaseModel):
    type: Literal["CombiBoiler"]
    cold_water_source: Annotated[str, Field(alias="ColdWaterSource")]
    heat_source_wet: Annotated[str, Field(alias="HeatSourceWet")]
    daily_hw_usage: Annotated[float, Field(alias="daily_HW_usage")]
    rejected_energy_1: Optional[float] = None
    rejected_factor_3: Optional[float] = None
    separate_dhw_tests: Annotated[BoilerHotWaterTest, Field(alias="separate_DHW_tests")]
    setpoint_temp: float
    storage_loss_factor_2: Optional[float] = None


class HotWaterSourceHUI(StrictBaseModel):
    type: Literal["HIU"]
    cold_water_source: Annotated[str, Field(alias="ColdWaterSource")]
    heat_source_wet: Annotated[str, Field(alias="HeatSourceWet")]
    setpoint_temp: Optional[float] = None


class HotWaterSourcePointOfUse(StrictBaseModel):
    type: Literal["PointOfUse"]
    cold_water_source: Annotated[str, Field(alias="ColdWaterSource")]
    energy_supply: Annotated[str, Field(alias="EnergySupply")]
    efficiency: float
    setpoint_temp: float


class HotWaterSourceHeatBattery(StrictBaseModel):
    type: Literal["HeatBattery"]
    cold_water_source: Annotated[str, Field(alias="ColdWaterSource")]
    heat_source_wet: Annotated[str, Field(alias="HeatSourceWet")]


class MechanicalVentilationDuctwork(StrictBaseModel):
    cross_section_shape: DuctShape
    duct_perimeter_mm: Optional[float] = None
    duct_type: DuctType
    external_diameter_mm: Optional[float] = None
    insulation_thermal_conductivity: float
    insulation_thickness_mm: float
    internal_diameter_mm: Optional[float] = None
    length: float
    reflective: bool


class OtherWaterUse(StrictBaseModel):
    cold_water_source: Annotated[str, Field(alias="ColdWaterSource")]
    flowrate: Annotated[float, Field(description="Tap/outlet flow rate (unit: litre/minute)")]


class ScheduleRepeaterEntryForBoolean(RootModel[Optional[bool]]):
    root: Optional[bool]


class ScheduleRepeaterEntryForDouble(RootModel[Optional[float]]):
    root: Optional[float]


class ScheduleRepeaterValueForBoolean(RootModel[Union[str, ScheduleRepeaterEntryForBoolean]]):
    root: Union[str, ScheduleRepeaterEntryForBoolean]


class ScheduleRepeaterValueForDouble(RootModel[Union[str, ScheduleRepeaterEntryForDouble]]):
    root: Union[str, ScheduleRepeaterEntryForDouble]


class ScheduleRepeaterForBoolean(StrictBaseModel):
    repeat: Annotated[int, Field(ge=0)]
    value: ScheduleRepeaterValueForBoolean


class ScheduleRepeaterForDouble(StrictBaseModel):
    repeat: Annotated[int, Field(ge=0)]
    value: ScheduleRepeaterValueForDouble


class ShowerMixer(StrictBaseModel):
    type: Literal["MixerShower"]
    cold_water_source: Annotated[str, Field(alias="ColdWaterSource")]
    waste_water_heat_recovery_system: Annotated[
        Optional[str],
        Field(
            alias="WWHRS",
            description="Reference to a key in Input.WWHRS",
        ),
    ] = None
    flowrate: Annotated[float, Field(description="Shower flow rate (unit: litre/minute)")]


class ShowerInstantElectric(StrictBaseModel):
    type: Literal["InstantElecShower"]
    cold_water_source: Annotated[str, Field(alias="ColdWaterSource")]
    energy_supply: Annotated[str, Field(alias="EnergySupply")]
    rated_power: float


Shower = Annotated[
    Union[ShowerMixer, ShowerInstantElectric],
    Field(discriminator="type"),
]


class SimulationTime(StrictBaseModel):
    end: float
    start: float
    step: float


class SmartApplianceBattery(StrictBaseModel):
    battery_state_of_charge: dict[str, list[float]]
    energy_into_battery_from_generation: dict[str, list[float]]
    energy_into_battery_from_grid: dict[str, list[float]]
    energy_out_of_battery: dict[str, list[float]]


class SmartApplianceControl(StrictBaseModel):
    appliances: Annotated[list[str], Field(alias="Appliances")]
    battery24hr: SmartApplianceBattery
    non_appliance_demand_24hr: dict[str, list[float]]
    power_timeseries: dict[str, list[float]]
    time_series_step: float


class SpaceHeatSystemHeatSource(StrictBaseModel):
    name: str
    temp_flow_limit_upper: Optional[float] = None


class ThermalBridgingLinear(StrictBaseModel):
    type: Literal["ThermalBridgeLinear"]
    length: float
    linear_thermal_transmittance: float


class ThermalBridgingPoint(StrictBaseModel):
    type: Literal["ThermalBridgePoint"]
    heat_transfer_coeff: float


ThermalBridging = Annotated[
    Union[ThermalBridgingLinear, ThermalBridgingPoint],
    Field(discriminator="type"),
]


class Vent(StrictBaseModel):
    area_cm2: float
    mid_height_air_flow_path: float
    orientation360: Orientation360
    pitch: PitchAngle
    pressure_difference_ref: Annotated[
        float,
        Field(description="Reference pressure difference for an air terminal device (unit: Pa)"),
    ]


class VentilationLeaks(StrictBaseModel):
    env_area: Annotated[
        float, Field(description="Reference area of the envelope airtightness index")
    ]
    test_pressure: Annotated[float, Field(description="Reference pressure difference (unit: Pa)")]
    test_result: Annotated[float, Field(description="Flow rate through")]
    ventilation_zone_height: float


class WaterHeatingEvent(StrictBaseModel):
    duration: Optional[float] = None
    start: float
    temperature: float
    volume: Optional[float] = None


class WaterHeatingEvents(StrictBaseModel):
    # Restrict top-level keys to only these predefined categories
    shower: Annotated[Optional[dict[str, list[WaterHeatingEvent]]], Field(alias="Shower")] = None
    bath: Annotated[Optional[dict[str, list[WaterHeatingEvent]]], Field(alias="Bath")] = None
    other: Annotated[Optional[dict[str, list[WaterHeatingEvent]]], Field(alias="Other")] = None


class WaterPipework(StrictBaseModel):
    external_diameter_mm: float
    insulation_thermal_conductivity: float
    insulation_thickness_mm: float
    internal_diameter_mm: float
    length: float
    location: WaterPipeworkLocation
    pipe_contents: WaterPipeContentsType
    surface_reflectivity: bool


class WaterPipeworkSimple(StrictBaseModel):
    # Only the three core fields for the simple pipework class
    internal_diameter_mm: float
    length: float
    location: WaterPipeworkLocation


class WetEmitterRadiator(StrictBaseModel):
    type: Annotated[Literal["radiator"], Field(alias="wet_emitter_type")]
    c: float
    frac_convective: float
    n: float


class WetEmitterUFH(StrictBaseModel):
    type: Annotated[Literal["ufh"], Field(alias="wet_emitter_type")]
    emitter_floor_area: float
    equivalent_specific_thermal_mass: float
    frac_convective: float
    system_performance_factor: float


class WetEmitterFanCoil(StrictBaseModel):
    type: Annotated[Literal["fancoil"], Field(alias="wet_emitter_type")]
    fancoil_test_data: FancoilTestData
    frac_convective: float
    n_units: Annotated[Optional[int], Field(default=1, gt=0)] = 1


WetEmitter = Annotated[
    Union[WetEmitterRadiator, WetEmitterUFH, WetEmitterFanCoil],
    Field(discriminator="type"),
]


class WindowPart(StrictBaseModel):
    mid_height_air_flow_path: float


class WindowShadingObject(StrictBaseModel):
    type: WindowShadingType
    depth: float
    distance: float


class WindowShadingObstacle(StrictBaseModel):
    type: Literal["obstacle"]
    height: float
    distance: float
    transparency: float


WindowShading = Union[WindowShadingObject, WindowShadingObstacle]
# Can't use Field(discriminator="type") because WindowShadingObject.type is an enum.
# Shouldn't need to anyway, the structures are different enough to clearly infer.


class Appliance(StrictBaseModel):
    energysupply: Annotated[Optional[str], Field(alias="Energysupply")] = None
    k_wh_per_100cycle: Annotated[Optional[float], Field(alias="kWh_per_100cycle")] = None
    k_wh_per_annum: Annotated[Optional[float], Field(alias="kWh_per_annum")] = None
    k_wh_per_cycle: Annotated[Optional[float], Field(alias="kWh_per_cycle")] = None
    kg_load: Optional[float] = None
    loadshifting: Optional[ApplianceLoadShifting] = None
    standard_use: Optional[float] = None


# TODO unused? (Generated from ECAS schema)
ApplianceEntry = Union[Appliance, ApplianceReference]


class Bath(StrictBaseModel):
    cold_water_source: Annotated[str, Field(alias="ColdWaterSource")]
    flowrate: Annotated[float, Field(description="Tap/outlet flow rate (unit: litre/minute)")]
    size: Annotated[float, Field(description="Volume held by bath (unit: litre)")]


class BuildingElementOpaque(StrictBaseModel):
    type: Literal["BuildingElementOpaque"]
    area: Annotated[
        float,
        Field(
            description="Net area of the opaque building element (i.e. minus any windows / doors / etc.) (unit: m²)"
        ),
    ]
    areal_heat_capacity: Annotated[float, Field(description="Areal heat capacity (unit: J/m².K)")]
    base_height: Annotated[
        float,
        Field(
            description="The distance between the ground and the lowest edge of the element (unit: m)"
        ),
    ]
    height: Annotated[float, Field(description="The height of the building element (unit: m)")]
    is_unheated_pitched_roof: Optional[bool] = None
    mass_distribution_class: Annotated[
        MassDistributionClass,
        Field(
            description="Mass distribution class of the building element, one of: evenly distributed (D); concentrated on external side (E); concentrated on internal side (I); concentrated on internal and external sides (IE); concentrated in middle (M)."
        ),
    ]
    orientation360: Orientation360
    pitch: PitchAngle
    solar_absorption_coeff: Annotated[
        float,
        Field(description="Solar absorption coefficient at the external surface (dimensionless)"),
    ]
    thermal_resistance_construction: Annotated[
        Optional[float], Field(description="Thermal resistance (unit: m².K/W)")
    ] = None
    u_value: Optional[float] = None
    width: Annotated[float, Field(description="The width of the building element (unit: m)")]


class BuildingElementGroundBase(StrictBaseModel):
    """Base class with fields common to ALL ground building elements"""

    type: Literal["BuildingElementGround"]

    # Geometric properties (used by all types)
    area: Annotated[
        float, Field(description="Area of this building element within the zone (unit: m²)")
    ]
    total_area: Annotated[
        float,
        Field(
            description="Total area of the building element across entire dwelling; if the Floor is divided among several zones, this is the total area across all zones (unit: m²)"
        ),
    ]
    perimeter: Annotated[
        float,
        Field(
            description="Perimeter of the floor; calculated for the entire ground floor, even if it is distributed among several zones (unit: m)"
        ),
    ]

    # Thermal properties (used by all types)
    areal_heat_capacity: Annotated[
        float, Field(description="Areal heat capacity of the ground floor element (unit: J/m2.K)")
    ]
    thermal_resistance_floor_construction: Annotated[
        float,
        Field(
            description="Total thermal resistance of all layers in the floor construction (unit: m².K/W)"
        ),
    ]
    u_value: Annotated[
        float,
        Field(
            description="Steady-state thermal transmittance of floor, including the effect of the ground (calculated for the entire ground floor, even if it is distributed among several zones) (unit: W/m2.K)"
        ),
    ]

    # Junction properties (used by all types)
    psi_wall_floor_junc: Annotated[
        float,
        Field(
            description="Linear thermal transmittance of the junction between the floor and the walls (unit: W/m.K)"
        ),
    ]

    # Surface properties (used by all types)
    mass_distribution_class: MassDistributionClass
    pitch: PitchAngle
    thickness_walls: Annotated[float, Field(description="Thickness of the walls (unit: m)")]

    # Optional common fields
    height_upper_surface: Optional[float] = None
    shield_fact_location: Annotated[
        Optional[WindShieldLocation], Field(description="Wind shielding factor")
    ] = None


class BuildingElementGroundSlabNoEdgeInsulation(BuildingElementGroundBase):
    """Slab floor with no edge insulation - uses init_slab_on_ground_floor_uninsulated_or_all_insulation()"""

    floor_type: Literal[FloorType.SLAB_NO_EDGE_INSULATION]

    # No additional required fields - this is the simplest case
    # Edge insulation not used but could be present (ignored)
    edge_insulation: Optional[list[EdgeInsulation]] = None


class BuildingElementGroundSlabEdgeInsulation(BuildingElementGroundBase):
    """Slab floor with edge insulation - uses init_slab_on_ground_floor_edge_insulated()"""

    floor_type: Literal[FloorType.SLAB_EDGE_INSULATION]

    # Edge insulation is actually used in edge_type() function for this floor type
    edge_insulation: Optional[list[EdgeInsulation]] = None


class BuildingElementGroundSuspendedFloor(BuildingElementGroundBase):
    """Suspended floor - uses init_suspended_floor()"""

    floor_type: Literal[FloorType.SUSPENDED_FLOOR]

    # Fields used specifically in suspended floor calculations
    # Using the actual Pydantic field names from the original schema
    area_per_perimeter_vent: Annotated[
        Optional[float],
        Field(description="Area of ventilation openings per perimeter (unit: m²/m)"),
    ] = None
    thermal_resist_insul: Annotated[
        Optional[float],
        Field(
            description="Thermal resistance of insulation on base of underfloor space (unit: m².K/W)"
        ),
    ] = None
    # thermal_transm_walls and height_upper_surface are used in suspended floor calculations
    thermal_transm_walls: Annotated[
        Optional[float],
        Field(description="Thermal transmittance of walls above ground (unit: W/m².K)"),
    ] = None

    # height_upper_surface is inherited from base class (moved from here)

    # shield_fact_location is used in wind_shield_fact() - inherited from base

    # Edge insulation not typically used for suspended floors
    edge_insulation: Optional[list[EdgeInsulation]] = None


class BuildingElementGroundHeatedBasement(BuildingElementGroundBase):
    """Heated basement - uses init_heated_basement()"""

    floor_type: Literal[FloorType.HEATED_BASEMENT]

    # Required fields actually used in init_heated_basement()
    # Only z_b (depth_basement_floor) and r_w_b (thermal_resist_walls_base) are used!
    depth_basement_floor: Annotated[
        float, Field(description="Depth of basement floor below ground level (unit: m)")
    ]
    thermal_resist_walls_base: Annotated[
        float,
        Field(description="Thermal resistance of walls of the basement (unit: m².K/W)"),
    ]

    # These fields are passed to constructor but NOT used in init_heated_basement()
    # Making them optional for heated basements
    height_basement_walls: Annotated[
        Optional[float],
        Field(description="Height of the basement walls above ground level (unit: m)"),
    ] = None
    thermal_transm_envi_base: Annotated[
        Optional[float],
        Field(description="Thermal transmittance of floor above basement (unit: W/m².K)"),
    ] = None
    thermal_transm_walls: Annotated[
        Optional[float],
        Field(description="Thermal transmittance of walls above ground (unit: W/m².K)"),
    ] = None

    # Optional - edge insulation can be used with basements
    edge_insulation: Optional[list[EdgeInsulation]] = None


class BuildingElementGroundUnheatedBasement(BuildingElementGroundBase):
    """Unheated basement - uses init_unheated_basement()"""

    floor_type: Literal[FloorType.UNHEATED_BASEMENT]

    # Required fields actually used in init_unheated_basement()
    # All basement parameters are used in unheated basement calculations
    depth_basement_floor: Annotated[
        float, Field(description="Depth of basement floor below ground level (unit: m)")
    ]
    height_basement_walls: Annotated[
        float,
        Field(description="Height of the basement walls above ground level (unit: m)"),
    ]
    thermal_resist_walls_base: Annotated[
        float,
        Field(description="Thermal resistance of walls of the basement (unit: m².K/W)"),
    ]
    thermal_transm_envi_base: Annotated[
        float,
        Field(description="Thermal transmittance of floor above basement (unit: W/m².K)"),
    ]
    thermal_transm_walls: Annotated[
        float,
        Field(description="Thermal transmittance of walls above ground (unit: W/m².K)"),
    ]

    # Optional - edge insulation can be used with basements
    edge_insulation: Optional[list[EdgeInsulation]] = None


# Discriminated union based on floor_type
BuildingElementGround = Annotated[
    Union[
        BuildingElementGroundSlabNoEdgeInsulation,
        BuildingElementGroundSlabEdgeInsulation,
        BuildingElementGroundSuspendedFloor,
        BuildingElementGroundHeatedBasement,
        BuildingElementGroundUnheatedBasement,
    ],
    Field(discriminator="floor_type"),
]


class BuildingElementAdjacentConditionedSpace(StrictBaseModel):
    type: Literal["BuildingElementAdjacentConditionedSpace"]
    area: float
    areal_heat_capacity: Annotated[float, Field(description="Areal heat capacity (unit: J/m².K)")]
    mass_distribution_class: MassDistributionClass
    pitch: Annotated[
        float,
        Field(
            description="Tilt angle of the surface from horizontal, between 0 and 180, where 0 means the external surface is facing up, 90 means the external surface is vertical and 180 means the external surface is facing down (unit: ˚)"
        ),
    ]
    thermal_resistance_construction: Annotated[
        Optional[float], Field(description="Thermal resistance (unit: m².K/W)")
    ] = None
    u_value: Optional[float] = None


class BuildingElementAdjacentUnconditionedSpace_Simple(StrictBaseModel):
    type: Literal["BuildingElementAdjacentUnconditionedSpace_Simple"]
    area: Annotated[float, Field(description="Area of this building element (unit: m²)")]
    areal_heat_capacity: Annotated[float, Field(description="Areal heat capacity (unit: J/m2.K)")]
    mass_distribution_class: MassDistributionClass
    pitch: PitchAngle
    thermal_resistance_construction: Annotated[
        Optional[float], Field(description="Thermal resistance (unit: m2.K/W)")
    ] = None
    thermal_resistance_unconditioned_space: Annotated[
        float, Field(description="Effective thermal resistance of unheated space (unit: m².K/W)")
    ]
    u_value: Optional[float] = None


class ControlCombination(StrictBaseModel):
    controls: Annotated[list[str], Field(min_length=1)]
    operation: ControlCombinationOperation


class ControlCombinations(RootModel[dict[str, ControlCombination]]):
    """
    A dictionary of control combinations where:
    - Keys are user-defined names (e.g., "main", "week", "weekday", "weekend")
    - Values conform to the ControlCombination schema
    - The "main" entry is required
    """

    @model_validator(mode="after")
    def validate_main_exists(self) -> Self:
        if "main" not in self.root:
            raise ValueError("ControlCombinations must contain a 'main' entry")
        return self

    @property
    def main(self) -> ControlCombination:
        return self.root["main"]


class ControlCombinationTime(StrictBaseModel):
    type: Literal["CombinationTimeControl"]
    combination: ControlCombinations


class EcoDesignController(StrictBaseModel):
    ecodesign_control_class: EcoDesignControllerClass
    max_outdoor_temp: Optional[float] = None
    min_flow_temp: Optional[float] = None
    min_outdoor_temp: Optional[float] = None


class EnergyDiverter(StrictBaseModel):
    controlmax: Annotated[str, Field(alias="Controlmax")]
    heat_source: Annotated[str, Field(alias="HeatSource")]


class EnergySupply(StrictBaseModel):
    electric_battery: Annotated[Optional[ElectricBattery], Field(alias="ElectricBattery")] = None
    diverter: Optional[EnergyDiverter] = None
    factor: Optional[CustomEnergySourceFactor] = None
    fuel: FuelType
    is_export_capable: Annotated[
        bool,
        Field(description="Denotes that this energy supply can export its surplus supply"),
    ]
    priority: Optional[list[EnergySupplyPriorityEntry]] = None
    tariff: Optional[str] = None
    threshold_charges: Optional[Annotated[list[float], Field(max_length=12, min_length=12)]] = None
    threshold_prices: Optional[Annotated[list[float], Field(max_length=12, min_length=12)]] = None


class ExternalSensor(StrictBaseModel):
    correlation: list[ExternalSensorCorrelation]


class HeatPumpTestDatum(StrictBaseModel):
    air_flow_rate: Optional[float] = None
    capacity: float
    cop: float
    degradation_coeff: float
    design_flow_temp: float
    eahp_mixed_ext_air_ratio: Optional[float] = None
    temp_outlet: float
    temp_source: float
    temp_test: float
    test_letter: TestLetter


class ImmersionHeater(StrictBaseModel):
    type: Literal["ImmersionHeater"]
    controlmax: Annotated[
        str,
        Field(
            alias="Controlmax",
            description="Reference to a control schedule of maximum temperature setpoints",
        ),
    ]
    controlmin: Annotated[
        str,
        Field(
            alias="Controlmin",
            description="Reference to a control schedule of minimum temperature setpoints",
        ),
    ]
    energy_supply: Annotated[str, Field(alias="EnergySupply")]
    heater_position: float
    power: float
    thermostat_position: Optional[float] = None


class SolarThermalSystem(StrictBaseModel):
    type: Literal["SolarThermalSystem"]
    controlmax: Annotated[
        str,
        Field(
            alias="Controlmax",
            description="Reference to a control schedule of maximum temperature setpoints",
        ),
    ]
    energy_supply: Annotated[str, Field(alias="EnergySupply")]
    area_module: float
    collector_mass_flow_rate: float
    first_order_hlc: float
    heater_position: float
    incidence_angle_modifier: float
    modules: Annotated[int, Field(ge=1)]
    orientation360: Orientation360
    peak_collector_efficiency: float
    power_pump: float
    power_pump_control: float
    second_order_hlc: float
    sol_loc: SolarCollectorLoopLocation
    solar_loop_piping_hlc: float
    thermostat_position: Annotated[
        Optional[float], Field(description="Required for StorageTank but not for SmartHotWaterTank")
    ] = None
    tilt: float


class HeatSourceWetServiceWaterRegular(StrictBaseModel):
    type: Literal["HeatSourceWet"]
    controlmax: Annotated[
        str,
        Field(
            alias="Controlmax",
            description="Reference to a control schedule of maximum temperature setpoints",
        ),
    ]
    controlmin: Annotated[
        str,
        Field(
            alias="Controlmin",
            description="Reference to a control schedule of minimum temperature setpoints",
        ),
    ]
    energy_supply: Annotated[str, Field(alias="EnergySupply")]
    heater_position: float
    name: str
    temp_flow_limit_upper: Optional[float] = None
    thermostat_position: Annotated[
        Optional[float], Field(description="Required for StorageTank but not for SmartHotWaterTank")
    ] = None


class HeatPumpHotWaterOnly(StrictBaseModel):
    type: Literal["HeatPump_HWOnly"]
    controlmax: Annotated[
        str,
        Field(
            alias="Controlmax",
            description="Reference to a control schedule of maximum temperature setpoints",
        ),
    ]
    controlmin: Annotated[
        str,
        Field(
            alias="Controlmin",
            description="Reference to a control schedule of minimum temperature setpoints",
        ),
    ]
    energy_supply: Annotated[str, Field(alias="EnergySupply")]
    daily_losses_declared: float
    heat_exchanger_surface_area_declared: float
    heater_position: float
    in_use_factor_mismatch: float
    power_max: float
    tank_volume_declared: float
    test_data: HeatPumpHotWaterTestData
    thermostat_position: Annotated[
        Optional[float], Field(description="Required for StorageTank but not for SmartHotWaterTank")
    ] = None
    vol_hw_daily_average: float


HotWaterHeatSource = Annotated[
    Union[
        ImmersionHeater, SolarThermalSystem, HeatSourceWetServiceWaterRegular, HeatPumpHotWaterOnly
    ],
    Field(discriminator="type"),
]


class HotWaterDemand(StrictBaseModel):
    bath: Annotated[Optional[Optional[dict[str, Bath]]], Field(alias="Bath")] = None
    distribution: Annotated[Optional[list[WaterPipeworkSimple]], Field(alias="Distribution")] = None
    other: Annotated[Optional[dict[str, OtherWaterUse]], Field(alias="Other")] = None
    shower: Annotated[Optional[dict[str, Shower]], Field(alias="Shower")] = None


class HotWaterSourceSmartHotWaterTank(StrictBaseModel):
    type: Literal["SmartHotWaterTank"]
    cold_water_source: Annotated[str, Field(alias="ColdWaterSource")]
    energy_supply_pump: Annotated[str, Field(alias="EnergySupply_pump")]
    heat_source: Annotated[dict[str, HotWaterHeatSource], Field(alias="HeatSource")]
    daily_losses: float
    init_temp: float
    max_flow_rate_pump_l_per_min: float
    power_pump_k_w: Annotated[float, Field(alias="power_pump_kW")]
    primary_pipework: Optional[list[WaterPipework]] = None
    temp_setpnt_max: Annotated[
        str, Field(description="Reference to a control schedule of maximum state of charge values")
    ]
    temp_usable: float
    volume: float


class MechanicalVentilation(StrictBaseModel):
    control: Annotated[Optional[str], Field(alias="Control")] = None
    energy_supply: Annotated[str, Field(alias="EnergySupply")]
    sfp: Annotated[
        float,
        Field(
            alias="SFP",
            description="Specific fan power, inclusive of any in use factors (unit: W/l/s)",
        ),
    ]
    design_outdoor_air_flow_rate: Annotated[float, Field(description="(unit: m³/hour)")]
    ductwork: Optional[list[MechanicalVentilationDuctwork]] = None
    mvhr_eff: Annotated[Optional[float], Field(description="MVHR efficiency")] = None
    mvhr_location: Optional[MVHRLocation] = None
    sup_air_flw_ctrl: SupplyAirFlowRateControlType
    sup_air_temp_ctrl: SupplyAirTemperatureControlType
    vent_type: MechVentType

    @model_validator(mode="after")
    def validate_supply_air_temp_ctrl(self) -> Self:
        """Validate that only implemented supply air temperature control types are used."""
        if self.sup_air_temp_ctrl != SupplyAirTemperatureControlType.NO_CTRL:
            raise ValueError(
                f"Supply air temperature control type '{self.sup_air_temp_ctrl}' is not currently "
                f"implemented. Only '{SupplyAirTemperatureControlType.NO_CTRL}' is supported. "
                f"Other values would be silently overwritten by the ventilation engine."
            )
        return self


class PhotovoltaicSystem(StrictBaseModel):
    type: Literal["PhotovoltaicSystem"]
    energy_supply: Annotated[str, Field(alias="EnergySupply")]
    base_height: Annotated[
        float,
        Field(
            description="The distance between the ground and the lowest edge of the PV array (unit: m)"
        ),
    ]
    height: Annotated[float, Field(description="Height of the PV array (unit: m)")]
    inverter_is_inside: Annotated[
        bool, Field(description="Whether the inverter is considered inside the building")
    ]
    inverter_peak_power_ac: float
    inverter_peak_power_dc: float
    inverter_type: InverterType
    orientation360: Orientation360
    peak_power: Annotated[
        float,
        Field(
            description="Peak power; represents the electrical power of a photovoltaic system with a given area for a solar irradiance of 1 kW/m² on this surface (at 25 degrees) (unit: kW)"
        ),
    ]
    pitch: PitchAnglePV
    shading: list[WindowShading]
    ventilation_strategy: PhotovoltaicVentilationStrategy
    width: Annotated[float, Field(description="Width of the PV panel (unit: m)")]


OnSiteGeneration = Annotated[
    Union[PhotovoltaicSystem],
    # Ready for expanding with further generation types.
    Field(discriminator="type"),
]


class ScheduleEntryForBoolean(RootModel[Optional[Union[bool, ScheduleRepeaterForBoolean, str]]]):
    root: Optional[Union[bool, ScheduleRepeaterForBoolean, str]]


class ScheduleEntryForDouble(RootModel[Optional[Union[float, ScheduleRepeaterForDouble, str]]]):
    root: Optional[Union[float, ScheduleRepeaterForDouble, str]]


class ScheduleReferenceEntryForBoolean(
    RootModel[Union[list[ScheduleEntryForBoolean], ScheduleEntryForBoolean]]
):
    root: Union[list[ScheduleEntryForBoolean], ScheduleEntryForBoolean]


class ScheduleReferenceEntryForDouble(
    RootModel[Union[list[ScheduleEntryForDouble], ScheduleEntryForDouble]]
):
    root: Union[list[ScheduleEntryForDouble], ScheduleEntryForDouble]


# Updated ScheduleForBoolean to support user-defined entries
class ScheduleForBoolean(RootModel[dict[str, list[ScheduleEntryForBoolean]]]):
    """
    A dictionary of schedule entries where:
    - Keys are user-defined names (e.g., "main", "week", "weekday", "weekend")
    - Values are lists of ScheduleEntryForBoolean
    - The "main" entry is required
    """

    @model_validator(mode="after")
    def validate_main_exists(self) -> Self:
        if "main" not in self.root:
            raise ValueError("Schedule must contain a 'main' entry")
        return self

    # Convenience properties for backward compatibility
    @property
    def main(self) -> list[ScheduleEntryForBoolean]:
        return self.root["main"]


# Updated ScheduleForDouble to support user-defined entries
class ScheduleForDouble(RootModel[dict[str, list[ScheduleEntryForDouble]]]):
    """
    A dictionary of schedule entries where:
    - Keys are user-defined names (e.g., "main", "week", "weekday", "weekend")
    - Values are lists of ScheduleEntryForDouble
    - The "main" entry is required
    """

    @model_validator(mode="after")
    def validate_main_exists(self) -> Self:
        if "main" not in self.root:
            raise ValueError("Schedule must contain a 'main' entry")
        return self

    # Convenience properties for backward compatibility
    @property
    def main(self) -> list[ScheduleEntryForDouble]:
        return self.root["main"]


class ShadingObject(StrictBaseModel):
    distance: float
    height: float
    type: ShadingObjectType


class ShadingSegment(StrictBaseModel):
    end360: float
    shading: Optional[list[ShadingObject]] = None
    start360: float


class SpaceCoolSystemAirConditioning(StrictBaseModel):
    type: Literal["AirConditioning"]  # Changed from SpaceCoolSystemType to Literal
    control: Annotated[str, Field(alias="Control")]
    energy_supply: Annotated[str, Field(alias="EnergySupply")]
    cooling_capacity: Annotated[
        float, Field(description="Maximum cooling capacity of the system (unit: kW)")
    ]
    efficiency: float
    frac_convective: Annotated[float, Field(description="Convective fraction for cooling")]


SpaceCoolSystem = Annotated[
    Union[SpaceCoolSystemAirConditioning],
    Field(discriminator="type"),
]


class SpaceHeatSystemInstantElectricHeater(StrictBaseModel):
    type: Literal["InstantElecHeater"]
    energy_supply: Annotated[str, Field(alias="EnergySupply")]
    control: Annotated[str, Field(alias="Control")]
    frac_convective: Annotated[float, Field(description="Convective fraction for heating")]
    rated_power: Annotated[float, Field(description="(unit: kW)")]


class SpaceHeatSystemElectricStorageHeater(StrictBaseModel):
    type: Literal["ElecStorageHeater"]
    control_charger: Annotated[str, Field(alias="ControlCharger")]
    esh_max_output: Annotated[
        list[Annotated[list[float], Field(max_length=2, min_length=2)]],
        Field(alias="ESH_max_output"),
    ]
    esh_min_output: Annotated[
        list[Annotated[list[float], Field(max_length=2, min_length=2)]],
        Field(alias="ESH_min_output"),
    ]
    energy_supply: Annotated[str, Field(alias="EnergySupply")]
    air_flow_type: AirFlowType
    control: Annotated[str, Field(alias="Control")]
    fan_pwr: Annotated[float, Field(description="Fan power (unit: W)")]
    frac_convective: Annotated[float, Field(description="Convective fraction for heating")]
    n_units: Annotated[int, Field(ge=0)]
    pwr_in: float
    rated_power_instant: Annotated[float, Field(description="(instant backup) (unit: kW)")]
    storage_capacity: float
    zone: Annotated[
        str, Field(alias="Zone", description="The zone where the unit(s) is/are installed")
    ]
    temp_setback: Optional[float] = None
    advanced_start: Optional[float] = None


class SpaceHeatSystemWetDistribution(StrictBaseModel):
    type: Literal["WetDistribution"]
    heat_source: Annotated[SpaceHeatSystemHeatSource, Field(alias="HeatSource")]
    bypass_percentage_recirculated: Optional[float] = None
    design_flow_rate: Optional[float] = None
    design_flow_temp: int
    emitters: Annotated[list[WetEmitter], Field(min_length=1)]
    ecodesign_controller: EcoDesignController
    max_flow_rate: Optional[float] = None
    min_flow_rate: Optional[float] = None
    temp_diff_emit_dsgn: float
    thermal_mass: Optional[float] = None

    variable_flow: bool
    control: Annotated[str, Field(alias="Control")]
    energy_supply: Annotated[Optional[str], Field(alias="EnergySupply")] = None
    zone: Annotated[str, Field(alias="Zone")]


class SpaceHeatSystemWarmAir(StrictBaseModel):
    type: Literal["WarmAir"]
    heat_source: Annotated[SpaceHeatSystemHeatSource, Field(alias="HeatSource")]
    control: Annotated[str, Field(alias="Control")]
    frac_convective: float


SpaceHeatSystem = Annotated[
    Union[
        SpaceHeatSystemInstantElectricHeater,
        SpaceHeatSystemElectricStorageHeater,
        SpaceHeatSystemWetDistribution,
        SpaceHeatSystemWarmAir,
    ],
    Field(discriminator="type"),
]


class WasteWaterHeatRecoverySystem(StrictBaseModel):
    cold_water_source: Annotated[str, Field(alias="ColdWaterSource")]
    efficiencies: list[float]
    flow_rates: list[float]
    type: WasteWaterHeatRecoverySystemType
    utilisation_factor: float


class WindowTreatment(StrictBaseModel):
    control_closing_irrad: Annotated[Optional[str], Field(alias="Control_closing_irrad")] = None
    control_open: Annotated[Optional[str], Field(alias="Control_open")] = None
    control_opening_irrad: Annotated[Optional[str], Field(alias="Control_opening_irrad")] = None
    controls: WindowTreatmentControl
    delta_r: float
    is_open: Annotated[
        Optional[bool],
        Field(
            description="This field should be a boolean - any string provided will be ignored and treated as a null."
        ),
    ] = None
    opening_delay_hrs: Optional[float] = None
    trans_red: float
    type: WindowTreatmentType


class ApplianceGains(StrictBaseModel):
    events: Annotated[
        Optional[list[ApplianceGainsEvent]],
        Field(alias="Events", description="List of appliance usage events"),
    ] = None
    standby: Annotated[
        Optional[float],
        Field(alias="Standby", description="Appliance power consumption when not in use (unit: W)"),
    ] = None
    energy_supply: Annotated[str, Field(alias="EnergySupply")]
    gains_fraction: Annotated[
        float, Field(description="Proportion of appliance demand turned into heat gains (no unit)")
    ]
    loadshifting: Optional[ApplianceLoadShifting] = None
    priority: Optional[int] = None
    schedule: Optional[ScheduleForDouble] = None
    start_day: Annotated[
        int,
        Field(description="First day of the time series, day of the year, 0 to 365", ge=0, le=365),
    ]
    time_series_step: Annotated[
        float, Field(description="Timestep of the time series data (unit: hours)")
    ]


class BoilerCostScheduleHybrid(StrictBaseModel):
    cost_schedule_boiler: ScheduleForDouble
    cost_schedule_hp: ScheduleForDouble
    cost_schedule_start_day: Annotated[int, Field(ge=0, le=365)]
    cost_schedule_time_series_step: float


class BuildingElementTransparent(StrictBaseModel):
    type: Literal["BuildingElementTransparent"]
    control_window_openable: Annotated[Optional[str], Field(alias="Control_WindowOpenable")] = None
    base_height: Annotated[
        float,
        Field(
            description="The distance between the ground and the lowest edge of the element (unit: m)"
        ),
    ]
    frame_area_fraction: Annotated[
        float,
        Field(
            description="The frame area fraction of window, ratio of the projected frame area to the overall projected area of the glazed element of the window"
        ),
    ]
    free_area_height: float
    g_value: Annotated[
        float,
        Field(description="Total solar energy transmittance of the transparent part of the window"),
    ]
    height: Annotated[float, Field(description="The height of the building element (unit: m)")]
    max_window_open_area: float
    mid_height: float
    orientation360: Orientation360
    pitch: PitchAngle
    shading: list[WindowShading]
    thermal_resistance_construction: Annotated[
        Optional[float], Field(description="Thermal resistance (unit: m².K/W)")
    ] = None
    treatment: Optional[list[WindowTreatment]] = None
    u_value: Optional[float] = None
    width: Annotated[float, Field(description="The width of the building element (unit: m)")]
    window_part_list: list[WindowPart]


BuildingElement = Annotated[
    Union[
        BuildingElementOpaque,
        BuildingElementTransparent,
        BuildingElementGround,
        BuildingElementAdjacentConditionedSpace,
        BuildingElementAdjacentUnconditionedSpace_Simple,
    ],
    Field(discriminator="type"),
]


class ChargeLevel(RootModel[Union[float, list[float], ScheduleForDouble]]):
    root: Union[float, list[float], ScheduleForDouble]


class ControlOnOffTimer(StrictBaseModel):
    type: Literal["OnOffTimeControl"]
    allow_null: Optional[bool] = None
    schedule: Annotated[
        ScheduleForBoolean,
        Field(description="List of boolean values where true means on, one entry per hour"),
    ]
    start_day: Annotated[
        int,
        Field(description="First day of the time series, day of the year, 0 to 365", ge=0, le=365),
    ]
    time_series_step: Annotated[
        float, Field(description="Timestep of the time series data (unit: hours)")
    ]


class ControlOnOffCostMinimising(StrictBaseModel):
    type: Literal["OnOffCostMinimisingTimeControl"]
    schedule: Annotated[
        ScheduleForDouble, Field(description="List of cost values (one entry per time_series_step)")
    ]
    start_day: Annotated[
        int,
        Field(description="First day of the time series, day of the year, 0 to 365", ge=0, le=365),
    ]
    time_on_daily: Annotated[float, Field(description="Number of 'on' hours to be set per day")]
    time_series_step: Annotated[
        float, Field(description="Timestep of the time series data (unit: hours)")
    ]


class ControlSetpointTimer(StrictBaseModel):
    type: Literal["SetpointTimeControl"]
    advanced_start: Annotated[
        Optional[float],
        Field(
            description="How long before heating period the system should switch on (unit: hours)"
        ),
    ] = None
    default_to_max: Annotated[
        Optional[bool],
        Field(
            description="If both min and max limits are set but setpoint is not, whether to default to min (false) or max (true)"
        ),
    ] = None
    schedule: Annotated[
        ScheduleForDouble,
        Field(description="list of float values (one entry per hour)"),
    ]
    setpoint_max: Annotated[Optional[float], Field(description="Maximum setpoint allowed")] = None
    setpoint_min: Annotated[Optional[float], Field(description="Minimum setpoint allowed")] = None
    start_day: Annotated[
        int,
        Field(description="First day of the time series, day of the year, 0 to 365", ge=0, le=365),
    ]
    time_series_step: Annotated[
        float, Field(description="Timestep of the time series data (unit: hours)")
    ]


class ControlChargeTarget(StrictBaseModel):
    type: Literal["ChargeControl"]
    charge_level: Annotated[
        Optional[ChargeLevel], Field(description="Proportion of the charge targeted for each day")
    ] = None
    external_sensor: Optional[ExternalSensor] = None
    logic_type: Optional[ControlLogicType] = None
    schedule: Annotated[
        ScheduleForBoolean,
        Field(description="List of boolean values where true means 'on' (one entry per hour)"),
    ]
    start_day: Annotated[
        int,
        Field(description="First day of the time series, day of the year, 0 to 365", ge=0, le=365),
    ]
    temp_charge_cut: Optional[float] = None
    temp_charge_cut_delta: Optional[ScheduleForDouble] = None
    time_series_step: Annotated[
        float, Field(description="Timestep of the time series data (unit: hours)")
    ]


Control = Annotated[
    Union[
        ControlOnOffTimer,
        ControlOnOffCostMinimising,
        ControlSetpointTimer,
        ControlChargeTarget,
        ControlCombinationTime,
    ],
    Field(discriminator="type"),
]


class ExternalConditionsInput(StrictBaseModel):
    air_temperatures: Annotated[
        Optional[list[float]],
        Field(description="List of external air temperatures, one entry per hour (unit: ˚C)"),
    ] = None
    diffuse_horizontal_radiation: Annotated[
        Optional[list[float]],
        Field(
            description="List of diffuse horizontal radiation values, one entry per hour (unit: W/m²)"
        ),
    ] = None
    direct_beam_conversion_needed: Annotated[
        Optional[bool],
        Field(
            description="A flag to indicate whether direct beam radiation from climate data needs to be converted from horizontal to normal incidence; if normal direct beam radiation values are provided then no conversion is needed"
        ),
    ] = None
    direct_beam_radiation: Annotated[
        Optional[list[float]],
        Field(description="List of direct beam radiation values, one entry per hour (unit: W/m²)"),
    ] = None
    latitude: Annotated[
        Optional[float],
        Field(description="Latitude of weather station, angle from south (unit: ˚)"),
    ] = None
    longitude: Annotated[
        Optional[float],
        Field(description="Longitude of weather station, easterly +ve westerly -ve (unit: ˚)"),
    ] = None
    shading_segments: Annotated[
        Optional[list[ShadingSegment]],
        Field(
            description="Data splitting the ground plane into segments (8-36) and giving height and distance to shading objects surrounding the building"
        ),
    ] = None
    solar_reflectivity_of_ground: Annotated[
        Optional[list[float]],
        Field(description="List of ground reflectivity values, 0 to 1, one entry per hour"),
    ] = None
    wind_directions: Annotated[
        Optional[list[float]],
        Field(
            description="List of wind directions in degrees where North=0, East=90, South=180, West=270. Values range: 0 to 360. Wind direction is reported by the direction from which it originates, e.g. a southerly (180 degree) wind blows from the south to the north. (unit: ˚)"
        ),
    ] = None
    wind_speeds: Annotated[
        Optional[list[float]],
        Field(description="List of wind speeds, one entry per hour (unit: m/s)"),
    ] = None


class HeatPumpBoiler(BoilerBase):
    """Boiler used as backup for heat pump systems"""

    cost_schedule_hybrid: Optional[BoilerCostScheduleHybrid] = None


class HeatSourceWetHeatPump(StrictBaseModel):
    type: Literal["HeatPump"]
    buffer_tank: Annotated[Optional[HeatPumpBufferTank], Field(alias="BufferTank")] = None
    energy_supply: Annotated[str, Field(alias="EnergySupply")]
    energy_supply_heat_network: Annotated[
        Optional[str], Field(alias="EnergySupply_heat_network")
    ] = None
    mechanical_ventilation: Annotated[Optional[str], Field(alias="MechanicalVentilation")] = None
    backup_ctrl_type: HeatPumpBackupControlType
    boiler: Optional[HeatPumpBoiler] = None
    eahp_mixed_max_temp: Optional[float] = None
    eahp_mixed_min_temp: Optional[float] = None
    min_modulation_rate_20: Optional[float] = None
    min_modulation_rate_35: Optional[float] = None
    min_modulation_rate_55: Optional[float] = None
    min_temp_diff_flow_return_for_hp_to_operate: float
    modulating_control: bool
    power_crankcase_heater: float
    power_heating_circ_pump: Optional[float] = None
    power_heating_warm_air_fan: Optional[float] = None
    power_max_backup: Optional[float] = None
    power_off: float
    power_source_circ_pump: float
    power_standby: float
    sink_type: HeatPumpSinkType
    source_type: HeatPumpSourceType
    temp_distribution_heat_network: Optional[float] = None
    temp_lower_operating_limit: float
    temp_return_feed_max: Optional[float] = None
    test_data_en14825: Annotated[list[HeatPumpTestDatum], Field(alias="test_data_EN14825")]
    time_constant_onoff_operation: float
    time_delay_backup: Optional[float] = None
    var_flow_temp_ctrl_during_test: bool


HeatSourceWet = Annotated[
    Union[
        HeatSourceWetHeatPump,
        HeatSourceWetBoiler,
        HeatSourceWetHeatBattery,
        HeatSourceWetHIU,
    ],
    Field(discriminator="type"),
]


class InfiltrationVentilation(StrictBaseModel):
    control_vent_adjust_max: Annotated[Optional[str], Field(alias="Control_VentAdjustMax")] = None
    control_vent_adjust_min: Annotated[Optional[str], Field(alias="Control_VentAdjustMin")] = None
    control_window_adjust: Annotated[Optional[str], Field(alias="Control_WindowAdjust")] = None
    leaks: Annotated[VentilationLeaks, Field(alias="Leaks")]
    mechanical_ventilation: Annotated[
        Optional[dict[str, MechanicalVentilation]], Field(alias="MechanicalVentilation")
    ] = None
    vents: Annotated[dict[str, Vent], Field(alias="Vents")]
    ach_max_static_calcs: Optional[float] = None
    ach_min_static_calcs: Optional[float] = None
    altitude: float
    cross_vent_possible: bool
    shield_class: VentilationShieldClass
    terrain_class: TerrainClass
    ventilation_zone_base_height: Annotated[
        float, Field(description="Base height of the ventilation zone relative to ground (m)")
    ]
    vent_opening_ratio_init: Optional[float] = None


class InternalGainsDetails(StrictBaseModel):
    schedule: ScheduleForDouble
    start_day: Annotated[int, Field(ge=0, le=365)]
    time_series_step: float


class StorageTank(StrictBaseModel):
    type: Literal["StorageTank"]
    cold_water_source: Annotated[str, Field(alias="ColdWaterSource")]
    heat_source: Annotated[dict[str, HotWaterHeatSource], Field(alias="HeatSource")]
    daily_losses: Annotated[
        float,
        Field(
            description="Measured standby losses due to cylinder insulation at standardised conditions (unit: kWh/24h)"
        ),
    ]
    heat_exchanger_surface_area: Optional[float] = None
    init_temp: float
    primary_pipework: Optional[list[WaterPipework]] = None
    volume: Annotated[float, Field(description="Total volume of tank (unit: litre)")]


class Zone(StrictBaseModel):
    building_element: Annotated[dict[str, BuildingElement], Field(alias="BuildingElement")]
    space_cool_system: Annotated[
        Optional[Union[str, set[str]]],
        Field(alias="SpaceCoolSystem"),
    ] = None
    space_heat_system: Annotated[
        Optional[Union[str, set[str]]],
        Field(alias="SpaceHeatSystem"),
    ] = None
    thermal_bridging: Annotated[
        Union[float, dict[str, ThermalBridging]],
        Field(alias="ThermalBridging"),
    ]
    area: Annotated[float, Field(description="Useful floor area of the zone (unit: m²)")]
    temp_setpnt_basis: Optional[ZoneTemperatureControlBasis] = None
    temp_setpnt_init: Annotated[
        float,
        Field(description="Setpoint temperature to use during initialisation (unit: ˚C)"),
    ]
    volume: float


HotWaterSourceDetails = Annotated[
    Union[
        StorageTank,
        HotWaterSourceCombiBoiler,
        HotWaterSourceHUI,
        HotWaterSourcePointOfUse,
        HotWaterSourceSmartHotWaterTank,
        HotWaterSourceHeatBattery,
    ],
    Field(discriminator="type"),
]


class InternalGains(RootModel[dict[str, InternalGainsDetails]]):
    """
    A dictionary of internal gains entries where:
    - Keys are user-defined names (e.g., "ColdWaterLosses", "EvaporativeLosses", "metabolic gains", etc.)
    - Values conform to the InternalGainsDetails schema
    - No specific entries are required - all entries are optional and user-defined
    """

    root: dict[str, InternalGainsDetails]

    # Optional convenience properties for backward compatibility with common field names
    @property
    def cold_water_losses(self) -> Optional[InternalGainsDetails]:
        return self.root.get("ColdWaterLosses")

    @property
    def evaporative_losses(self) -> Optional[InternalGainsDetails]:
        return self.root.get("EvaporativeLosses")

    @property
    def metabolic_gains(self) -> Optional[InternalGainsDetails]:
        return self.root.get("metabolic gains")

    @property
    def other(self) -> Optional[InternalGainsDetails]:
        return self.root.get("other")

    @property
    def total_internal_gains_1(self) -> Optional[InternalGainsDetails]:
        return self.root.get("total internal gains") or self.root.get("total_internal_gains")


class HotWaterSource(StrictBaseModel):
    hw_cylinder: Annotated[HotWaterSourceDetails, Field(alias="hw cylinder")]


class Input(StrictBaseModel):
    appliance_gains: Annotated[
        Optional[dict[str, ApplianceGains]], Field(alias="ApplianceGains")
    ] = None
    cold_water_source: Annotated[dict[str, ColdWaterSource], Field(alias="ColdWaterSource")]
    control: Annotated[Optional[dict[str, Control]], Field(alias="Control")]
    energy_supply: Annotated[dict[str, EnergySupply], Field(alias="EnergySupply")]
    events: Annotated[WaterHeatingEvents, Field(alias="Events")]
    external_conditions: Annotated[ExternalConditionsInput, Field(alias="ExternalConditions")]
    heat_source_wet: Annotated[
        Optional[dict[str, HeatSourceWet]],
        Field(alias="HeatSourceWet"),
    ] = None
    hot_water_demand: Annotated[HotWaterDemand, Field(alias="HotWaterDemand")]
    hot_water_source: Annotated[HotWaterSource, Field(alias="HotWaterSource")]
    infiltration_ventilation: Annotated[
        InfiltrationVentilation, Field(alias="InfiltrationVentilation")
    ]
    internal_gains: Annotated[InternalGains, Field(alias="InternalGains")]

    on_site_generation: Annotated[
        Optional[dict[str, OnSiteGeneration]], Field(alias="OnSiteGeneration")
    ] = None
    pre_heated_water_source: Annotated[
        Optional[dict[str, StorageTank]], Field(alias="PreHeatedWaterSource")
    ] = None
    simulation_time: Annotated[SimulationTime, Field(alias="SimulationTime")]
    smart_appliance_controls: Annotated[
        Optional[dict[str, SmartApplianceControl]], Field(alias="SmartApplianceControls")
    ] = None
    space_cool_system: Annotated[
        Optional[dict[str, SpaceCoolSystem]], Field(alias="SpaceCoolSystem")
    ] = None
    space_heat_system: Annotated[
        Optional[dict[str, SpaceHeatSystem]], Field(alias="SpaceHeatSystem")
    ] = None
    waste_water_heat_recovery_systems: Annotated[
        Optional[dict[str, WasteWaterHeatRecoverySystem]], Field(alias="WWHRS")
    ] = None
    zone: Annotated[dict[str, Zone], Field(alias="Zone")]
    temp_internal_air_static_calcs: float

    @model_validator(mode="after")
    def validate_shower_waste_water_heat_recovery_systems(self) -> Self:
        # Validate that showers point to a valid WWHRS key.
        if self.hot_water_demand.shower:
            for shower_name, shower in self.hot_water_demand.shower.items():
                if (
                    isinstance(shower, ShowerMixer)
                    and shower.waste_water_heat_recovery_system is not None
                    and shower.waste_water_heat_recovery_system
                    not in (self.waste_water_heat_recovery_systems or {})
                ):
                    raise ValueError(
                        f"WWHRS value '{shower.waste_water_heat_recovery_system}' not found in Input.WWHRS (from Input.HotWaterDemand.Shower['{shower_name}'].WWHRS)"
                    )
        return self  # Valid
