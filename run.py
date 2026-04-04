#!/usr/bin/env python
"""
Convenience wrapper to run the document processing pipeline.
Run from project root: python run.py

Internally delegates to ai/run.py with proper sys.path setup.
"""
import os
import sys

# Ensure project root is on sys.path
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# Import and run the actual runner
from ai.run import main

if __name__ == "__main__":
    main()
