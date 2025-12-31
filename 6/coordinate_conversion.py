def direction_by_sign(value, coord_type):
    if coord_type == "lon":
        return "W" if value < 0 else "E"
    else:
        return "S" if value < 0 else "N"

def dd_to_dms(value, coord_type):
    
    direction = direction_by_sign(value, coord_type)
    
    value = abs(value)

    degrees = int(value)
    remainder = value - degrees

    minutes_full = remainder * 60
    minutes = int(minutes_full)
    
    seconds = (minutes_full - minutes) * 60

    return [degrees, minutes, round(seconds, 2), direction]

def coordinate_conversion(data):
    result = {}

    for city, info in data.items():
        dd_values = info["dd"]
        dms_values = []

        dms_values.append(dd_to_dms(dd_values[0], "lon"))
        dms_values.append(dd_to_dms(dd_values[1], "lat"))

        if len(dd_values) > 2:
            dms_values.append(dd_values[2])

        result[city] = {
            "dd": dd_values,
            "dms": dms_values
        }

    return result

# Test cases

coordinates = {
    "anchorage": {
        "dd": [-149.9002, 61.2181, 22]
    },
    "los_angeles": {
        "dd": [-118.2437, 34.0522]
    }
}

expected_output = {
    "anchorage": {
        "dd": [-149.9002, 61.2181, 22],
        "dms": [[149, 54, 0.72, "W"], [61, 13, 5.16, "N"], 22]
    },
    "los_angeles": {
        "dd": [-118.2437, 34.0522],
        "dms": [[118, 14, 37.32, "W"], [34, 3, 7.92, "N"]]
    }
}

result = coordinate_conversion(coordinates)

if result == expected_output:
    print("Test passed")
else:
    print("Test failed")
    print("Expected:")
    print(expected_output)
    print("Got:")
    print(result)

converted = coordinate_conversion(coordinates)
print(converted)















