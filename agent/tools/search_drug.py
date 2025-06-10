import pandas as pd
import os
from typing import List, Dict, Any
from langchain_core.tools import tool


def load_icd10_data() -> pd.DataFrame:
    """Load the ICD-10CM drug data from CSV file."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(current_dir, "..", "..", "data", "icd10cm-drug.csv")
    
    try:
        df = pd.read_csv(csv_path)
        return df
    except FileNotFoundError:
        raise FileNotFoundError(f"ICD-10CM drug data file not found at {csv_path}")


def search_substance(disease_name: str, df: pd.DataFrame, limit: int = 10) -> List[Dict[str, Any]]:
    """Search for substances in the ICD-10 data."""
    disease_name_lower = disease_name.lower()    
    mask = df['Substance'].str.lower().str.contains(disease_name_lower, na=False)
    results = df[mask].head(limit)
    
    search_results = []
    for _, row in results.iterrows():
        result = {
            'substance': row['Substance'],
            'poisoning_accidental': row['Poisoning Accidental (unintentional)'],
            'poisoning_intentional': row['Poisoning Intentional self-harm'],
            'poisoning_assault': row['Poisoning Assault'],
            'poisoning_undetermined': row['Poisoning Undetermined'],
            'adverse_effect': row['Adverse effect'],
            'underdosing': row['Underdosing']
        }
        search_results.append(result)
    
    return search_results


@tool
def search_drug(disease_name: str) -> str:
    """
    Search for ICD-10 codes related to drugs, substances, and poisoning.

    Args:
        disease_name: The name of the disease to search for.

    Returns:
        A string with the ICD-10 codes found for the query.
    """
    try:
        df = load_icd10_data()
        results = search_substance(disease_name, df, limit=5)
        
        if not results:
            return f"No ICD-10 codes found for substance: {disease_name}"
        
        output = []
        output.append(f"ICD-10 codes found for '{disease_name}':\n")
        
        for i, result in enumerate(results, 1):
            output.append(f"{i}. Substance: {result['substance']}")
            
            codes = []
            if result['poisoning_accidental'] != '--':
                codes.append(f"Accidental poisoning: {result['poisoning_accidental']}")
            if result['poisoning_intentional'] != '--':
                codes.append(f"Intentional self-harm: {result['poisoning_intentional']}")
            if result['poisoning_assault'] != '--':
                codes.append(f"Assault: {result['poisoning_assault']}")
            if result['poisoning_undetermined'] != '--':
                codes.append(f"Undetermined: {result['poisoning_undetermined']}")
            if result['adverse_effect'] != '--':
                codes.append(f"Adverse effect: {result['adverse_effect']}")
            if result['underdosing'] != '--':
                codes.append(f"Underdosing: {result['underdosing']}")
            
            if codes:
                output.append("   " + "\n   ".join(codes))
            else:
                output.append("   No specific ICD-10 codes available")
            
            output.append("") 
        
        return "\n".join(output)
        
    except Exception as e:
        return f"Error searching ICD-10 data: {str(e)}"
