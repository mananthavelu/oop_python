"""

Extract data.

on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file,
formatted as described in the project instructions, into a collection
of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the
command line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """
    
    Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about
    near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    list_of_neos = []
    with open(neo_csv_path, 'r') as neos_csv:
        reader = csv.DictReader(neos_csv)
        for row in reader:
            diameter = (float(row['diameter']) if
                        row['diameter'] != "" else float('nan'))
            name = row['name'] if row['name'] != "" else None
            hazardous = row['pha'] if row['pha'] != "" else False
            (list_of_neos.append(NearEarthObject(row['pdes'],
             name, diameter, hazardous, [])))
    return list_of_neos


def load_approaches(cad_json_path):
    """
    
    Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about
    close approaches.
    :return: A collection of `CloseApproach`es.
    """
    list_of_cas = []
    with open(cad_json_path, 'r') as cad_json:
        reader = json.load(cad_json)
        for row in reader['data']:
            approach = dict(zip(reader['fields'], row))
            distance = (float(approach['dist']) if
                        approach['dist'] is not None else float('nan'))
            velocity = (float(approach['v_rel']) if approach['v_rel']
                        is not None else float('nan'))
            list_of_cas.append(CloseApproach(approach['des'], approach['cd'],
                               distance, velocity,  None))
    return list_of_cas
