"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    # TODO: Load NEO data from the given CSV file.
    list_of_neos = []
    with open(neo_csv_path, 'r') as neos_csv:
        reader = csv.DictReader(neos_csv)
        for row in reader:
            list_of_neos.append(NearEarthObject(row['pdes'], row['name'], row['diameter'], row['pha'], []))
    return list_of_neos

def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    # TODO: Load close approach data from the given JSON file.
    list_of_cas = []
    with open(cad_json_path, 'r') as cad_json:
        reader = json.load(cad_json)
        for row in reader['data']:
            approach = dict(zip(reader['fields'], row))
            list_of_cas.append(CloseApproach(approach['des'], approach['cd'], approach['dist'], approach['v_rel'],  None))
    return list_of_cas

neos = load_neos('data/neos.csv')
print(len(neos))
print(type(neos))
print(type(neos[0]))

approaches = load_approaches('data/cad.json')
print(len(approaches))
print(type(approaches))
print(type(approaches[0]))