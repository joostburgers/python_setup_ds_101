#!/usr/bin/env python3
"""
Digital Studies 101 - Python Environment Setup Script

This script creates a proper virtual environment and installs all required packages
to avoid conflicts with system Python and Homebrew's externally-managed environment.

This solves the "externally-managed-environment" error and ensures Jupyter kernels
work correctly with VS Code.

Requirements:
- Python 3.8 or higher 
- Internet connection for downloading packages
- Homebrew (macOS) or system Python (Windows/Linux)

Compatible with:
- Windows 10/11
- macOS 10.15+ 
- Linux (Ubuntu 18.04+)
"""

import subprocess
import sys
import os
import platform
import venv
from pathlib import Path
import json

def check_python_version():
    """Check if Python version is compatible."""
    min_version = (3, 8)
    current_version = sys.version_info[:2]
    
    print(f"🐍 Python version: {sys.version}")
    print(f"🐍 Python executable: {sys.executable}")
    
    if current_version < min_version:
        print(f"❌ Python {min_version[0]}.{min_version[1]}+ is required, but you have {current_version[0]}.{current_version[1]}")
        print("💡 Please upgrade Python: https://www.python.org/downloads/")
        return False
    else:
        print(f"✅ Python version {current_version[0]}.{current_version[1]} is compatible")
        return True

def create_virtual_environment(venv_path):
    """Create a virtual environment for the course."""
    print(f"🔧 Creating virtual environment at: {venv_path}")
    
    try:
        # Remove existing venv if it exists
        if os.path.exists(venv_path):
            print("🗑️  Removing existing virtual environment...")
            import shutil
            shutil.rmtree(venv_path)
        
        # Create new virtual environment
        venv.create(venv_path, with_pip=True)
        print("✅ Virtual environment created successfully")
        return True
        
    except Exception as e:
        print(f"❌ Failed to create virtual environment: {e}")
        return False

def get_venv_python(venv_path):
    """Get the path to Python executable in the virtual environment."""
    system = platform.system()
    if system == "Windows":
        return os.path.join(venv_path, "Scripts", "python.exe")
    else:
        return os.path.join(venv_path, "bin", "python")

def get_venv_pip(venv_path):
    """Get the path to pip executable in the virtual environment."""
    system = platform.system()
    if system == "Windows":
        return os.path.join(venv_path, "Scripts", "pip.exe")
    else:
        return os.path.join(venv_path, "bin", "pip")

def upgrade_pip_in_venv(venv_path):
    """Upgrade pip in the virtual environment."""
    print("🔄 Upgrading pip in virtual environment...")
    venv_python = get_venv_python(venv_path)
    
    try:
        subprocess.check_call([venv_python, "-m", "pip", "install", "--upgrade", "pip"])
        print("✅ Pip upgraded successfully in virtual environment")
        return True
    except subprocess.CalledProcessError as e:
        print(f"⚠️  Failed to upgrade pip: {e}")
        return False

def install_package_in_venv(venv_path, package_name):
    """Install a package in the virtual environment."""
    venv_python = get_venv_python(venv_path)
    
    try:
        print(f"📦 Installing {package_name} in virtual environment...")
        subprocess.check_call([venv_python, "-m", "pip", "install", "--upgrade", package_name])
        print(f"✅ {package_name} installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install {package_name}: {e}")
        return False

def setup_jupyter_kernel(venv_path, kernel_name="ds101"):
    """Register the virtual environment as a Jupyter kernel."""
    venv_python = get_venv_python(venv_path)
    
    print(f"🔧 Setting up Jupyter kernel '{kernel_name}'...")
    
    try:
        # Install the kernel
        subprocess.check_call([
            venv_python, "-m", "ipykernel", "install", 
            "--user", 
            "--name", kernel_name,
            "--display-name", "Python (Digital Studies 101)"
        ])
        print(f"✅ Jupyter kernel '{kernel_name}' installed successfully")
        print(f"📝 This kernel will appear as 'Python (Digital Studies 101)' in VS Code")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to setup Jupyter kernel: {e}")
        return False

