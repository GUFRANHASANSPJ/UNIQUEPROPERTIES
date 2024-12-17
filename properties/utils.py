from django.utils.text import slugify
import os,re
from django.db.models import Q
from properties.models import *
from decimal import Decimal

def calculate_overall_rating(property_instance):
    """
    Calculate the overall rating for a property instance.
    """
    points = 0

    # Calculate points based on Building Age
    if property_instance.Building_Age in range(0, 5):
        points += 5
    elif property_instance.Building_Age in range(5, 10):
        points += 4
    elif property_instance.Building_Age in range(10, 15):
        points += 3
    elif property_instance.Building_Age in range(15, 20):
        points += 2

    # Check if pet-friendly
    if property_instance.pet_friendly == 1:
        points += 5

    # check For parking
    if property_instance.parking == 'car':
        points += 5
    elif property_instance.parking == 'two wheeler':
        points += 3

    # check for furnish
    if property_instance.furnish_detail == 'Furnished':
        points += 5
    elif property_instance.furnish_detail == 'Semi-Furnished':
        points += 3

    # check for Sunlight
    if property_instance.sunlight_access == 1:
        points += 5

    # check for road_side_parking
    if property_instance.road_side_parking == 1:
        points += 5

    # check for water_drainage
    if property_instance.water_drainage == 1:
        points += 5



    # check for balcony
    if property_instance.balcony == 1:
        points += 5

    # check for basement
    if property_instance.basement == 1:
        points += 5

    # check for roof_condition
    if property_instance.roof_condition == "New":
        points += 5

    # check for roof_condition
    if property_instance.flooring == "Hardwood":
        points += 5
    elif property_instance.flooring == "Tile":
        points += 3
    
    elif property_instance.flooring == "Carpet":
        points += 2
    
    # check for ceiling_condition
    if property_instance.ceiling_condition == "Standard":
        points += 5
    else:
        points+=3
    
    # check for air_Pollution_Levels
    if property_instance.air_Pollution_Levels == "Low":
        points += 5
    else:
        points+=3
    
    # check for Noise_Pollution
    if property_instance.Noise_Pollution == "Low":
        points += 5
    else:
        points+=3

    # check for Flood_Zone
    if property_instance.Flood_Zone == 0:
        points += 5

    # check for Earthquake_zone
    if property_instance.Earthquake_zone == 0:
        points += 5

    # check for handicap_accesibility
    if property_instance.handicap_accesibility == "Low":
        points += 3
    elif property_instance.handicap_accesibility == "Moderate":
        points += 2
    
    # check for road_quality
    if property_instance.road_quality == "Paved":
        points += 5

    # check for Neighborhood_Crime_Rate
    if property_instance.Neighborhood_Crime_Rate == "Low":
        points += 5
    else:
        points+=3

    # check for Internet_Speed
    if property_instance.Internet_Speed == "High":
        points += 5
    else:
        points+=3

    # check for Cell_Network_Coverage
    if property_instance.Cell_Network_Coverage == "Good":
        points += 5
    else:
        points+=3

    # check for Earthquake_zone
    if property_instance.Electric_Vehicle_Charging == 1:
        points += 5

    # check for Smart_Home_Features
    for i in property_instance.Smart_Home_Features:
        if i in ('Sports',):
            points += 2
        if i in ('Arts',):
            points += 2
        if i in ('Volunteer',):
            points += 1

    # check for Community_Events
    if property_instance.Community_Events == "Monthly":
        points += 5
    elif property_instance.Community_Events == "Quaterly":
        points += 3
    elif property_instance.Community_Events == "Yearly":
        points += 1

     # check for Gardens_Greenery
    if property_instance.Gardens_Greenery == 'Private':
        points += 5
    if property_instance.Gardens_Greenery == 'Community':
        points += 2

    # check for Pet_Friendly_Areas
    if property_instance.Pet_Friendly_Areas == 1:
        points += 5

    # check for Childcare_Centers
    if property_instance.Childcare_Centers == 1:
        points += 5

    # check for Playgrounds
    if property_instance.Playgrounds == "Nearby":
        points += 5
    else:
        points+=3

    # check for Electricity_Reliability
    if property_instance.Electricity_Reliability == "High":
        points += 5
    else:
        points+=3

    # check for Water_Supply_Quality
    if property_instance.Water_Supply_Quality == "Good":
        points += 5
    else:
        points+=3

    # check for Waste_Collection
    if property_instance.Waste_Collection == "Weekly":
        points += 5
    else:
        points+=3

    # check for Historical_Building_Status
    if property_instance.Historical_Building_Status == "Yes":
        points += 5

    # check for Cultural_Heritage_Sites
    if property_instance.Cultural_Heritage_Sites == "Nearby":
        points += 5

    # check for Luxury_Amenities
    for i in property_instance.Luxury_Amenities:
        if i in ('Gym',):
            points += 2
        if i in ('Pool',):
            points += 2

    # check for Assigned_Parking
    if property_instance.Community_Centers == "Yes":
        points += 5

    # check for Community_Centers
    if property_instance.Bicycle_Parking == "Yes":
        points += 5

    # check for Community_Centers
    if property_instance.Bicycle_Parking == "Yes":
        points += 5



    # Calculate percentage
    max_points = 190
    percentage = (points / max_points) * 100

    # Convert percentage to rating
    if percentage > 80:
        return 5.0
    return round((percentage / 20) + 1, 1)


