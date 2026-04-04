import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logging(log_directory="logs", log_file_name="ai_system.log"):
    """
    Configures the logging mechanism to write to both console and a rotating file.
    """
    # Ensure the log directory exists
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)
    
    log_file_path = os.path.join(log_directory, log_file_name)

    # Define the log format
    log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    date_format = '%Y-%m-%d %H:%M:%S'
    formatter = logging.Formatter(log_format, datefmt=date_format)

    # Get the root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO) # Set the default logging level

    # --- Console Handler ---
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    root_logger.addHandler(console_handler)

    # --- File Handler (Rotating) ---
    # Max size of 1 MB, keep 5 backup files
    file_handler = RotatingFileHandler(
        log_file_path, 
        maxBytes=1024 * 1024, 
        backupCount=5
    )
    file_handler.setFormatter(formatter)
    root_logger.addHandler(file_handler)

    logging.info("Logging system configured successfully.")

# --- Example Usage in an AI System Module ---

def process_data(data):
    """Simulates an AI system function."""
    logger = logging.getLogger("DataProcessor")
    try:
        if not data:
            raise ValueError("Data cannot be empty")
        
        logger.info(f"Starting data processing for {len(data)} items.")
        # ... processing logic ...
        logger.debug("Intermediate calculation step.") # DEBUG level won't show with INFO default
        logger.warning("Potential data anomaly detected.")
        return True
    except ValueError as e:
        logger.error(f"Error during data processing: {e}", exc_info=True)
        return False
    except Exception as e:
        logger.critical(f"A critical error occurred: {e}")
        return False

# --- Main execution ---
if __name__ == "__main__":
    setup_logging()
    
    # Test the logging
    process_data(["item1", "item2"])
    process_data([]) # This will trigger an error
    
    logging.info("System shutdown.")