import json

# Read the input file
with open('Community-centre.json', 'r') as file:
    data = json.load(file)

# Check if input is a FeatureCollection and extract features
if isinstance(data, dict) and 'features' in data:
    features = data['features']
else:
    features = data  # Assuming input is already a list of features

geojson_data = []

for feature in features:
    try:
        properties = feature.get('properties', {})
        geojson_feature = {
            "id": feature.get("id", ""),
            "type": "Feature",
            "properties": {
                "COMMUNITY_CENTRE": properties.get("COMMUNITY_CENTRE", ""),
                "ADDRESS1": properties.get("ADDRESS1", ""),
                "ADDRESS2": properties.get("ADDRESS2", ""),
                "TOWN": properties.get("TOWN", ""),
                "POSTCODE": properties.get("POSTCODE", ""),
                "PHONE": properties.get("PHONE", ""),
                "UPRN": properties.get("UPRN", ""),
                "OTHER_INFORMATION": properties.get("OTHER_INFORMATION", "")
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    float(properties.get("LONGITUDE", 0)),
                    float(properties.get("LATITUDE", 0))
                ]
            }
        }
        geojson_data.append(geojson_feature)
    except Exception as e:
        print(f"Error processing feature {feature.get('id', 'unknown')}: {e}")

# Write the output file
with open('community-centre-GeoJSON.json', 'w') as outfile:
    json.dump(geojson_data, outfile, indent=2)

print(f"Changed {len(geojson_data)} community centers to GeoJSON format")