"""
Library for interacting with the OpenTopography API.
"""

import urllib.request
import urllib.parse
from typing import Dict, Any


def retrieve_dem(params: Dict[str, Any]) -> bytes:
    """
    Retrieve DEM (Digital Elevation Model) data from OpenTopography API.
    
    Args:
        params: Dictionary containing the API parameters:
            - demtype: Type of DEM (e.g., 'SRTMGL3')
            - south: Southern boundary latitude
            - north: Northern boundary latitude
            - west: Western boundary longitude
            - east: Eastern boundary longitude
            - outputFormat: Output format (e.g., 'GTiff')
            - API_Key: API key for authentication
            
    Returns:
        bytes: The response content (typically a GeoTIFF file)
        
    Example:
        >>> params = {
        ...     'demtype': 'SRTMGL3',
        ...     'south': -25.451567,
        ...     'north': -25.418431,
        ...     'west': -49.308291,
        ...     'east': -49.235979,
        ...     'outputFormat': 'GTiff',
        ...     'API_Key': 'demoapikeyot2022'
        ... }
        >>> data = retrieve_dem(params)
    
    TODO: Set up API_Key as a secret/environment variable instead of passing it directly
    """
    base_url = "https://portal.opentopography.org/API/globaldem"
    
    # Construct the full URL with query parameters
    query_string = urllib.parse.urlencode(params)
    url = f"{base_url}?{query_string}"
    
    # Make the HTTP request
    with urllib.request.urlopen(url) as response:
        return response.read()
