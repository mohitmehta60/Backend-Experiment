# Project File Structure - Backend API Deployment

This document provides a comprehensive overview of the Backend Experiment project structure optimized for Railway backend deployment. All frontend-related files have been removed, keeping only core backend API and ML components.

## Root Directory Structure

```
Backend Experiment/
├── .dockerignore                    # Docker ignore patterns
├── .env                            # Environment variables (local)
├── .env.example                    # Example environment variables template
├── .gitignore                      # Git ignore patterns
├── .vscode/                        # VS Code settings
│   └── settings.json               # VS Code workspace settings
├── app/                            # Core application module
│   ├── __init__.py                 # Python package initializer
│   ├── price_provider.py           # Price calculation service
│   ├── rate_table.json            # Rate/pricing data
│   └── __pycache__/               # Python compiled bytecode
├── My new ml model/                # Machine Learning model directory
│   ├── [Detailed structure below]  # See ML Model Section
├── tests/                          # All test files organized here
│   ├── __init__.py                 # Test package initializer
│   └── [Test files listed below]   # See Testing Section
├── __pycache__/                    # Python compiled bytecode
└── [Files listed below]            # See Core Files Section
```

## Core Files

### Main Application Files

- **`main.py`** - Primary FastAPI application entry point and API server
- **`soil_api.py`** - Soil analysis API endpoints and logic
- **`predictor.py`** - Machine learning prediction service
- **`llm.py`** - Large Language Model integration and processing

### Server and Deployment Files

- **`run_server.py`** - Production server runner
- **`start_server.py`** - Server startup script
- **`start_railway.py`** - Railway deployment starter (entry point)
- **`start.sh`** - Shell script for server initialization
- **`Dockerfile`** - Docker container configuration
- **`Procfile`** - Process file for Railway deployment
- **`railway.json`** - Railway platform configuration
- **`requirements.txt`** - Python dependencies (backend-optimized)

### Model and Training Files

- **`retrain_model.py`** - Model retraining utilities

### Utility Files

- **`final_verification.py`** - Final system verification
- **`integration_summary.py`** - Integration summary
- **`validate_startup.py`** - Startup validation script

## Testing Section (`tests/`)

### API Testing Files

- **`__init__.py`** - Test package initializer
- **`comprehensive_test.py`** - Comprehensive system testing
- **`quick_server_test.py`** - Quick server functionality test
- **`simple_balanced_npk_test.py`** - Simple NPK balance testing
- **`test_api.py`** - General API testing
- **`test_api_balanced_npk.py`** - Balanced NPK API testing
- **`test_api_integration.py`** - API integration testing
- **`test_balanced_npk_api.py`** - NPK balance API testing
- **`test_balanced_npk_fix.py`** - NPK balance fix testing
- **`test_balanced_npk_quantity_fix.py`** - NPK quantity fix testing
- **`test_complete_api.py`** - Complete API testing suite
- **`test_endpoint.py`** - Endpoint-specific testing
- **`test_enhanced_soil_api.py`** - Enhanced soil API testing
- **`test_full_integration.py`** - Full system integration testing
- **`test_health.py`** - Health check testing
- **`test_integration.py`** - Integration testing
- **`test_llm_integration.py`** - LLM integration testing
- **`test_model.py`** - Model testing
- **`test_new_model.py`** - New model testing
- **`test_soil_api.py`** - Soil API testing

## Machine Learning Model Directory (`My new ml model/`)

### Configuration Files

- **`.env`** - ML model environment variables
- **`.gitignore`** - Git ignore for ML model directory
- **`requirements.txt`** - ML-specific dependencies

### Model Files

- **`classifier.pkl`** - Trained classifier model (pickled)
- **`fertilizer.pkl`** - Fertilizer recommendation model (pickled)
- **`models/fertilizer_recommender.pkl`** - Main fertilizer recommender model

### Data Files

- **`New dataset 5111 rows.csv`** - Training dataset (5111 records)
- **`Dataset info.txt`** - Dataset information and metadata

### Core ML Application Files

- **`main.py`** - ML application main entry point
- **`predictor.py`** - ML prediction logic
- **`llm.py`** - LLM integration for ML model
- **`train.py`** - Model training script
- **`train_new.py`** - Updated training script
- **`demo_pricing.py`** - Pricing demonstration script

