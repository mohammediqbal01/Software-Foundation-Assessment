#!/usr/bin/env python3
import sys
import csv
import logging
from typing import List, Tuple
import os

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('data_processing.log'),
        logging.StreamHandler()
    ]
)

def read_csv_file(file_path: str) -> List[List[float]]:
    """
    Read data from a CSV file and convert to float values.
    
    Args:
        file_path (str): Path to the input CSV file
        
    Returns:
        List[List[float]]: List of rows containing float values
        
    Raises:
        FileNotFoundError: If the input file doesn't exist
        ValueError: If the data cannot be converted to floats
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Input file not found: {file_path}")
    
    data = []
    try:
        with open(file_path, 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if len(row) < 3:
                    raise ValueError(f"Row must contain at least 3 values: {row}")
                data.append([float(value) for value in row])
    except ValueError as e:
        raise ValueError(f"Error converting data to float: {str(e)}")
    
    if not data:
        raise ValueError("Input file is empty")
    
    return data

def calculate_statistics(data: List[List[float]]) -> Tuple[float, float, float]:
    """
    Calculate statistics from the data.
    
    Args:
        data (List[List[float]]): Input data
        
    Returns:
        Tuple[float, float, float]: (sum, average, percentage)
    """
    # Calculate sum of all values
    total_sum = sum(sum(row) for row in data)
    
    # Calculate average
    total_values = sum(len(row) for row in data)
    average = total_sum / total_values
    
    # Calculate percentage (using first value as reference)
    first_value = data[0][0]
    percentage = (first_value / total_sum) * 100
    
    return total_sum, average, percentage

def write_results(output_file: str, results: Tuple[float, float, float]) -> None:
    """
    Write calculation results to output file.
    
    Args:
        output_file (str): Path to output file
        results (Tuple[float, float, float]): Results to write
    """
    with open(output_file, 'w') as file:
        file.write("Data Processing Results\n")
        file.write("=====================\n\n")
        file.write(f"Total Sum: {results[0]:.2f}\n")
        file.write(f"Average: {results[1]:.2f}\n")
        file.write(f"Percentage (first value): {results[2]:.2f}%\n")

def main():
    if len(sys.argv) != 2:
        logging.error("Usage: python data_processor.py <input_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = "results.txt"
    
    try:
        # Read and process data
        data = read_csv_file(input_file)
        results = calculate_statistics(data)
        
        # Write results
        write_results(output_file, results)
        
        logging.info(f"Processing completed successfully. Results written to {output_file}")
        
    except Exception as e:
        logging.error(f"Error processing data: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 