def save_images_to_property_folder(property_name, image_files):
    """
    Saves uploaded images into a property-specific folder and returns their paths.
    """
    image_paths = []

    # Generate property-specific folder name
    property_folder_name = slugify(property_name)
    property_folder_path = os.path.join('media/properties_img', property_folder_name)

    # Ensure the directory exists
    os.makedirs(property_folder_path, exist_ok=True)

    for image in image_files:
        # Generate a sanitized file name
        sanitized_name = slugify(image.name, allow_unicode=False)
        image_path = f"/media/properties_img/{property_folder_name}/{sanitized_name}"
        image_paths.append(image_path)

        # Full path to save the image
        full_path = os.path.join(property_folder_path, sanitized_name)

        # Save the image
        try:
            with open(full_path, 'wb') as destination:
                for chunk in image.chunks():
                    destination.write(chunk)
        except IOError as e:
            # Handle file saving error (e.g., log it)
            print(f"Error saving file {sanitized_name}: {e}")

    return image_paths

# Function to generate bot responses using regex patterns
def get_bot_response(user_input):

    # Greeting patterns
    if re.search(r'\b(hello|hi|hey|hola)\b', user_input):
        return "Hello! How can I help you today?"
    
    # Farewell patterns
    elif re.search(r'\b(bye|goodbye|see you)\b', user_input):
        return "Goodbye! Have a great day!"
    
    # Service-related inquiry patterns
    elif re.search(r'\b(what do you offer|services?)\b', user_input):
        return "We offer a variety of properties for sale and rent, as well as assistance from top real estate agents."
    
    # Business hours inquiry
    elif re.search(r'\b(working hours|open|hours)\b', user_input):
        return "We are open Monday to Friday from 9 AM to 6 PM."
    
    # Price-related inquiries
    elif re.search(r'\b(how much|price)\b', user_input):
        return "Our prices vary depending on the property. Please specify the property type and location for a quote."
    
    # Default fallback message
    return "Sorry, I didn't understand that. Can you please rephrase?"



def get_similar_properties(property_instance, limit=4):
    """
    Get similar properties based on certain attributes.
    :param property_instance: The property instance for which similar properties are fetched.
    :param limit: Number of similar properties to fetch.
    :return: Queryset of similar properties.
    """
    # Start with a basic filter that checks matching property type, city, state, and property info
    similar_properties = property.objects.filter(
        Q(property_type=property_instance.property_type) |
        Q(city=property_instance.city) |
        Q(state=property_instance.state) |
        Q(proprty_info=property_instance.proprty_info) |
        Q(proprty_status=True)  # Only active properties
    ).exclude(id=property_instance.id)  # Exclude the current property

    # Debugging: Check the count of similar properties before price filtering
    print(f"Similar properties before price filter: {similar_properties.count()}")

    # Further filter by price range (±20% price) if property_price exists
    if property_instance.property_price:
        price_range_min = property_instance.property_price * Decimal('0.4')
        price_range_max = property_instance.property_price * Decimal('2.2')

        # Print the calculated price range for debugging
        print(f"Price range: {price_range_min} to {price_range_max}")
        
        similar_properties = similar_properties.filter(
            property_price__gte=price_range_min,
            property_price__lte=price_range_max
        )

        # Debugging: Check the count of similar properties after price filtering
        print(f"Similar properties after price filter: {similar_properties.count()}")

    # Print the final count of similar properties
    print(f"Number of similar properties found: {similar_properties.count()}")
    
    return similar_properties[:limit]  # Limit the results


