from abc import ABC
from typing import Annotated, Optional, Literal, Union

from pydantic import Field, BaseModel, ConfigDict

from core.input import (
    Input,
    ColdWaterSource,
    InfiltrationVentilation,
    Zone,
    MechanicalVentilation,
    ApplianceGains,
    BuildingElementOpaque,
    BuildingElementTransparent,
    BuildingElementGround,
    BuildingElementAdjacentConditionedSpace,
    BuildingElementAdjacentUnconditionedSpace_Simple,
    SpaceCoolSystem,
    SpaceHeatSystemInstantElectricHeater,
    SpaceHeatSystemElectricStorageHeater,
    SpaceHeatSystemWetDistribution,
    SpaceHeatSystemWarmAir,
    ThermalBridgingLinear,
    ThermalBridgingPoint,
    ExternalConditionsInput,
    ShadingObject,
    ImmersionHeater,
    SolarThermalSystem,
    HeatSourceWetServiceWaterRegular,
    HeatPumpHotWaterOnly,
    HotWaterSourceSmartHotWaterTank,
    StorageTank,
    HotWaterSourceCombiBoiler,
    HotWaterSourceHUI,
    HotWaterSourcePointOfUse,
    HotWaterSourceHeatBattery,
)

# Import enums from the shared enums module
from core.enums import (
    EnergySupplyType,
    HeatingControlType,
    SpaceHeatControlType,
    CombustionAirSupplySituation,
    CombustionApplianceType,
    CombustionFuelType,
    FlueGasExhaustSituation,
    WaterHeatingSchedule,
)


class StrictBaseModel(BaseModel):
    """Base model class that forbids extra fields by default."""

    model_config = ConfigDict(extra="forbid")


class General(BaseModel):
    pass


class LoadShifting(BaseModel):
    pass


class Tariff(BaseModel):
    pass


class Appliance(BaseModel, ABC):
    loadshifting: Optional[LoadShifting] = None


class ApplianceEnergyPerCycle(Appliance, ABC):
    kWh_per_cycle: float


class ApplianceEnergyPer100Cycle(Appliance, ABC):
    kWh_per_100cycle: float


class ApplianceEnergyPerAnnum(Appliance):
    kWh_per_annum: float


class ApplianceGainsFHS(ApplianceGains):
    type: Optional[str] = None
    loadshifting: Optional[LoadShifting] = None


class BuildingElementOpaqueFHS(BuildingElementOpaque):
    """FHS-specific version of BuildingElementOpaque with additional fields"""

    is_external_door: Optional[bool] = None


class BuildingElementTransparentFHS(BuildingElementTransparent):
    """FHS-specific version of BuildingElementTransparent with additional fields"""

    security_risk: Optional[bool] = None


BuildingElementFHS = Annotated[
    Union[
        BuildingElementOpaqueFHS,  # Use FHS version here
        BuildingElementTransparentFHS,
        BuildingElementGround,
        BuildingElementAdjacentConditionedSpace,
        BuildingElementAdjacentUnconditionedSpace_Simple,
    ],
    Field(discriminator="type"),
]


class ClothesDrying(ApplianceEnergyPer100Cycle):
    kg_load: float


class ClothesWashing(ApplianceEnergyPer100Cycle):
    kg_load: float


class CombustionAppliance(BaseModel):
    appliance_type: CombustionApplianceType
    exhaust_situation: FlueGasExhaustSituation
    fuel_type: CombustionFuelType
    supply_situation: CombustionAirSupplySituation


class Dishwasher(ApplianceEnergyPer100Cycle): ...


class Fridge(ApplianceEnergyPerAnnum): ...


class FridgeFreezer(BaseModel):
    # FHS preprocessing can create different field combinations
    kWh_per_annum: Optional[float] = None
    kWh_per_cycle: Optional[float] = None
    Energysupply: Optional[EnergySupplyType] = None
    loadshifting: Optional[LoadShifting] = None


class Freezer(ApplianceEnergyPerAnnum): ...


class Hobs(ApplianceEnergyPerCycle):
    energy_supply: Annotated[EnergySupplyType, Field(alias="Energysupply")]


class ImmersionHeaterFHS(ImmersionHeater):
    """FHS-specific version of ImmersionHeater with additional fields"""

    temp_setpnt_max: Optional[str] = None


HotWaterHeatSourceFHS = Annotated[
    Union[
        ImmersionHeaterFHS,
        SolarThermalSystem,
        HeatSourceWetServiceWaterRegular,
        HeatPumpHotWaterOnly,
    ],
    Field(discriminator="type"),
]


class HotWaterSourceSmartHotWaterTankFHS(HotWaterSourceSmartHotWaterTank):
    """FHS-specific version using FHS HotWaterHeatSource"""

    heat_source: Annotated[dict[str, HotWaterHeatSourceFHS], Field(alias="HeatSource")]


HotWaterSourceDetailsFHS = Annotated[
    Union[
        StorageTank,
        HotWaterSourceCombiBoiler,
        HotWaterSourceHUI,
        HotWaterSourcePointOfUse,
        HotWaterSourceSmartHotWaterTankFHS,  # Use FHS version
        HotWaterSourceHeatBattery,
    ],
    Field(discriminator="type"),
]


