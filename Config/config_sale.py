class ConfigSale:

    """ 
    Ruta del archivo CSV de entrada (el limpio    
    """
    INPUT_PATH = 'Extract/Files/Sale_G_limpio.csv'

    """ 
    Ruta de la base de datos SQLite donde se guardarán los datos    
    """
    SQLITE_DB_PATH = 'Extract/Files/sales_data.db'

    """ 
    Nombre de la tabla dentro de la base de datos  
    """
    SQLITE_TABLE = 'sales_clean'

    
    OUTPUT_PATH = 'Extract/Files/sales_clean_output.csv'
