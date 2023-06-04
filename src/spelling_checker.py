import difflib
import json
import sys

def auto_correct_city_name(city_name, city_list, n=3):
    matches = difflib.get_close_matches(city_name, city_list, n=n)
    return matches


def spell_check(city_name):
    file = json.load(open("city.list.json"))
    cities = [city['name'].lower() for city in file]
    city_name = city_name.lower()
    if city_name in cities:
        return city_name
    else:
        matches = list(set(auto_correct_city_name(city_name, cities, n=3)))
        # print(matches)
        if len(matches) > 0:
            for match in matches:
                print("\nDid you mean %s instead?" % match.capitalize())
                decide = input("\nPress y for yes or n for no: ")
                if decide == "y":
                    return match
                elif decide == "n":
                    if match == matches[-1]:
                        return "City not found"
                    else:
                        continue
                else:
                    return "\nYou have entered wrong input please enter just y or n"
        else:
            return "City not found"