class HotWaterSourceFHS(StrictBaseModel):
    hw_cylinder: Annotated[HotWaterSourceDetailsFHS, Field(alias="hw cylinder")]


class Kettle(ApplianceEnergyPerCycle): ...


class Microwave(ApplianceEnergyPerCycle): ...


class Oven(ApplianceEnergyPerCycle):
    energy_supply: Annotated[EnergySupplyType, Field(alias="Energysupply")]


T_APPLIANCE_LITERALS = Literal["Default", "Not Installed"]
APPLIANCE_NOT_INSTALLED = "Not Installed"


class Appliances(BaseModel):
    """
    The keys of this object match with the ApplianceKey enum.
    Each appliance type is determined by its key.
    "Lighting" is not included in the FHS applianced mapping.
    """

    clothes_drying: Annotated[
        Union[ClothesDrying, T_APPLIANCE_LITERALS],
        Field(alias="Clothes_drying"),
    ] = APPLIANCE_NOT_INSTALLED
    clothes_washing: Annotated[
        Union[ClothesWashing, T_APPLIANCE_LITERALS],
        Field(alias="Clothes_washing"),
    ] = APPLIANCE_NOT_INSTALLED
    dishwasher: Annotated[
        Union[Dishwasher, T_APPLIANCE_LITERALS],
        Field(alias="Dishwasher"),
    ] = APPLIANCE_NOT_INSTALLED
    fridge: Annotated[Union[Fridge, T_APPLIANCE_LITERALS], Field(alias="Fridge")] = (
        APPLIANCE_NOT_INSTALLED
    )
    fridge_freezer: Annotated[
        Union[FridgeFreezer, T_APPLIANCE_LITERALS],
        Field(alias="Fridge-Freezer"),
    ] = APPLIANCE_NOT_INSTALLED
    freezer: Annotated[Union[Freezer, T_APPLIANCE_LITERALS], Field(alias="Freezer")] = (
        APPLIANCE_NOT_INSTALLED
    )
    hobs: Annotated[Union[Hobs, T_APPLIANCE_LITERALS], Field(alias="Hobs")] = (
        APPLIANCE_NOT_INSTALLED
    )
    kettle: Annotated[Union[Kettle, T_APPLIANCE_LITERALS], Field(alias="Kettle")] = (
        APPLIANCE_NOT_INSTALLED
    )
    microwave: Annotated[
        Union[Microwave, T_APPLIANCE_LITERALS],
        Field(alias="Microwave"),
    ] = APPLIANCE_NOT_INSTALLED
    otherdevices: Annotated[
        Union[ApplianceEnergyPerAnnum, T_APPLIANCE_LITERALS],
        Field(alias="Otherdevices"),
    ] = APPLIANCE_NOT_INSTALLED
    oven: Annotated[Union[Oven, T_APPLIANCE_LITERALS], Field(alias="Oven")] = (
        APPLIANCE_NOT_INSTALLED
    )


class LightingBulbs(BaseModel):
    count: Annotated[int, Field(description="The number of bulbs present.", ge=0)]
    efficacy: Optional[float] = None
    power: Annotated[float, Field(ge=0.0)]


class Lighting(BaseModel):
    efficacy: Optional[float] = None
    bulbs: Optional[dict[str, LightingBulbs]] = None


class MechanicalVentilationFHS(MechanicalVentilation):
    # Add the FHS-specific field that's not in core
    measured_air_flow_rate: Optional[float] = None
    measured_fan_power: Optional[float] = None


class InfiltrationVentilationFHS(InfiltrationVentilation):
    noise_nuisance: Optional[bool] = None

    # Override to use FHS-specific MechanicalVentilation
    mechanical_ventilation: Annotated[
        Optional[dict[str, MechanicalVentilationFHS]], Field(alias="MechanicalVentilation")
    ] = None

    # Add CombustionAppliances as optional field (only exists in FHS wrapper)
    combustion_appliances: Annotated[
        Optional[dict[str, CombustionAppliance]],
        Field(alias="CombustionAppliances", default_factory=dict),
    ] = {}


class ShadingSegmentFHS(BaseModel):
    """FHS-specific version of ShadingSegment with additional field names"""

    # FHS preprocessing uses these field names instead of end360/start360
    end: Optional[float] = None
    start: Optional[float] = None
    number: Optional[int] = None

    # Also allow the core field names for compatibility
    end360: Optional[float] = None
    start360: Optional[float] = None
    shading: Optional[list[ShadingObject]] = None


class ExternalConditionsInputFHS(ExternalConditionsInput):
    """FHS-specific version of ExternalConditionsInput"""

    # Override to use FHS-specific ShadingSegment
    shading_segments: Annotated[
        Optional[list[ShadingSegmentFHS]],
        Field(
            description="Data splitting the ground plane into segments (8-36) and giving height and distance to shading objects surrounding the building"
        ),
    ] = None


