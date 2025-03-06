import streamlit as st

# Title of the app
st.title("🔍  Unit Converter")

# Sidebar for selecting the type of conversion
st.sidebar.header("Settings")
conversion_type = st.sidebar.selectbox(
    "Choose a conversion type:",
    ["Length", "Weight", "Temperature", "Volume", "Area", "Speed", "Time"]
)

# Function to get units based on conversion type
def get_units(conversion_type):
    units = {
        "Length": ["Meters", "Feet", "Kilometers", "Miles", "Inches", "Yards"],
        "Weight": ["Kilograms", "Pounds", "Grams", "Ounces", "Tons"],
        "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
        "Volume": ["Liters", "Gallons", "Milliliters", "Ounces", "Cubic Meters"],
        "Area": ["Square Meters", "Square Feet", "Square Kilometers", "Square Miles", "Acres"],
        "Speed": ["Meters/Second", "Kilometers/Hour", "Miles/Hour", "Feet/Second"],
        "Time": ["Seconds", "Minutes", "Hours", "Days", "Weeks"]
    }
    return units.get(conversion_type, [])

# Function to perform conversions
def convert(value, from_unit, to_unit, conversion_type):
    # Conversion logic for each type
    if conversion_type == "Length":
        conversions = {
            "Meters": {"Feet": 3.28084, "Kilometers": 0.001, "Miles": 0.000621371, "Inches": 39.3701, "Yards": 1.09361},
            "Feet": {"Meters": 0.3048, "Kilometers": 0.0003048, "Miles": 0.000189394, "Inches": 12, "Yards": 0.333333},
            "Kilometers": {"Meters": 1000, "Feet": 3280.84, "Miles": 0.621371, "Inches": 39370.1, "Yards": 1093.61},
            "Miles": {"Meters": 1609.34, "Feet": 5280, "Kilometers": 1.60934, "Inches": 63360, "Yards": 1760},
            "Inches": {"Meters": 0.0254, "Feet": 0.0833333, "Kilometers": 0.0000254, "Miles": 0.000015783, "Yards": 0.0277778},
            "Yards": {"Meters": 0.9144, "Feet": 3, "Kilometers": 0.0009144, "Miles": 0.000568182, "Inches": 36}
        }
    elif conversion_type == "Weight":
        conversions = {
            "Kilograms": {"Pounds": 2.20462, "Grams": 1000, "Ounces": 35.274, "Tons": 0.001},
            "Pounds": {"Kilograms": 0.453592, "Grams": 453.592, "Ounces": 16, "Tons": 0.000453592},
            "Grams": {"Kilograms": 0.001, "Pounds": 0.00220462, "Ounces": 0.035274, "Tons": 0.000001},
            "Ounces": {"Kilograms": 0.0283495, "Pounds": 0.0625, "Grams": 28.3495, "Tons": 0.0000283495},
            "Tons": {"Kilograms": 1000, "Pounds": 2204.62, "Grams": 1000000, "Ounces": 35274}
        }
    elif conversion_type == "Temperature":
        if from_unit == "Celsius":
            if to_unit == "Fahrenheit":
                return (value * 9/5) + 32
            elif to_unit == "Kelvin":
                return value + 273.15
        elif from_unit == "Fahrenheit":
            if to_unit == "Celsius":
                return (value - 32) * 5/9
            elif to_unit == "Kelvin":
                return (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin":
            if to_unit == "Celsius":
                return value - 273.15
            elif to_unit == "Fahrenheit":
                return (value - 273.15) * 9/5 + 32
        return value
    elif conversion_type == "Volume":
        conversions = {
            "Liters": {"Gallons": 0.264172, "Milliliters": 1000, "Ounces": 33.814, "Cubic Meters": 0.001},
            "Gallons": {"Liters": 3.78541, "Milliliters": 3785.41, "Ounces": 128, "Cubic Meters": 0.00378541},
            "Milliliters": {"Liters": 0.001, "Gallons": 0.000264172, "Ounces": 0.033814, "Cubic Meters": 0.000001},
            "Ounces": {"Liters": 0.0295735, "Gallons": 0.0078125, "Milliliters": 29.5735, "Cubic Meters": 0.0000295735},
            "Cubic Meters": {"Liters": 1000, "Gallons": 264.172, "Milliliters": 1000000, "Ounces": 33814}
        }
    elif conversion_type == "Area":
        conversions = {
            "Square Meters": {"Square Feet": 10.7639, "Square Kilometers": 0.000001, "Square Miles": 0.000000386102, "Acres": 0.000247105},
            "Square Feet": {"Square Meters": 0.092903, "Square Kilometers": 0.000000092903, "Square Miles": 0.0000000358701, "Acres": 0.0000229568},
            "Square Kilometers": {"Square Meters": 1000000, "Square Feet": 10763910.4, "Square Miles": 0.386102, "Acres": 247.105},
            "Square Miles": {"Square Meters": 2589988.11, "Square Feet": 27878400, "Square Kilometers": 2.58999, "Acres": 640},
            "Acres": {"Square Meters": 4046.86, "Square Feet": 43560, "Square Kilometers": 0.00404686, "Square Miles": 0.0015625}
        }
    elif conversion_type == "Speed":
        conversions = {
            "Meters/Second": {"Kilometers/Hour": 3.6, "Miles/Hour": 2.23694, "Feet/Second": 3.28084},
            "Kilometers/Hour": {"Meters/Second": 0.277778, "Miles/Hour": 0.621371, "Feet/Second": 0.911344},
            "Miles/Hour": {"Meters/Second": 0.44704, "Kilometers/Hour": 1.60934, "Feet/Second": 1.46667},
            "Feet/Second": {"Meters/Second": 0.3048, "Kilometers/Hour": 1.09728, "Miles/Hour": 0.681818}
        }
    elif conversion_type == "Time":
        conversions = {
            "Seconds": {"Minutes": 0.0166667, "Hours": 0.000277778, "Days": 0.0000115741, "Weeks": 0.00000165344},
            "Minutes": {"Seconds": 60, "Hours": 0.0166667, "Days": 0.000694444, "Weeks": 0.0000992063},
            "Hours": {"Seconds": 3600, "Minutes": 60, "Days": 0.0416667, "Weeks": 0.00595238},
            "Days": {"Seconds": 86400, "Minutes": 1440, "Hours": 24, "Weeks": 0.142857},
            "Weeks": {"Seconds": 604800, "Minutes": 10080, "Hours": 168, "Days": 7}
        }

    if from_unit == to_unit:
        return value
    return value * conversions[from_unit][to_unit]

# Main UI
st.header(f"🔧 {conversion_type} Conversion")
units = get_units(conversion_type)
col1, col2 = st.columns(2)
with col1:
    from_unit = st.selectbox("From:", units, key="from_unit")
with col2:
    to_unit = st.selectbox("To:", units, key="to_unit")
value = st.number_input("Enter value:", value=1.0, key="value")

# Real-time conversion
if value is not None:
    result = convert(value, from_unit, to_unit, conversion_type)
    st.success(f"**Converted Value:** {result:.6f} {to_unit}")