def create_vscode_settings(venv_path, workspace_path):
    """Create VS Code settings to use the virtual environment."""
    vscode_dir = os.path.join(workspace_path, ".vscode")
    settings_file = os.path.join(vscode_dir, "settings.json")
    
    # Create .vscode directory if it doesn't exist
    os.makedirs(vscode_dir, exist_ok=True)
    
    venv_python = get_venv_python(venv_path)
    
    # Convert to absolute path
    venv_python = os.path.abspath(venv_python)
    
    settings = {
        "python.pythonPath": venv_python,
        "python.defaultInterpreterPath": venv_python,
        "jupyter.kernels.filter": [
            {
                "path": venv_python,
                "type": "pythonEnvironment"
            }
        ]
    }
    
    try:
        # Read existing settings if they exist
        if os.path.exists(settings_file):
            with open(settings_file, 'r') as f:
                existing_settings = json.load(f)
            # Merge with new settings
            existing_settings.update(settings)
            settings = existing_settings
        
        # Write settings
        with open(settings_file, 'w') as f:
            json.dump(settings, f, indent=4)
        
        print(f"✅ VS Code settings created at: {settings_file}")
        print(f"🔧 Python interpreter set to: {venv_python}")
        return True
        
    except Exception as e:
        print(f"❌ Failed to create VS Code settings: {e}")
        return False

def check_and_download_nltk_data(venv_path):
    """Download required NLTK data packages."""
    venv_python = get_venv_python(venv_path)
    
    print("📚 Setting up NLTK data...")
    
    # NLTK download script
    nltk_script = '''
import nltk
import ssl

# Handle SSL certificate issues
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# Download required NLTK data
packages = ["punkt", "vader_lexicon"]
for package in packages:
    try:
        nltk.data.find(f"tokenizers/{package}" if package == "punkt" else package)
        print(f"✅ NLTK {package} already available")
    except LookupError:
        print(f"📥 Downloading NLTK {package}...")
        nltk.download(package, quiet=True)
        print(f"✅ NLTK {package} downloaded successfully")
'''
    
    try:
        subprocess.check_call([venv_python, "-c", nltk_script])
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to setup NLTK data: {e}")
        return False

def check_and_download_spacy_model(venv_path):
    """Download required spaCy language models."""
    venv_python = get_venv_python(venv_path)
    
    models = ["en_core_web_sm", "en_core_web_md"]
    print("🤖 Setting up spaCy models...")
    
    for model_name in models:
        try:
            print(f"📥 Downloading spaCy model {model_name}...")
            subprocess.check_call([venv_python, "-m", "spacy", "download", model_name])
            print(f"✅ spaCy model {model_name} downloaded successfully")
        except subprocess.CalledProcessError:
            print(f"⚠️  Failed to download spaCy model {model_name} - you can install it later")

def setup_geoparser(venv_path):
    """Setup geoparser and download GeoNames database."""
    venv_python = get_venv_python(venv_path)
    
    print("🌍 Setting up geoparser...")
    
    try:
        print("📥 Downloading GeoNames database (this may take a while)...")
        print("💾 This will download ~1GB of geographic data")
        
        subprocess.check_call([venv_python, "-m", "geoparser", "download", "geonames"])
        print("✅ GeoNames database downloaded successfully")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"⚠️  Failed to setup geoparser: {e}")
        print("💡 You can set this up later with: python -m geoparser download geonames")
        return False

