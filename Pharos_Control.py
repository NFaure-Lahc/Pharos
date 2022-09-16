# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 17:45:13 2022
@author: Nicolas Faure
"""

# This example scenario shows how to use Pharos laser via API.
import requests
import json
import time

# Let's use default laser IP address.
laserEndPoint = "http://192.168.244.10:20022"


# Each request is serialized in JSON format.
requestHeaders = {"Content-Type": "application/json"}

#%% Gestion des paramètres du Pharos
#
# classe principale du Pharos.
# permet de piloter les fonctions de base sans risque pour le laser.
#
class PharosControl():

    ### ---------------------------------------  COMPRESSOR
    # Récupére la position actuelle du compresseur
    def getCompressorPosition():
        response = requests.get(laserEndPoint + "/v0/StretcherCompressor/ActualPosition", headers = requestHeaders)
        if response.status_code == 200:
            return response.text
        else:
            return response.status_code

    # modifie la position du compresseur
    def setCompressorPosition(posComp):
        response = requests.put(laserEndPoint + "/v0/StretcherCompressor/TargetPosition", data = json.dumps(posComp), headers = requestHeaders)
        if response.status_code == 200:
            return "SetCompressorPosition ok"
        else:
            return response.status_code


    ### ---------------------------------------  ATTENUATOR
    # Récupére la position actuelle de l'atténuateur
    def getAttenuatorPosition():
        response = requests.get(laserEndPoint + "/v0/Basic/ActualAttenuatorPercentage", headers = requestHeaders)
        if response.status_code == 200:
            return response.text
        else:
            return response.status_code

    # modifie la position de l'atténuateur
    def setAttenuatorPosition(posAtt):
        response = requests.put(laserEndPoint + "/v0/Basic/TargetAttenuatorPercentage", data = json.dumps(posAtt), headers = requestHeaders)
        if response.status_code == 200:
            return "SetAttenuatorPosition ok"
        else:
            return response.status_code


    ### ---------------------------------------  PP DIVIDER
    # Récupére la position actuelle du Divider
    def getDivider():
        response = requests.get(laserEndPoint + "/v0/Basic/ActualPpDivider", headers = requestHeaders)
        if response.status_code == 200:
            return response.text
        else:
            return response.status_code

    # modifie la position du Divider
    def setDivider(posDiv):
        response = requests.put(laserEndPoint + "/v0/Basic/TargetPpDivider", data = json.dumps(posDiv), headers = requestHeaders)
        if response.status_code == 200:
            return "SetPpDivider ok"
        else:
            return response.status_code


    ### ---------------------------------------  PULSE COUNT
    # Récupére la position actuelle du Divider
    def getPulseCount():
        response = requests.get(laserEndPoint + "/v0/Advanced/ActualPulseCount", headers = requestHeaders)
        if response.status_code == 200:
            return response.text
        else:
            return response.status_code

    # modifie la position du Divider
    def setPulseCount(pulseCount):
        response = requests.put(laserEndPoint + "/v0/Advanced/TargetPulseCount", data = json.dumps(pulseCount), headers = requestHeaders)
        if response.status_code == 200:
            return "SetPulseCount ok"
        else:
            return response.status_code


    ### ---------------------------------------  OUTPUT ENABLE / DISABLE
    def enableOutput(state):
        if (state):
            response = requests.post(laserEndPoint + "/v0/Basic/EnableOutput", headers = requestHeaders)
            if response.status_code == 200:
                return "EnableOutput ok"
            else:
                return response.status_code
        else :
            response = requests.post(laserEndPoint + "/v0/Basic/CloseOutput", headers = requestHeaders)
            if response.status_code == 200:
                return "CloseOutput ok"
            else:
                return response.status_code


    ### ---------------------------------------  PP ENABLE / DISABLE
    def enablePpOutput(state):
        if (state):
            response = requests.post(laserEndPoint + "/v0/Advanced/EnablePp", headers = requestHeaders)
            if response.status_code == 200:
                return "EnablePp ok"
            else:
                return response.status_code
        else :
            response = requests.post(laserEndPoint + "/v0/Advanced/DisablePp", headers = requestHeaders)
            if response.status_code == 200:
                return "DisablePp ok"
            else:
                return response.status_code

    ### ---------------------------------------  OUTPUT ENERGY
    def getOutputEnergy():
        response = requests.get(laserEndPoint + "/v0/Basic/ActualOutputEnergy", headers = requestHeaders)
        if response.status_code == 200:
            return response.text
        else:
            return response.status_code

    ### ---------------------------------------  OUTPUT POWER
    def getOutputPower():
        response = requests.get(laserEndPoint + "/v0/Basic/ActualOutputPower", headers = requestHeaders)
        if response.status_code == 200:
            return response.text
        else:
            return response.status_code

    ### ---------------------------------------  RA POWER
    def getRAPower():
        response = requests.get(laserEndPoint + "/v0/Basic/ActualRaPower", headers = requestHeaders)
        if response.status_code == 200:
            return response.text
        else:
            return response.status_code

    ### ---------------------------------------  OUTPUT FREQUENCY
    def getOutputFrequency():
        response = requests.get(laserEndPoint + "/v0/Basic/ActualOutputFrequency", headers = requestHeaders)
        if response.status_code == 200:
            return response.text
        else:
            return response.status_code

    ### ---------------------------------------  RA FREQUENCY
    def getRAFrequency():
        response = requests.get(laserEndPoint + "/v0/Basic/ActualRAFrequency", headers = requestHeaders)
        if response.status_code == 200:
            return response.text
        else:
            return response.status_code






def main():
    # Test Zone

    print ( PharosControl.getOutputEnergy() )
    print ( PharosControl.getOutputPower() )
    print ( PharosControl.getRAPower() )
    print ( PharosControl.getOutputFrequency() )
    print ( PharosControl.getRAFrequency() )

    """
    print ( PharosControl.setCompressorPosition(47500) )
    time.sleep(0.5)
    print (PharosControl.getCompressorPosition() )
    """
    """
    print ( PharosControl.setAttenuatorPosition(80) )
    time.sleep(0.5)
    print (PharosControl.getAttenuatorPosition() )
    """
    """
    print ( PharosControl.setDividerPosition(50) )
    time.sleep(0.5)
    print (PharosControl.getDividerPosition() )
    """
    """
    print ( PharosControl.setPulseCount(500) )
    time.sleep(0.5)
    print (PharosControl.getPulseCount() )
    """
    #print ( PharosControl.enablePpOutput(True) )



if __name__ == "__main__":
    main()
