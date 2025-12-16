"""
Library for interacting with the OpenTopography API.
"""

import urllib.request
import urllib.parse
import urllib.error
from typing import Dict, Any


def retrieve_dem(params: Dict[str, Any], timeout: int = 30) -> bytes:
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
        timeout: Request timeout in seconds (default: 30)
            
    Returns:
        bytes: The response content (typically a GeoTIFF file)
        
    Raises:
        ValueError: If required parameters are missing
        urllib.error.URLError: If there's a network connection error
        urllib.error.HTTPError: If the API returns an HTTP error
        
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
    # Validate required parameters
    required_params = ['demtype', 'south', 'north', 'west', 'east', 'outputFormat', 'API_Key']
    missing_params = [param for param in required_params if param not in params]
    
    if missing_params:
        raise ValueError(f"Missing required parameters: {', '.join(missing_params)}")
    
    base_url = "https://portal.opentopography.org/API/globaldem"
    
    # Construct the full URL with query parameters
    query_string = urllib.parse.urlencode(params)
    url = f"{base_url}?{query_string}"
    
    # Make the HTTP request with timeout and error handling
    try:
        with urllib.request.urlopen(url, timeout=timeout) as response:
            return response.read()
    except urllib.error.HTTPError as e:
        raise urllib.error.HTTPError(
            e.url, e.code, f"HTTP error {e.code}: {e.reason}", e.hdrs, e.fp
        )
    except urllib.error.URLError as e:
        raise urllib.error.URLError(f"Network error: {e.reason}")
