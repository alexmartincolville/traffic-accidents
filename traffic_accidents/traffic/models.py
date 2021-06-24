# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class FactAccidentVehicle(models.Model):
    accident_index = models.TextField(blank=True, null=True)
    date = models.TextField(blank=True, null=True)
    day_of_week = models.TextField(blank=True, null=True)
    accident_severity = models.TextField(blank=True, null=True)
    road_type = models.TextField(blank=True, null=True)
    speed_limit = models.FloatField(blank=True, null=True)
    make = models.TextField(blank=True, null=True)
    age_band_of_driver = models.TextField(blank=True, null=True)
    driver_home_area_type = models.TextField(blank=True, null=True)
    age_of_vehicle = models.FloatField(blank=True, null=True)
    journey_purpose_of_driver = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fact_accident_vehicle'


class InputAccidentInformation(models.Model):
    accident_index = models.TextField(db_column='Accident_Index', blank=True, null=True)  # Field name made lowercase.
    number_1st_road_class = models.TextField(db_column='1st_Road_Class', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1st_road_number = models.FloatField(db_column='1st_Road_Number', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2nd_road_class = models.TextField(db_column='2nd_Road_Class', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2nd_road_number = models.FloatField(db_column='2nd_Road_Number', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    accident_severity = models.TextField(db_column='Accident_Severity', blank=True, null=True)  # Field name made lowercase.
    carriageway_hazards = models.TextField(db_column='Carriageway_Hazards', blank=True, null=True)  # Field name made lowercase.
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    day_of_week = models.TextField(db_column='Day_of_Week', blank=True, null=True)  # Field name made lowercase.
    did_police_officer_attend_scene_of_accident = models.FloatField(db_column='Did_Police_Officer_Attend_Scene_of_Accident', blank=True, null=True)  # Field name made lowercase.
    junction_control = models.TextField(db_column='Junction_Control', blank=True, null=True)  # Field name made lowercase.
    junction_detail = models.TextField(db_column='Junction_Detail', blank=True, null=True)  # Field name made lowercase.
    latitude = models.FloatField(db_column='Latitude', blank=True, null=True)  # Field name made lowercase.
    light_conditions = models.TextField(db_column='Light_Conditions', blank=True, null=True)  # Field name made lowercase.
    local_authority_district_field = models.TextField(db_column='Local_Authority_(District)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    local_authority_highway_field = models.TextField(db_column='Local_Authority_(Highway)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    location_easting_osgr = models.FloatField(db_column='Location_Easting_OSGR', blank=True, null=True)  # Field name made lowercase.
    location_northing_osgr = models.FloatField(db_column='Location_Northing_OSGR', blank=True, null=True)  # Field name made lowercase.
    longitude = models.FloatField(db_column='Longitude', blank=True, null=True)  # Field name made lowercase.
    lsoa_of_accident_location = models.TextField(db_column='LSOA_of_Accident_Location', blank=True, null=True)  # Field name made lowercase.
    number_of_casualties = models.BigIntegerField(db_column='Number_of_Casualties', blank=True, null=True)  # Field name made lowercase.
    number_of_vehicles = models.BigIntegerField(db_column='Number_of_Vehicles', blank=True, null=True)  # Field name made lowercase.
    pedestrian_crossing_human_control = models.FloatField(db_column='Pedestrian_Crossing-Human_Control', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pedestrian_crossing_physical_facilities = models.FloatField(db_column='Pedestrian_Crossing-Physical_Facilities', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    police_force = models.TextField(db_column='Police_Force', blank=True, null=True)  # Field name made lowercase.
    road_surface_conditions = models.TextField(db_column='Road_Surface_Conditions', blank=True, null=True)  # Field name made lowercase.
    road_type = models.TextField(db_column='Road_Type', blank=True, null=True)  # Field name made lowercase.
    special_conditions_at_site = models.TextField(db_column='Special_Conditions_at_Site', blank=True, null=True)  # Field name made lowercase.
    speed_limit = models.FloatField(db_column='Speed_limit', blank=True, null=True)  # Field name made lowercase.
    time = models.TextField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    urban_or_rural_area = models.TextField(db_column='Urban_or_Rural_Area', blank=True, null=True)  # Field name made lowercase.
    weather_conditions = models.TextField(db_column='Weather_Conditions', blank=True, null=True)  # Field name made lowercase.
    year = models.BigIntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    inscotland = models.TextField(db_column='InScotland', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'input_accident_information'


class InputVehicleInformation(models.Model):
    accident_index = models.TextField(db_column='Accident_Index', blank=True, null=True)  # Field name made lowercase.
    age_band_of_driver = models.TextField(db_column='Age_Band_of_Driver', blank=True, null=True)  # Field name made lowercase.
    age_of_vehicle = models.FloatField(db_column='Age_of_Vehicle', blank=True, null=True)  # Field name made lowercase.
    driver_home_area_type = models.TextField(db_column='Driver_Home_Area_Type', blank=True, null=True)  # Field name made lowercase.
    driver_imd_decile = models.FloatField(db_column='Driver_IMD_Decile', blank=True, null=True)  # Field name made lowercase.
    engine_capacity_cc_field = models.FloatField(db_column='Engine_Capacity_.CC.', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    hit_object_in_carriageway = models.TextField(db_column='Hit_Object_in_Carriageway', blank=True, null=True)  # Field name made lowercase.
    hit_object_off_carriageway = models.TextField(db_column='Hit_Object_off_Carriageway', blank=True, null=True)  # Field name made lowercase.
    journey_purpose_of_driver = models.TextField(db_column='Journey_Purpose_of_Driver', blank=True, null=True)  # Field name made lowercase.
    junction_location = models.TextField(db_column='Junction_Location', blank=True, null=True)  # Field name made lowercase.
    make = models.TextField(blank=True, null=True)
    model = models.TextField(blank=True, null=True)
    propulsion_code = models.TextField(db_column='Propulsion_Code', blank=True, null=True)  # Field name made lowercase.
    sex_of_driver = models.TextField(db_column='Sex_of_Driver', blank=True, null=True)  # Field name made lowercase.
    skidding_and_overturning = models.TextField(db_column='Skidding_and_Overturning', blank=True, null=True)  # Field name made lowercase.
    towing_and_articulation = models.TextField(db_column='Towing_and_Articulation', blank=True, null=True)  # Field name made lowercase.
    vehicle_leaving_carriageway = models.TextField(db_column='Vehicle_Leaving_Carriageway', blank=True, null=True)  # Field name made lowercase.
    vehicle_location_restricted_lane = models.FloatField(db_column='Vehicle_Location.Restricted_Lane', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    vehicle_manoeuvre = models.TextField(db_column='Vehicle_Manoeuvre', blank=True, null=True)  # Field name made lowercase.
    vehicle_reference = models.BigIntegerField(db_column='Vehicle_Reference', blank=True, null=True)  # Field name made lowercase.
    vehicle_type = models.TextField(db_column='Vehicle_Type', blank=True, null=True)  # Field name made lowercase.
    was_vehicle_left_hand_drive = models.TextField(db_column='Was_Vehicle_Left_Hand_Drive', blank=True, null=True)  # Field name made lowercase.
    x1st_point_of_impact = models.TextField(db_column='X1st_Point_of_Impact', blank=True, null=True)  # Field name made lowercase.
    year = models.BigIntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'input_vehicle_information'
