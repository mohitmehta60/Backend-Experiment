#!/usr/bin/env python3
"""
Ensure the ML model is trained and available before starting the API server.
This script checks if the model exists and trains it if necessary.
"""

import os
import sys
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def ensure_model_exists():
    """Ensure the ML model is trained and available."""
    
    # Paths
    base_dir = Path(__file__).parent
    model_dir = base_dir / "My new ml model"
    model_path = model_dir / "models" / "fertilizer_recommender.pkl"
    train_script = model_dir / "train.py"
    dataset_path = model_dir / "New dataset 5111 rows.csv"
    
    logger.info(f"Checking for model at: {model_path}")
    
    # Check if model already exists
    if model_path.exists():
        logger.info("✅ Model file already exists")
        return True
    
    logger.info("❌ Model file not found, attempting to train...")
    
    # Check if training script exists
    if not train_script.exists():
        logger.error(f"Training script not found: {train_script}")
        return False
    
    # Check if dataset exists
    if not dataset_path.exists():
        logger.error(f"Dataset not found: {dataset_path}")
        return False
    
    # Change to model directory and train
    original_cwd = os.getcwd()
    try:
        os.chdir(model_dir)
        logger.info(f"Changed directory to: {model_dir}")
        
        # Import and run training
        sys.path.insert(0, str(model_dir))
        
        logger.info("Starting model training...")
        import train
        train.main()
        
        # Verify model was created
        if model_path.exists():
            logger.info("✅ Model training completed successfully")
            return True
        else:
            logger.error("❌ Model training failed - model file not created")
            return False
            
    except Exception as e:
        logger.error(f"❌ Error during model training: {str(e)}")
        return False
    finally:
        os.chdir(original_cwd)
        if str(model_dir) in sys.path:
            sys.path.remove(str(model_dir))

if __name__ == "__main__":
    success = ensure_model_exists()
    sys.exit(0 if success else 1)