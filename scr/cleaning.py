def coincidencia(string):
    """
    Takes the data that match the pattern
    Args:
        string: dates of the dataframe 
    Reurns:
        The dataframe just with the dates
    """
    pattern = r'^[0-9]{4}-[0-9]{2}-[0-9]{2}'
    import re
    try:
        return re.search(pattern, string).group().lower()
    except:
        return f"Error"