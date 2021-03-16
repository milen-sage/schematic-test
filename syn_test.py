import pandas as pd
import wget
import json
import logging

import synapseclient

import schematic # for now install from here: https://github.com/Sage-Bionetworks/schematic/tree/develop
from schematic import CONFIG
from schematic.store.synapse import SynapseStorage
from schematic.schemas.explorer import SchemaExplorer


def get_file_project_id(syn_id, syn_store):

    # get a list of all files in asset store
    all_files = syn_store.storageFileviewTable

    # get the project of a specified file
    project_id = all_files[all_files["id"] == syn_id][["projectId"]].to_dict()
    
    return project_id

if __name__ == '__main__':

    logging.disable(logging.DEBUG)
     
    # load schematic config
    schematic.CONFIG.load_config('./config-htan.yml')
    
    # instantiate synapse client
    syn = synapseclient.Synapse()

    try:
        syn.login(rememberMe = True)
    except synapseclient.core.exceptions.SynapseNoCredentialsError:
        print("Please make sure the 'username' and 'password'/'api_key' values have been filled out in .synapseConfig.")
    except synapseclient.core.exceptions.SynapseAuthenticationError:
        print("Please make sure the credentials in the .synapseConfig file are correct.")

    # instantiate storage assets (e.g. master fileview specified in config)
    syn_store = SynapseStorage()

    # file syn ID
    syn_id = "syn24829481"

    project_id = get_file_project_id(syn_id, syn_store)

    print(project_id)