### Notebook

- **`finalferti.ipynb`** - Jupyter notebook for fertilizer analysis (kept for local development)

### Application Module (`app/`)

- **`__init__.py`** - Package initializer
- **`price_provider.py`** - Price calculation service
- **`rate_table.json`** - Rate and pricing data

### Model Training Information (`catboost_info/`)

- **`catboost_training.json`** - CatBoost training configuration
- **`learn_error.tsv`** - Training error logs
- **`time_left.tsv`** - Training time tracking
- **`learn/`** - Learning process files
- **`tmp/`** - Temporary training files

### Test Files (ML-specific in `tests/`)

- ML-specific test files have been moved to the main tests directory for better organization

## Key Features by Directory

### `/` (Root)

- FastAPI application with REST API endpoints
- Soil analysis and fertilizer recommendation APIs
- ML model integration and prediction services
- Railway deployment configuration
- Comprehensive testing suite

### `/app`

- Core business logic modules
- Price calculation services
- Rate management and pricing data

### `/My new ml model`

- Machine learning models and training scripts
- Data files and model evaluation
- Jupyter notebook for local development
- Model artifacts (.pkl files)

### `/tests`

- Organized test suite for all components
- API testing, integration testing, ML testing
- Comprehensive system verification tests

## Railway Deployment Configuration

### Entry Point

- **`start_railway.py`** - Main entry point for Railway deployment
- Configured for host='0.0.0.0' and Railway PORT environment variable
- Uses uvicorn ASGI server for FastAPI

### Dependencies

- **`requirements.txt`** - Optimized for backend-only deployment
- Includes FastAPI, uvicorn, gunicorn for production
- ML libraries: scikit-learn, pandas, numpy, xgboost, catboost
- Google Generative AI for LLM integration

### Process Configuration

- **`Procfile`** - Specifies `web: python start_railway.py`
- **`railway.json`** - Railway platform configuration
- **`Dockerfile`** - Docker container configuration (optional)

## Usage Notes

1. **API Entry Point:**

   - `main.py` - FastAPI application with all endpoints
   - Accessible via Railway URL once deployed

2. **Testing:**

   - All tests organized in `/tests` directory
   - Run with pytest or individual test files
   - Comprehensive API and ML model testing

3. **Railway Deployment:**

   - Automatic deployment via `start_railway.py`
   - Environment variables via `.env` (configure in Railway dashboard)
   - Scalable FastAPI backend with ML prediction capabilities

4. **Model Management:**
   - Pre-trained models stored as `.pkl` files
   - Training scripts available for model updates
   - Separate ML test suite for model validation

## Removed Components (Frontend)

The following have been removed for backend-only deployment:

- `/static/` - Static web assets
- `/templates/` - HTML templates
- `/docs/images/` - Frontend documentation diagrams
- `/My new ml model/images/` - Frontend image assets
- `/My new ml model/static/` and `/templates/` - ML frontend assets
- `jinja2` dependency from requirements.txt
- Local development files not needed for production

This structure now supports a pure backend API for fertilizer recommendations with ML capabilities, optimized for Railway deployment without frontend dependencies.

## Cleanup Summary

### ✅ Removed Frontend Components:

- `/static/` directory and all static assets
- `/templates/` directory and HTML templates
- `/docs/images/` frontend documentation diagrams
- `/My new ml model/images/` frontend image assets
- `/My new ml model/static/` and `/templates/` directories
- `jinja2` dependency from requirements.txt
- `main_backup.py` and `run_local.py` development files

### ✅ Organized Structure:

- All test files moved to `/tests/` directory
- Test package properly initialized with `__init__.py`
- ML test files consolidated from subdirectory

### ✅ Backend Optimization:

- Added `gunicorn` to requirements.txt for production deployment
- Removed unnecessary frontend dependencies
- Kept `finalferti.ipynb` for local ML development
- Maintained all core API and ML functionality

### ✅ Railway Ready:

- `start_railway.py` configured as entry point
- `Procfile` properly configured for web process
- All necessary backend dependencies included
- Environment variable support maintained