def main():
    """Main setup function."""
    print("🚀 Digital Studies 101 - Python Environment Setup")
    print("=" * 60)
    print("This script creates a virtual environment to avoid conflicts")
    print("with system Python and ensures Jupyter works correctly.")
    print("=" * 60)
    
    # Check Python version
    if not check_python_version():
        print("\n❌ Setup aborted due to incompatible Python version.")
        sys.exit(1)
    
    # Determine paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    venv_name = "ds101_env"
    venv_path = os.path.join(script_dir, venv_name)
    
    print(f"\n🏠 Working directory: {script_dir}")
    print(f"📁 Virtual environment will be created at: {venv_path}")
    
    # Create virtual environment
    print(f"\n🔧 Setting up virtual environment...")
    print("-" * 40)
    if not create_virtual_environment(venv_path):
        print("❌ Failed to create virtual environment")
        sys.exit(1)
    
    # Upgrade pip in virtual environment
    if not upgrade_pip_in_venv(venv_path):
        print("⚠️  Pip upgrade failed, continuing anyway...")
    
    # Install packages in virtual environment
    packages = [
        # Essential Jupyter packages first
        "ipykernel",         # Required for Jupyter kernels
        "jupyterlab",        # JupyterLab interface
        "jupyter",           # Jupyter ecosystem
        "ipywidgets",        # Interactive widgets
        "notebook",          # Classic Jupyter notebook
        
        # Data science core
        "pandas",
        "numpy", 
        "matplotlib",
        "seaborn",
        "plotly",
        "mapclassify",
        
        # Progress bars and utilities
        "tqdm",
        
        # Reddit scraping (Lesson 1)
        "praw",
        
        # NLP packages (Lessons 4-5)
        "nltk",
        "spacy",
        "geoparser",
        
        # Machine Learning (Lesson 5)
        "transformers",
        "torch",
        "scipy",
        "scikit-learn",
        
        # Utilities
        "cryptography",
        "requests"
    ]
    
    print(f"\n📦 Installing packages in virtual environment...")
    print("-" * 40)
    
    failed_packages = []
    
    # Install essential packages first
    essential_packages = ["ipykernel", "jupyterlab", "jupyter"]
    print("Installing essential Jupyter packages first...")
    
    for package in essential_packages:
        if not install_package_in_venv(venv_path, package):
            failed_packages.append(package)
            print(f"❌ Critical package {package} failed to install!")
    
    # Check if essential packages were installed
    if any(pkg in failed_packages for pkg in essential_packages):
        print("❌ Critical Jupyter packages failed to install. Cannot continue.")
        sys.exit(1)
    
    # Install remaining packages
    for package in packages:
        if package not in essential_packages:  # Skip already installed
            if not install_package_in_venv(venv_path, package):
                failed_packages.append(package)
    
    # Setup Jupyter kernel
    print(f"\n🔧 Setting up Jupyter kernel...")
    print("-" * 40)
    if not setup_jupyter_kernel(venv_path):
        print("❌ Failed to setup Jupyter kernel")
        sys.exit(1)
    
    # Create VS Code settings
    print(f"\n⚙️  Configuring VS Code...")
    print("-" * 40)
    create_vscode_settings(venv_path, script_dir)
    
    # Setup NLP resources
    print(f"\n📚 Setting up NLP resources...")
    print("-" * 40)
    check_and_download_nltk_data(venv_path)
    check_and_download_spacy_model(venv_path)
    setup_geoparser(venv_path)
    
    # Final summary
    print(f"\n🎯 Setup Summary")
    print("=" * 60)
    
    if failed_packages:
        print(f"⚠️  Some packages failed to install: {', '.join(failed_packages)}")
        print("💡 You can install these manually later in the virtual environment")
    else:
        print("✅ All packages installed successfully!")
    
    print(f"\n📋 What was created:")
    print(f"• Virtual environment: {venv_path}")
    print(f"• Jupyter kernel: 'Python (Digital Studies 101)'")
    print(f"• VS Code settings: .vscode/settings.json")
    
    print(f"\n🔧 Next Steps:")
    print("1. Restart VS Code completely")
    print("2. Open this folder in VS Code")
    print("3. When opening a .ipynb file, select 'Python (Digital Studies 101)' kernel")
    print("4. VS Code should automatically use the virtual environment")
    
    print(f"\n💡 Manual activation (if needed):")
    system = platform.system()
    if system == "Windows":
        print(f"   {venv_path}\\Scripts\\activate")
    else:
        print(f"   source {venv_path}/bin/activate")
    
    print(f"\n✨ Environment Details:")
    venv_python = get_venv_python(venv_path)
    print(f"• Python executable: {venv_python}")
    print(f"• Packages installed in isolated environment")
    print(f"• No conflicts with system Python or Homebrew")
    
    print(f"\n🎉 Setup complete! Your Python environment is ready for Digital Studies 101.")

if __name__ == "__main__":
    main()