class SpaceCoolSystemFHS(SpaceCoolSystem):
    """FHS-specific version of SpaceCoolSystem with additional fields"""

    advanced_start: Optional[float] = None
    temp_setback: Optional[float] = None


class SpaceHeatSystemInstantElectricHeaterFHS(SpaceHeatSystemInstantElectricHeater):
    """FHS-specific version of SpaceHeatSystemInstantElectricHeater with additional fields"""

    advanced_start: Optional[float] = None
    temp_setback: Optional[float] = None


class SpaceHeatSystemWarmAirFHS(SpaceHeatSystemWarmAir):
    """FHS-specific version of SpaceHeatSystemWarmAir with additional fields"""

    advanced_start: Optional[float] = None
    temp_setback: Optional[float] = None


class SpaceHeatSystemWetDistributionFHS(SpaceHeatSystemWetDistribution):
    """FHS-specific version of SpaceHeatSystemWetDistribution with additional fields"""

    advanced_start: Optional[float] = None
    temp_setback: Optional[float] = None


SpaceHeatSystemFHS = Annotated[
    Union[
        SpaceHeatSystemInstantElectricHeaterFHS,  # Use FHS version here
        SpaceHeatSystemElectricStorageHeater,
        SpaceHeatSystemWetDistributionFHS,
        SpaceHeatSystemWarmAirFHS,
    ],
    Field(discriminator="type"),
]


class ThermalBridgingLinearFHS(ThermalBridgingLinear):
    """FHS-specific version of ThermalBridgingLinear with additional fields"""

    junction_type: Optional[str] = None


ThermalBridgingFHS = Annotated[
    Union[ThermalBridgingLinearFHS, ThermalBridgingPoint],
    Field(discriminator="type"),
]


class ZoneFHS(Zone):
    building_element: Annotated[dict[str, BuildingElementFHS], Field(alias="BuildingElement")]

    thermal_bridging: Annotated[
        Union[float, dict[str, ThermalBridgingFHS]],
        Field(alias="ThermalBridging"),
    ]

    space_heat_control: Annotated[
        Optional[SpaceHeatControlType], Field(alias="SpaceHeatControl")
        # TODO Not technically required by existing code, but should be
    ] = None
    lighting: Annotated[Optional[Lighting], Field(alias="Lighting")] = None


class InputFHS(Input):
    """
    Version of the HEM inputs for the FHS wrapper.
    """

    # Modified fields from core.input.Input
    appliances: Annotated[
        Optional[Appliances],
        Field(
            alias="Appliances",
        ),
    ] = None
    appliance_gains: Annotated[
        Optional[dict[str, ApplianceGainsFHS]], Field(alias="ApplianceGains")
    ] = None
    cold_water_source: Annotated[  # type: ignore[IncompatibleVariableOverride]
        dict[str, ColdWaterSource],
        Field(alias="ColdWaterSource", description="Requires specific keys for FHS wrapper"),
    ]
    infiltration_ventilation: Annotated[  # type: ignore[IncompatibleVariableOverride]
        InfiltrationVentilationFHS, Field(alias="InfiltrationVentilation")
    ]
    zone: Annotated[dict[str, ZoneFHS], Field(alias="Zone")]  # type: ignore[IncompatibleVariableOverride]

    # New fields for the FHS wrapper only
    general: Annotated[Optional[General], Field(alias="General")] = None  # type: ignore[IncompatibleVariableOverride]
    number_of_bedrooms: Annotated[Optional[int], Field(alias="NumberOfBedrooms", ge=0)] = None
    number_of_wet_rooms: Annotated[Optional[int], Field(alias="NumberOfWetRooms", ge=0)] = None
    part_gcompliance: Annotated[Optional[bool], Field(alias="PartGcompliance")] = None
    part_o_active_cooling_required: Annotated[
        Optional[bool], Field(alias="PartO_active_cooling_required")
    ] = None
    ground_floor_area: Annotated[
        Optional[float],
        Field(
            alias="GroundFloorArea",
            description="For a house, the area of the ground floor (unit: m²)",
        ),
    ] = None
    heating_control_type: Annotated[
        Optional[HeatingControlType], Field(alias="HeatingControlType")
    ] = None
    water_heat_sched_default: Annotated[
        Optional[WaterHeatingSchedule], Field(alias="WaterHeatSchedDefault")
    ] = None
    tariff: Annotated[Optional[Tariff], Field(alias="Tariff")] = None
    space_cool_system: Annotated[
        Optional[dict[str, SpaceCoolSystemFHS]], Field(alias="SpaceCoolSystem")
    ] = None
    space_heat_system: Annotated[
        Optional[dict[str, SpaceHeatSystemFHS]], Field(alias="SpaceHeatSystem")
    ] = None
    thermal_bridging_linear: Annotated[
        Optional[dict[str, ThermalBridgingLinearFHS]], Field(alias="ThermalBridgingLinear")
    ] = None
    external_conditions: Annotated[ExternalConditionsInputFHS, Field(alias="ExternalConditions")]
    hot_water_source: Annotated[HotWaterSourceFHS, Field(alias="HotWaterSource")]
